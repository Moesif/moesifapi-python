import logging


class APILogger:
    def __init__(self, name,
                 level=logging.DEBUG):

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

    def get_logger(self):
        return self.logger
