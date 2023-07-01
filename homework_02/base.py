from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight=weight, fuel=fuel, fuel_consumption=fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self) -> None:
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance) -> None:
        way_range = self.fuel / self.fuel_consumption
        if way_range >= distance:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel
