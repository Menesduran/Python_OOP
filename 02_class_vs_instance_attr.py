"""
02_class_vs_instance_attr.py

Topic: class attribute vs instance attribute.
- Class attribute: defined in the class body, shared by all objects.
- Instance attribute: assigned on an object, belongs only to that object.
"""


class Sensor:
    unit = "°C"  # class attribute (paylaşılan varsayılan)
    tags = []    # DİKKAT: mutable class attribute -> tüm nesneler AYNI listeyi paylaşır


s1 = Sensor()
s2 = Sensor()

# 1) Atama = gölgeleme (shadowing)
s1.unit = "°F"           # s1'e özel instance attribute oluşturur
print(s1.unit)           # °F
print(s2.unit)           # °C
print(Sensor.unit)       # °C

# 2) Tuzak: paylaşılan liste
s1.tags.append("line-1")  # atama değil, mevcut class listesini DEĞİŞTİRİYOR
print(s2.tags)            # ['line-1']  -> s2'ye hiç dokunmadık!
print(s1.tags is s2.tags) # True        -> aynı liste nesnesi

# Çözüm: nesneye özel veriyi __init__ içinde self'e ata (bkz. 03_init_self.py)
