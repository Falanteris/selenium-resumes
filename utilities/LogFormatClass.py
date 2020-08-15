import inspect
import logging

class LogFormatClass():

    def get_logger_format_default(self,**kwargs):
        logger_name = "{}.log".format(inspect.stack()[1][3])
        if "logger_name" in kwargs:
            logger_name = kwargs["logger_name"]
        logger = logging.getLogger(logger_name)
        # file handler to be passed into the logger
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler = logging.FileHandler(logger_name)
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        """
        asctime: time and date
        levelname: log importane (debug, info, warning, etc.)
        the 's' in the end is to make it parsed as a string
        name: test name
        message : actual message from logger

        """
        """
        log hierarchy (bottom to top):
            1. debug
            2. info
            3. warning
            4. error
            5. critical
        using setLevel method from logger object would 
        only display specific log level.

        """
        # this will only make info and the levels below it visible
        logger.setLevel(logging.DEBUG)
        # this will only make error and the levels below it visible
        # logger.setLevel(logging.ERROR)
        return logger
    def get_logger_format_csv(self,**kwargs):
        # use inspect.stack()[1][3] to get the caller of this method
        logger_name = inspect.stack()[1][3]
        if "logger_name" in kwargs:
            logger_name = kwargs["logger_name"]
        logger = logging.getLogger(logger_name)
        template = logging.Formatter("%(asctime)s,%(levelname)s,%(name)s,%(message)s")
        file_handler = logging.FileHandler("log.csv")
        file_handler.setFormatter(template)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
