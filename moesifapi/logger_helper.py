import os


class LoggerHelper:
    def __init__(self):
        pass

    @classmethod
    def get_worker_pid(cls):
        return str(os.getpid())
