"""Module to sample from  a given endpoint or endpoint collection. This file
only provides basic interfaces.

:author: Julian M. Kleber
"""
import os
import csv
from abc import ABC, abstractmethod

from typing import Any, Dict, List

from bulkhead.base_interface import BaseInterface
from bulkhead.endpoint.weather_endpoint import EndpointWeather
from bulkhead.utils.file_utils import check_make_dir, make_full_filename


class Sampler(BaseInterface, ABC):
    """
    Abstract Python class to model a sampler calling an Object
    in regular time intervals and processing the output
    """

    def __init__(self, object_instance: Any) -> None:
        self.object_instance = object_instance

    @abstractmethod
    def sample_intervall(self, **kwargs: Dict[Any, Any]) -> list[Any]:
        """The sample_intervall function is used to sample the intervall of a
        given distribution. The function takes in a dictionary with keys:

                    - 'distribution' : str, name of the distribution (e.g., 'normal')
                    - 'parameters' : dict, parameters for the chosen distribution
                                             (e.g., {'loc': 0, 'scale': 1})

                Returns: list[Any]

        :param **kwargs:Dict[Any: Used to Pass a dictionary of parameters to the function.
        :param Dict[Any, Any]: Used to Define the type of data that can be passed to the function.
        :return: A list of values for which the probability density function is greater than 0.

        :doc-author: Julian M. Kleber
        """

        raise NotImplementedError  # pragma: no cover

    def save_to_csv(
        self,
        save_dir: str,
        file_name: str,
        data: List[Any],
        header: List[Any] = [],
    ) -> None:
        """
        The save_to_csv function saves a list of data to a CSV file.

        :param file_name:str: Used to Specify the name of the file to be written.
        :param data:List[Any]: Used to Pass in a list of data to be written to the csv file.
        :param header:List[str]: Used to Specify the header row of the csv file.
        :return: None.

        :doc-author: Julian M. Kleber
        """
        write_header = False
        if len(header) > 0:
            try:
                assert len(data) == len(header)
                write_header = True
            except:
                raise RuntimeError(
                    "Input data and input header do not have the same number of fields ({len_data}, {len_header}). Please ensure an appropriate data structure.".format(
                        len_data=len(data), len_header=len(header)
                    )
                )
        if not os.path.isdir(save_dir):
            check_make_dir(save_dir)
            with open(file_name, "w", newline="") as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=";")
                if write_header:
                    csv_writer.writerow(header)
                csv_writer.writerow(data)
        else:
            file_name = make_full_filename(save_dir, file_name)
            with open(file_name, "a", newline="") as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=";")
                if write_header:
                    csv_writer.writerow(header)
                csv_writer.writerow(data)
