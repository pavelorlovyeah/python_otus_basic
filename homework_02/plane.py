"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0

    def __init__(
            self, weight, fuel,
            fuel_consumption, max_cargo=0
    ):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo: int) -> None:
        sum_cargo = self.cargo + add_cargo
        if sum_cargo <= self.max_cargo:
            self.cargo = sum_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self) -> int:
        cargo_init = self.cargo
        self.cargo = 0
        return cargo_init
