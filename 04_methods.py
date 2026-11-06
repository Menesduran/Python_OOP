"""
04_methods.py

Topic: methods: function defined inside a class.
- A method works on its own object through self.
- a method can return a value, or change the object's statue (attributes). 
"""

class Machine:
    def __init__(self,name: str, power_kw: float):
        self.name = name
        self.power_kw = power_kw
        self.total_hours = 0  # her makinenin kendi sayacı (instance attribute)


    def run(self,hours: float):
        # Durumu değiştiren method: bir şey döndürmez, nesnenin verisini günceller
        self.total_hours += hours

    def energy_kwh(self):
        # Değer döndüren method: nesnenin verisinden hesap yapar
        return self.power_kw * self.total_hours


m1 = Machine(name = "Lathe", power_kw = 7.5)
m2 = Machine(name = "Mill", power_kw = 5.0)

m1.run(2)
m1.run(3)
print(m1.total_hours)   # 5    -> sadece m1'in sayacı çalıştı
print(m1.energy_kwh())  # 37.5 -> 7.5 * 5
print(m2.energy_kwh())  # 0.0  -> m2 hiç çalışmadı

# m1.run(1) aslında şunun kısayoludur: Machine.run(m1, 1)
# Python, noktanın solundaki nesneyi (m1) otomatik olarak self yapar.
Machine.run(m1, 1)
print(m1.total_hours) 

# Hata örnekleri:
# m1.run()  # TypeError: run() missing 1 required positional argument: 'hours'
# def run(hours): ...  (self yazmayı unutmak)
#   -> m1.run(2)  # TypeError: run() takes 1 positional argument but 2 were given

