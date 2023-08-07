"""Endpoint collection module. The EndpointCollection is about orchestration of
different endpoints. This module only provides the sample interface.

:author: Julian M. Kleber
"""
import datetime

from abc import ABC
from typing import Optional, Any, Type, List, Optional, Union


from bulkhead.endpoint.weather_endpoint import (
    EndpointWeather,
)
from bulkhead.base_interface import BaseInterface


class EndpointCollection(BaseInterface, ABC):
    """Interface for orchestration of different endpoints.

    :author: Julian M. Kleber
    """

    def __init__(self, endpoints: list[Type[EndpointWeather]]) -> None:
        self.endpoints = endpoints

    def get_time_mean_atomic_vals(
        self,
        lon: float,
        lat: float,
        value_name: str,
        endpoints: Optional[List[Type[EndpointWeather]]] = None,
    ) -> List[Union[int, str]]:
        """
        The get_time_mean_atomic_vals function takes in a value_name and endpoints.
        The value_name is the name of the attribute that you want to get from each endpoint.
        The endpoints are a list of EndpointWeather objects, which contain attributes such as temperature, humidity, etc.
        This function returns a list containing:
            1) The current time (as string)
            2) The values for each endpoint (in order), and
            3) The mean of all those values

        :param self: Used to Represent the instance of the class.
        :param value_name:str: Used to Specify which value we want to get the mean of.
        :param endpoints:Optional[List[Type[EndpointWeather]]]=None: Used to Pass in a list of endpoints.
        :return: A list of values.

        :doc-author: Julian M. Kleber
        """

        if endpoints is None:
            endpoints = self.endpoints

        cum_sum = 0
        result: List[Union[int, str]]
        result = []
        result.append(str(datetime.datetime.now()))
        calculate_mean = True

        for i in range(len(endpoints)):

            try:
                value = endpoints[i].get_value(
                    lon=lon, lat=lat, value_name=value_name)
                cum_sum += value
                result.append(value)
            except:
                value = ""
                calculate_mean = False
                result.append(value)
            finally:
                continue

        if calculate_mean is True:

            value = int(cum_sum / len(endpoints))
            result.append(value)
        else:
            result.append("")

        return result

    def get_mean(
        self,
        value_name: str,
        endpoints: Optional[List[Type[EndpointWeather]]] = None,
        **kwargs
    ) -> int:
        """The get_mean function takes a list of endpoints and a value to
        calculate the mean for the attribute of the objects in the list
        specified by value.

        It then iterates through each endpoint in the list, adding up all values for that attribute.
        Finally, it returns an integer representing the mean of those values.

        :param self: Used to Represent the instance of the object itself.
        :param endpoints:list[type(Endpoint)]: Used to pass in a list of endpoint objects.
        :param value:str: Used to specify the key of the dictionary that is being used to
                          calculate the mean.
        :return: The mean of the values in a list.

        :doc-author: Julian M. Kleber
        """
        if endpoints is None:
            endpoints = self.endpoints
        cum_sum = 0

        for endpoint in endpoints:
            cum_sum += endpoint.__dict__[value_name]

        return int(cum_sum / len(endpoints))

    def get_method(self, method_name: str) -> Any:
        return getattr(self, method_name)
