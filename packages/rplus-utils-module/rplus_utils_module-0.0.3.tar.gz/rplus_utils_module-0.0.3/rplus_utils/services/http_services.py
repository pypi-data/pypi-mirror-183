import io
from http import HTTPStatus
from typing import List, Dict, Any

import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException


class HttpServices:
    def __init__(
        self,
        base_url: str,
        default_time_out: int = 10,
    ):
        # if base url have end with slash and then remove this slash
        # example http://localhost/
        # then it will remove las slash to like this http://localhost
        if base_url.endswith("/"):
            base_url = base_url[:-1]

        self.base_url = base_url
        self.cl = requests.session()
        self.default_time_out = default_time_out

    @classmethod
    def from_base_url(
        cls,
        base_url: str,
        default_timeout: int = 10,
    ) -> "HttpServices":
        """Create new object based on specified base url
        :param base_url: string base url
        :param default_timeout: int default timeout for request
        :return: current object class
        """
        return cls(
            base_url,
            default_timeout,
        )

    def put(
        self,
        url: str,
        username: str = None,
        password: str = None,
        data: bytes = None,
    ) -> List[Dict[str, Any]]:
        """Fetch data from services services and return as list of dictionary
        :param url: string url
        :param username: string url
        :param password: string url
        :param data: bytes data to update
        :return: list of dictionary
        """
        try:
            # if base url have end with slash and then remove this slash
            # example /user/123
            # then it will remove las slash to like this user/123
            if url.startswith("/"):
                url = url[1:]

            url = "{}/{}".format(self.base_url, url)
            if username is not None and password is not None:
                resp = self.cl.put(
                    url,
                    timeout=self.default_time_out,
                    data=data,
                    auth=HTTPBasicAuth(username, password),
                )
                if resp.status_code == HTTPStatus.NOT_FOUND:
                    return []

                return resp.json()

            resp = self.cl.put(url, timeout=self.default_time_out, data=data)
            if resp.status_code == HTTPStatus.NOT_FOUND:
                return []

            return resp.json()
        except RequestException as t:
            return []

    def get(
        self,
        url: str,
        username: str = None,
        password: str = None,
    ) -> List[Dict[str, Any]]:
        """Fetch data from services services and return as list of dictionary
        :param url: string url
        :param username: string url
        :param password: string url
        :return: list of dictionary
        """
        try:
            # if base url have end with slash and then remove this slash
            # example /user/123
            # then it will remove las slash to like this user/123
            if url.startswith("/"):
                url = url[1:]

            url = "{}/{}".format(self.base_url, url)
            if username is not None and password is not None:
                resp = self.cl.get(
                    url,
                    timeout=self.default_time_out,
                    auth=HTTPBasicAuth(username, password),
                )
                if resp.status_code == HTTPStatus.NOT_FOUND:
                    return []

                return resp.json()

            resp = self.cl.get(url, timeout=self.default_time_out)
            if resp.status_code == HTTPStatus.NOT_FOUND:
                return []

            return resp.json()
        except RequestException as t:
            return []

    def delete(
        self,
        url: str,
        username: str = None,
        password: str = None,
    ) -> bool:
        """Fetch data from services services and return as list of dictionary
        :param url: string url
        :param username: string url
        :param password: string url
        :return: boolean true or false
        """
        try:
            # if base url have end with slash and then remove this slash
            # example /user/123
            # then it will remove las slash to like this user/123
            if url.startswith("/"):
                url = url[1:]

            url = "{}/{}".format(self.base_url, url)
            if username is not None and password is not None:
                resp = self.cl.delete(
                    url,
                    timeout=self.default_time_out,
                    auth=HTTPBasicAuth(username, password),
                )
                return resp.status_code == 200

            resp = self.cl.delete(url, timeout=self.default_time_out)
            return resp.status_code == 200
        except RequestException as t:
            return False

    def get_raw(
        self,
        url: str,
        username: str = None,
        password: str = None,
    ) -> bytes:
        """Fetch data from services services and return as list of dictionary
        :param url: string url
        :param username: string url
        :param password: string url
        :return: bytes data
        """
        try:
            # if base url have end with slash and then remove this slash
            # example /user/123
            # then it will remove las slash to like this user/123
            if url.startswith("/"):
                url = url[1:]

            url = "{}/{}".format(self.base_url, url)
            if username is not None and password is not None:
                resp = self.cl.get(
                    url,
                    timeout=self.default_time_out,
                    auth=HTTPBasicAuth(username, password),
                )
                if resp.status_code == HTTPStatus.NOT_FOUND:
                    return b""

                return resp.content

            resp = self.cl.get(url, timeout=self.default_time_out)
            if resp.status_code == HTTPStatus.NOT_FOUND:
                return b""

            return resp.content
        except RequestException as t:
            return b""

    def load_to_dataframe(
        self,
        url: str,
        username: str = None,
        password: str = None,
    ) -> pd.DataFrame:
        """Load csv from url and convert as dataframe
        we will chunk load data cause the data can be huge
        example:
            cls = HttpServices.from_base_url("https://cloud.mnc-cloud.xyz")
            resp = cls.load_to_dataframe("index.php/s/3i4TnZS38xRNHfB/download")
            for df in resp:
                print(len(df))
        :param url: string url
        :param username: string username
        :param password: string password
        :return: dataframe object generator
        """
        # if base url have end with slash and then remove this slash
        # example /user/123
        # then it will remove las slash to like this user/123
        if url.startswith("/"):
            url = url[1:]

        # get raw data from services
        if username is not None and password is not None:
            data = self.get_raw(url, username, password)
            # ida data is empty
            if len(data) == 0:
                return pd.DataFrame()

            resp = pd.read_csv(
                io.BytesIO(data),
                on_bad_lines="skip",
            )
            return resp

        data = self.get_raw(url)
        # ida data is empty
        if len(data) == 0:
            return pd.DataFrame()

        resp = pd.read_csv(
            io.BytesIO(data),
            on_bad_lines="skip",
        )
        return resp
