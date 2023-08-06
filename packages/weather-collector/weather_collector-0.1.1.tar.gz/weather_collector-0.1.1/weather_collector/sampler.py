"""
Module for formatting Python files

:author: Julian M. Kleber
"""
import os
import click
import time
import datetime

from typing import Any

from bulkhead.sampler.sampler import SamplerEndpoints
from bulkhead.endpoint_collection.endpoint_collection import WeatherEndpointCollection
from bulkhead.endpoint.weather_endpoint import (
    Endpoint,
    EndpointOpenWeatherMap,
    EndpointTomorrowIO,
)
from bulkhead.utils.file_utils import make_full_filename


@click.command()
@click.option("-o", help="Output file name")
@click.option("-i", help="Output file name")
@click.option("-l", help="Longitude")
@click.option("-t", help="Latitude")
def sample(o: str, i: float, l: float, t: float) -> None:
    """
    The sample function is a wrapper for the sample_infinite_intervall function.
    It takes in an output file path, and an interval as parameters. The output file
    path is used to create a directory where the sampled data will be saved, and
    the interval is used to determine how often sampling should occur. The sample
    wrapper function then calls the sample_infinite_intervall function with these two
    parameters along with some other parameters that are specific to this project.

    :param o:str: Used to Define the output file name and location.
    :param i:float: Used to Set the interval in seconds.
    :return: A nonetype object.

    :doc-author: Julian M. Kleber
    """
    lon = l
    lat = t

    save_dir = os.path.dirname(o)
    file_name = os.path.basename(o)

    header = ["time_stamp", "Tomorrow.io", "OpenWeatherMap", "mean"]

    value_name = "cloud_cover"
    method_name = "get_time_mean_atomic_vals"
    method_parameters = {"value_name": value_name}
    interval = i

    ec = weather_collection(value_name=value_name, lon=lon, lat=lat)
    sampler = SamplerEndpoints(object_instance=ec)

    sample_infinite_intervall(
        file_name=file_name,
        save_dir=save_dir,
        header=header,
        method_name=method_name,
        interval=interval,
        sampler=sampler,
        method_parameters=method_parameters,
        lon=lon,
        lat=lat,
    )


def sample_infinite_intervall(**kwargs: Any) -> None:
    """
    The sample_infinite_intervall function samples the data from a given interval and saves it to a csv file.
        The function is called in an infinite loop, so that the sampling can be done continuously.

    :param **kwargs:Any: Used to Pass in a dictionary of arguments.
    :return: Nothing.

    :doc-author: Julian M. Kleber
    """
    file_name = str(kwargs["file_name"])
    save_dir = str(kwargs["save_dir"])
    header = list(kwargs["header"])
    method_name = str(kwargs["method_name"])
    interval = int(kwargs["interval"])
    sampler = kwargs["sampler"]
    method_parameters = kwargs["method_parameters"]
    lon = float(kwargs["lon"])
    lat = float(kwargs["lat"])

    while True:
        try:
            data = sampler.sample_intervall(
                method_name=method_name,
                interval=0,
                num=1,
                method_parameters=method_parameters,
                lon=lon,
                lat=lat,
            )[0]
            print(data)
            check_name = make_full_filename(save_dir, file_name)
            if os.path.isfile(check_name):
                sampler.save_to_csv(save_dir, file_name, data)
            else:
                sampler.save_to_csv(save_dir, file_name, data, header)
        except Exception as e:
            print(
                "Could not sample data at time {time}".format(
                    time=str(datetime.datetime.now())
                )
            )
            print(e)
            continue
        finally:
            time.sleep(interval)


def weather_collection(lon: float, lat: float, value_name: str):

    owp_endpoint = EndpointOpenWeatherMap()

    tmio_endpoint = EndpointTomorrowIO()
    endpoint_list = [owp_endpoint, tmio_endpoint]
    ec = WeatherEndpointCollection(endpoint_list)

    return ec


if __name__ == "__main__":
    sample()
