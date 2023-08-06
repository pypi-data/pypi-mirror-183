import pytest

from bulkhead.endpoint_collection.endpoint_collection import WeatherEndpointCollection
from bulkhead.endpoint.weather_endpoint import (
    Endpoint,
    EndpointOpenWeatherMap,
    EndpointTomorrowIO,
)
from bulkhead.sampler.sampler import SamplerEndpoints


value_name = "cloud_cover"

lon = 53.551086
lat = 9.993682

print("Single request")
print()
print()
owp_endpoint = EndpointOpenWeatherMap()
cloud_cover = owp_endpoint.get_value(lon=lon, lat=lat, value_name=value_name)
print("OpenWeatherMap:", cloud_cover)

tmio_endpoint = EndpointTomorrowIO()
cloud_cover = tmio_endpoint.get_value(lon=lon, lat=lat, value_name=value_name)
print("TomorrowIO:", cloud_cover)

endpoint_list = [owp_endpoint, tmio_endpoint]
ec = WeatherEndpointCollection(endpoint_list)
avg_cloud_cover = ec.get_mean(endpoints=ec.endpoints, value_name=value_name)
print("The Average is:", avg_cloud_cover)
print()
print()

print("Multiple requests:")
print()
print()

method = "get_mean"
interval = 0.2
num = 2
sampler_coll = SamplerEndpoints(object_instance=ec)
method_params = {"value_name": value_name}
multi_avg_cloud_cover = sampler_coll.sample_intervall(
    method_name="get_mean", method_params=method_params, interval=interval, num=num
)
print(
    "Multiple averages time interval = {interval} s:".format(interval=interval),
    multi_avg_cloud_cover,
)
