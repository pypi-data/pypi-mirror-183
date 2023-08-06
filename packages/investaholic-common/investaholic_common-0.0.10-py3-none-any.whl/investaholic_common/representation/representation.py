from abc import ABC, abstractmethod


class Representation(ABC):
    def __init__(self, obj_repr=None):
        pass

    @abstractmethod
    def as_dict(self) -> dict:
        pass
