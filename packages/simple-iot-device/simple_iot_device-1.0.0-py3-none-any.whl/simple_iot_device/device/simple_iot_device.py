from dataclasses import dataclass, asdict
from random import gauss, seed, uniform

from simple_iot_device.prototype import AbstractIOTDevice
from .utils import get_utc_time_as_string


@dataclass
class SimpleIOTDeviceMeasurement:
    ts: str
    temperature: float
    pressure: float
    relative_humidity: float


class SimpleIOTDevice(AbstractIOTDevice):
    def __init__(self, name, description=None):
        if description is None:
            description = "Simple IOT Device"
        super().__init__(name=name, description=description)
        seed()

    def make_measurement(self) -> dict:
        ts = get_utc_time_as_string()
        temperature = 22 + gauss(0, 3)
        pressure = 101.3 + gauss(0, 5)
        relative_humidity = 0.35 + uniform(-0.075, 0.075)

        measurement = SimpleIOTDeviceMeasurement(
            ts=ts,
            temperature=round(temperature, 2),
            pressure=round(pressure, 2),
            relative_humidity=round(relative_humidity),
        )
        return asdict(measurement)
