# 01_class_instance.py
# Konu: Class, instance (nesne) ve class attribute / instance attribute farkı


class Vehicle:
    # Class attribute: bu class'tan üretilen TÜM nesneler arasında paylaşılır
    door_number = 4
    brand = None  # None'ı ben atıyorum, Python otomatik atamıyor


car1 = Vehicle()  # instance alma (nesne oluşturma)
car2 = Vehicle()

# Bu satır class'ı değil, SADECE car1'e ait yeni bir instance attribute oluşturur
car1.brand = "Dodge"

print(car1.brand)        # Dodge  -> car1'in kendi değeri
print(car2.brand)        # None   -> class attribute'tan geliyor
print(Vehicle.brand)     # None   -> class attribute değişmedi
print(car2.door_number)  # 4      -> herkes paylaşır