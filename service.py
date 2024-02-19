from abc import ABC, abstractmethod


class Service(ABC):

    @abstractmethod
    def needs_service(self):
        pass