import logging


class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
            cls._instance.logger_setup()
        return cls._instance

    def logger_setup(self):
        self.logger = logging.getLogger("Mylogger")
        self.logger.setLevel(logging.INFO)

