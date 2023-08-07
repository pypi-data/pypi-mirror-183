import os 

from bulkhead.endpoint.weather_endpoint import EndpointOpenWeatherMap, EndpointTomorrowIO
from bulkhead.endpoint_collection.endpoint_collection import WeatherEndpointCollection
from bulkhead.sampler.sampler import SamplerEndpoints

from tests.make_collection import weather_collection


def test_sample_endpoint_collection_mean_cloud_cover(weather_collection):

    ec = weather_collection
    value_name = "cloud_cover"
    method_name = "get_mean"
    interval = 0.2
    num = 2
    lon = 53.551086
    lat = 9.993682

    sampler_coll = SamplerEndpoints(object_instance=ec)
    method_parameters = {"value_name": value_name}
    multi_avg_cloud_cover = sampler_coll.sample_intervall(
        method_name=method_name,
        method_parameters=method_parameters,
        interval=interval,
        num=num,
        lon=lon, 
        lat = lat
    )
    assert len(multi_avg_cloud_cover) == num

    val1, val2 = multi_avg_cloud_cover
    assert isinstance(val1, int) and val1 >= 0 and val1 <= 100
    assert isinstance(val2, int) and val1 >= 0 and val1 <= 100


def test_timestamped_atomic_sampling(weather_collection):

    lon = 53.551086
    lat = 9.993682
    save_dir = "tests/results/"
    result_file = "test_sampler_save.csv"
    sample_header = ["time_stamp", "Tomorrow.io", "OpenWeatherMap", "Mean"]

    ec = weather_collection
    value_name = "cloud_cover"
    method_name = "get_time_mean_atomic_vals"
    interval = 0.2
    num = 2

    sampler_coll = SamplerEndpoints(object_instance=ec)
    method_parameters = {"value_name": value_name}
    multi_avg_cloud_cover = sampler_coll.sample_intervall(
        method_name=method_name,
        method_parameters=method_parameters,
        interval=interval,
        num=num,
        lon = lon, 
        lat = lat
    )

    #assert len(prod_result_atomic_values_timestamped) == 4
    sampler_coll.save_to_csv(save_dir = save_dir, file_name=result_file, data=multi_avg_cloud_cover[0])

    results = os.listdir("tests/results")
    assert "test_sampler_save.csv" in results
