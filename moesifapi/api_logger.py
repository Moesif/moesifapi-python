import logging


class APILogger:
    def __init__(self, name,
                 level=logging.DEBUG,
                 log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        formatter = logging.Formatter(log_format)

        # handler
        customize_handler = logging.StreamHandler()
        customize_handler.setFormatter(formatter)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.addHandler(customize_handler)

    def get_logger(self):
        return self.logger
