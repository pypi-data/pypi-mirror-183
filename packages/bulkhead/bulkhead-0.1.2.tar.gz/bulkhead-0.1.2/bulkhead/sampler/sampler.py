"""Module to sample from  a given endpoint or endpoint collection.

:author: Julian M. Kleber
"""

import time


from typing import Any, List, Optional, Type

from bulkhead.sampler.interface import Sampler


class SamplerEndpoints(Sampler):
    """Class to sample Edpoints or collection of endpoints regularly.

    :author: Julian M. Kleber
    """

    def sample_intervall(self, **kwargs: Any) -> List[Any]:

        method_name = str(kwargs["method_name"])
        interval = int(kwargs["interval"])
        num = int(kwargs["num"])
        method_parameters = dict(kwargs["method_parameters"])
        lon = float(kwargs["lon"])
        lat = float(kwargs["lat"])

        method = self.object_instance.get_method(method_name=method_name)
        counter = 0
        result = []
        while counter < num:
            result.append(method(lon=lon, lat=lat, **method_parameters))
            time.sleep(interval)
            counter += 1
        return result
