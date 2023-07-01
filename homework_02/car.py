"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.engine import Engine
from homework_02.base import Vehicle


class Car(Vehicle):
    engine: Engine

    def set_engine(self, engine):
        self.engine = engine
