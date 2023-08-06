import os
from abc import ABCMeta, abstractmethod


class AbstractIOTDevice(metaclass=ABCMeta):
    def __init__(self, name, frequency=1, description=None):
        self.name = name
        self.host = os.uname().nodename
        self.description = description

    @abstractmethod
    def make_measurement(self):
        raise NotImplementedError
