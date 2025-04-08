import math
import queue
import threading
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
import atexit
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class Batcher:
    """
    A class used for batching events. This runs in a single background thread,
    and consumes events from the input queue, executes batch size and maximum
    wait time constraints and puts batches of events into the batch queue for
    the worker threads to consume.
    """

    def __init__(self, event_queue, batch_queue, batch_size, timeout, api_client, config, debug):
        logger.debug("Initializing Batcher")
        self.event_queue = event_queue  # input queue
        self.batch_queue = batch_queue  # output queue
        # batch_size is used to control how many events are in a batch maximum
        self.batch_size = batch_size
        # timeout is used to control how long the batcher will wait for the next event
        self.timeout = timeout
        self.debug = debug
        self.api_client = api_client
        self.config = config
        self.worker = Worker(self.batch_queue, self.api_client, self.config, self.debug)

    def create_batch(self):
        batch_events = []
        try:
            while not self.event_queue.empty():
                event = self.event_queue.get_nowait()
                batch_events.append(event)
                if len(batch_events) == self.batch_size:
                    break
            if batch_events:
                self.worker.send_events(batch_events)
            else:
                if self.debug:
                    logger.info("No events to send")
        except:
            if self.debug:
                logger.info("No message to read from the queue")

class Worker:
    """
    A class used for sending events to Moesif asynchronously. This runs in a pool of
    background threads, and consumes batches of events from the batch queue.
    """

    def __init__(self, queue, api_client, config, debug):
        logger.debug("Initializing Worker")
        self.queue = queue
        self.api_client = api_client
        self.config = config
        self.debug = debug

    def send_events(self, batch_events):
        try:
            logger.debug("Sending events to Moesif")
            self.api_client.create_events_batch(batch_events)
            if self.debug:
                logger.debug("Events sent successfully to Moesif")
        except Exception as ex:
            logger.exception(f"Error sending event to Moesif. {str(ex)}")


class BatchedWorkerPool:
    """
    A class used for managing a pool of workers and a batcher. This class is
    responsible for starting and stopping the workers and the batcher, and
    for adding events to the event queue.
    """

    def __init__(self, worker_count, api_client, config, debug, max_queue_size, batch_size, timeout):
        logger.debug("Initializing BatchedWorkerPool")
        self.event_queue = queue.Queue(maxsize=max_queue_size)
        self.batch_queue = queue.Queue(maxsize=math.ceil(max_queue_size / batch_size))
        self.batch_size = batch_size
        self.timeout = timeout
        self.worker_count = worker_count
        self.api_client = api_client
        self.config = config
        self.debug = debug
        self.scheduler = None

        self.last_event_job_run_time = datetime(1970, 1, 1, 0, 0)  # Assuming job never ran, set it to epoch start time

        # Create an instance of batcher
        self.batcher = Batcher(self.event_queue, self.batch_queue, self.batch_size, self.timeout, self.api_client, self.config, self.debug)

    def exit_config_job(self):
        try:
            # Shut down the scheduler
            self.scheduler.remove_job('moesif_event_job')
            self.scheduler.shutdown()
        except Exception as ex:
            if self.debug:
                logger.info(f"Error during shut down of the event scheduler. {str(ex)}")

    # Function to listen to the send event job response
    def moesif_event_listener(self, event):
        if event.exception:
            if self.debug:
                print('Error reading response from the event scheduled job')
        else:
            self.last_event_job_run_time = datetime.utcnow()


    def schedule_background_job(self):
        try:
            if not self.scheduler:
                self.scheduler = BackgroundScheduler(daemon=True)
            if not self.scheduler.get_jobs():
                self.scheduler.add_listener(self.moesif_event_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
                self.scheduler.start()
                self.scheduler.add_job(
                    func=lambda: self.batcher.create_batch(),
                    trigger=IntervalTrigger(seconds=self.timeout),
                    id='moesif_event_job',
                    name=f'Schedule event job every {self.timeout} second(s)',
                    replace_existing=True)

                # Avoid passing logging message to the ancestor loggers
                if self.debug:
                    logging.getLogger('apscheduler').setLevel(logging.WARNING)
                    logging.getLogger('apscheduler.executors.default').setLevel(logging.WARNING)
                else:
                    logging.getLogger('apscheduler').setLevel(logging.ERROR)
                    logging.getLogger('apscheduler.executors.default').setLevel(logging.ERROR)
                logging.getLogger('apscheduler.executors.default').propagate = False

                # Exit handler when exiting the app
                atexit.register(lambda: self.exit_config_job)
        except Exception as ex:
            if self.debug:
                logger.info(f"Error when scheduling the event job. {str(ex)}")

    def add_event(self, event):
        # Add event to the event queue if it's not full
        # do not block and return immediately, True if successful, False if not
        try:
            if datetime.utcnow() > self.last_event_job_run_time + timedelta(minutes=5):
                try:
                    self.schedule_background_job()
                    self.last_event_job_run_time = datetime.utcnow()
                except Exception as ex:
                    if self.debug:
                        logger.info(f'Error while starting the event scheduler job in background: {str(ex)}')

            self.event_queue.put(event, block=False)
            return True
        except queue.Full:
            return False
        except Exception as ex:
            if self.debug:
                logger.info(f"Error while adding event to the queue: {str(ex)}")
            return False

    def stop(self):
        logging.debug("Stopping BatchedWorkerPool")
        if self.batcher:
            self.batcher.stop()
            self.batcher.join()

        for worker in self.workers:
            worker.stop()

        # Wait for all tasks in the queue to be processed
        self.batch_queue.join()

        for worker in self.workers:
            worker.join()

        # Clear workers
        self.batcher = None
        self.workers = []


class ConfigJobScheduler:

    def __init__(self, debug, config):
        self.debug = debug
        self.scheduler = None
        self.config = config

    def exit_config_job(self):
        try:
            # Shut down the scheduler
            self.scheduler.remove_job('moesif_config_job')
            self.scheduler.shutdown()
        except Exception as ex:
            if self.debug:
                logger.info(f"Error during shut down of the config scheduler. {str(ex)}")

    def schedule_background_job(self):
        try:
            if not self.scheduler:
                self.scheduler = BackgroundScheduler(daemon=True)
            if not self.scheduler.get_jobs():
                self.scheduler.start()
                self.scheduler.add_job(
                    func=lambda: self.config.update_configuration(),
                    trigger=IntervalTrigger(seconds=60),
                    id='moesif_config_job',
                    name='Schedule config job every 60 second',
                    replace_existing=True)

                # Avoid passing logging message to the ancestor loggers
                if self.debug:
                    logging.getLogger('apscheduler').setLevel(logging.WARNING)
                    logging.getLogger('apscheduler.executors.default').setLevel(logging.WARNING)
                else:
                    logging.getLogger('apscheduler').setLevel(logging.ERROR)
                    logging.getLogger('apscheduler.executors.default').setLevel(logging.ERROR)
                logging.getLogger('apscheduler.executors.default').propagate = False

                # Exit handler when exiting the app
                atexit.register(lambda: self.exit_config_job)
        except Exception as ex:
            if self.debug:
                logger.info(f"Error when scheduling the config job. {str(ex)}")
