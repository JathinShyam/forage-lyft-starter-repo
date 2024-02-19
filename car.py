from abc import ABC, abstractmethod
from service import Service

class Car(Service, ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        
    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
