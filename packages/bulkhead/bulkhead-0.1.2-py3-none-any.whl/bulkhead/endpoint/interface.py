from http.client import HTTPSConnection

from bulkhead.base_interface import BaseInterface

from abc import ABC, abstractmethod
import json

from typing import Callable, Any, Type, Dict


class Endpoint(BaseInterface, ABC):
    """Interface for implementing Endpoint objects.

    :author: Julian M. Kleber
    """

    def parse_request(
        self,
        response: Dict[str, Any],
        parsing_func: Callable[[Dict[str, Any]], Any],
    ) -> Any:

        value = parsing_func(response)
        return value

    @abstractmethod
    def get_value(self, **kwargs: Any) -> Any:
        pass  # pragma: no cover

    @abstractmethod
    def request(self, **kwargs: Any) -> Dict[str, Any]:
        pass  # pragma: no cover

    def get_dict_response(self, conn: HTTPSConnection) -> Dict[str, Any]:
        """The get_dict_response function takes a connection object as an
        argument and returns the response from the server in dictionary form.
        The function first gets the response from the server, then decodes it
        into a string, and finally loads it into a dictionary.

        :param conn: Used to Get the response from the server.
        :return: A dictionary.

        :doc-author: Julian M. Kleber
        """

        res = conn.getresponse()
        data = res.read()
        string_response = data.decode("utf-8")
        dict_response = dict(json.loads(string_response))
        return dict_response
