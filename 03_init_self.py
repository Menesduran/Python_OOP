"""
03_init_self.py

Topic: __init__ and self.
- __init__ runs automatically when an object is created (initializer).
- self is the object being created/used; it is a convention, not a keyword.
"""


class Sensor:
    """A sensor with a name, a unit and its own list of readings."""

    def __init__(self, name: str, unit: str):
        self.name = name        # instance attribute
        self.unit = unit        # instance attribute
        self.readings = []      # her sensörün KENDİ listesi (02'deki tuzak çözüldü)


temp = Sensor("T1", "°C")       # __init__'i biz çağırmadık, otomatik çalıştı
pressure = Sensor("P1", "bar")

temp.readings.append(21.5)

print(temp.name, temp.unit, temp.readings)   # T1 °C [21.5]
print(pressure.readings)                     # []
print(temp.readings is pressure.readings)    # False -> ayrı listeler

# Sensor("T1", "°C") çağrılırken self = az önce yaratılan nesne (yani temp).
# Eksik argüman hatası: Sensor("T1")  # TypeError: missing 1 required positional argument
