"""Endpoint collection module. The EndpointCollection is about orchestration of
different endpoints.

:author: Julian M. Kleber
"""
from bulkhead.endpoint_collection.interface import EndpointCollection


class WeatherEndpointCollection(EndpointCollection):
    """Interface for orchestration of different weather endpoints.

    :author: Julian M. Kleber
    """
