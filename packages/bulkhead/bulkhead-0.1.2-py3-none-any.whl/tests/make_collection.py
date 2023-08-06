import pytest

from bulkhead.endpoint_collection.endpoint_collection import WeatherEndpointCollection
from bulkhead.endpoint.weather_endpoint import (
    Endpoint,
    EndpointOpenWeatherMap,
    EndpointTomorrowIO,
)


@pytest.fixture
def weather_collection():

    value_name = "cloud_cover"

    lon = 53.551086
    lat = 9.993682

    owp_endpoint = EndpointOpenWeatherMap()
    cloud_cover = owp_endpoint.get_value(lon=lon, lat=lat, value_name=value_name)
    assert isinstance(cloud_cover, int) and cloud_cover <= 100 and cloud_cover >= 0

    tmio_endpoint = EndpointTomorrowIO()
    cloud_cover = tmio_endpoint.get_value(lon=lon, lat=lat, value_name=value_name)
    assert isinstance(cloud_cover, int) and cloud_cover <= 100 and cloud_cover >= 0

    endpoint_list = [owp_endpoint, tmio_endpoint]
    ec = WeatherEndpointCollection(endpoint_list)

    return ec
