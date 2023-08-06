import inspect
import logging
from typing import Any, Dict

from rplus_constants.logger import LOG_FORMATTING, LOG_TYPE, INFO
from rplus_constants.rplus_utils_module import SERVICE_NAME

logging.basicConfig(
    handlers=[logging.StreamHandler()],
    format=LOG_FORMATTING,
    level=LOG_TYPE[INFO],
)


class Logging:
    @staticmethod
    def get_logger():
        return logging

    @staticmethod
    def formatting_message(msg: Any) -> Dict[str, Any]:
        """formatting message to get better logs
        :param msg: message that want to print
        :return: dictionary message
        """
        func_inspection = inspect.stack()
        default_msg = {
            "service_name": SERVICE_NAME,
            "text": msg,
            "func_name": "{}:{}".format(
                func_inspection[2].function, func_inspection[2].lineno
            ),
            "func_file_path": func_inspection[2].filename,
        }
        return default_msg

    @staticmethod
    def info(message: Any):
        """Print logging info message
        :param message: any message
        :return: None
        """
        logging.info(Logging.formatting_message(message))

    @staticmethod
    def debug(message: Any):
        """Print logging debug message
        :param message: any message
        :return: None
        """
        logging.debug(Logging.formatting_message(message))

    @staticmethod
    def error(message: Any):
        """Print logging error message
        :param message: any message
        :return: None
        """
        logging.error(Logging.formatting_message(message))

    @staticmethod
    def warning(message: Any):
        """Print logging warning message
        :param message: any message
        :return: None
        """
        logging.warning(Logging.formatting_message(message))

    @staticmethod
    def exception(message: Any):
        """Print logging exception() message
        :param message: any message
        :return: None
        """
        logging.exception(Logging.formatting_message(message))
