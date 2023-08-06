import base64
from typing import List, Dict, Any, Union


def encode_string(text: str) -> str:
    """Base64 encode string from plain text
    :param text: string plain text
    :return: string base 64 value
    """
    return base64.b64encode(text.encode("ascii")).decode("ascii")


def decode_string(text: str) -> str:
    """Base64 encode string from plain text
    :param text: string plain text
    :return: string base 64 value
    """
    return base64.b64decode(text.encode("ascii")).decode("ascii")


def paginate(
    data: Union[List[Dict[str, Any]], List[Any]],
    page_no: int = 1,
    page_size: int = 50,
) -> Union[List[Dict[str, Any]], List[Any]]:
    """Pagination logic
    :param data: all data that need to paginate
    :param page_no: int page number
    :param page_size: int page size
    :return: all chunk data
    """
    if data is None or len(data) == 0:
        return []

    if page_no == 1 or page_no == 0:
        return data[:page_size]

    n = (page_no - 1) * page_size
    return data[n : n + page_size]


def hash_string(text: str) -> str:
    """Hash string with base64
    :param text: string text
    :return: return string text
    """
    return base64.b64encode(
        "{}".format(
            text,
        ).encode("utf-8")
    ).decode("utf-8")
