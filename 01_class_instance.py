"""
01_class_instance.py

Topic: what a class is, how to create an instance (object), dot notation.
- A class is a blueprint, an instance is an object built from it.
- Dot notation (obj.name) reaches an object's attributes and methods.
"""

# --- Dot notation: even a list is an object of the built-in list class ---
readings = []            # list sınıfından bir nesne
readings.append(21.5)    # nokta notasyonu: nesnenin method'unu çağırır
print(readings)          # [21.5]
print(type(readings))    # <class 'list'>


# --- Our own class ---
class Machine:
    # Class attributes: tüm nesneler için ortak varsayılan değerler
    category = "CNC"
    power_kw = None  # None'ı biz yazıyoruz; yazmasaydık attribute hiç var olmazdı


m1 = Machine()  # instance alma (nesne oluşturma)
m2 = Machine()

m1.power_kw = 7.5  # class'ı değil, SADECE m1'e ait yeni bir instance attribute oluşturur

print(m1.category)       # CNC   -> class attribute, herkes paylaşır
print(m1.power_kw)       # 7.5   -> m1'in kendi değeri
print(m2.power_kw)       # None  -> m2 hâlâ class attribute'u görüyor
print(Machine.power_kw)  # None  -> class attribute değişmedi

# Hata örneği: hiç tanımlanmamış bir attribute
# print(m1.color)  # AttributeError: 'Machine' object has no attribute 'color'
