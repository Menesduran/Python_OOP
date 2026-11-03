"""
sensor.py

Exercise: complete the Sensor class.
Steps: 1) add_reading  2) average  3) (later) __str__
"""


class Sensor:
    def __init__(self, name: str, unit: str):
        self.name = name
        self.unit = unit
        self.readings = []

    def add_reading(self, value: float):
        # TODO: append value to self.readings
        pass

    def average(self):
        # TODO: return the average of self.readings (None if there are no readings)
        pass


if __name__ == "__main__":
    t = Sensor("T1", "°C")
    t.add_reading(20.0)
    t.add_reading(22.0)
    print(t.average())  # expected: 21.0

    empty = Sensor("T2", "°C")
    print(empty.average())  # expected: None
