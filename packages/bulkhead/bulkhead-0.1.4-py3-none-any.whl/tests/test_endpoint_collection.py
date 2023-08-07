from bulkhead.endpoint_collection.endpoint_collection import WeatherEndpointCollection
from bulkhead.endpoint.weather_endpoint import (
    Endpoint,
    EndpointOpenWeatherMap,
    EndpointTomorrowIO,
)
from tests.make_collection import weather_collection


def test_endpoint_collection_cloud_cover(weather_collection):

    value_name = "cloud_cover"
    ec = weather_collection
    avg_cloud_cover = ec.get_mean(endpoints=ec.endpoints, value_name=value_name)
    assert (
        isinstance(avg_cloud_cover, int)
        and avg_cloud_cover <= 100
        and avg_cloud_cover >= 0
    )

def test_endpoint_collection_cloud_cover(weather_collection):

    #value_name = "solar_radiation"
    #ec = weather_collection
    #avg_cloud_cover = ec.get_mean(endpoints=ec.endpoints, value_name=value_name)
    #assert (
    #    isinstance(avg_cloud_cover, int)
    #    and avg_cloud_cover <= 100
    #    and avg_cloud_cover >= 0
    #)
    pass