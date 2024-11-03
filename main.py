import random

maxfiy_son = random.randint(1, 10)
urinishlar = 0

print("Men 1 dan 10 gacha raqam o'yladim. Uni topishga harakat qiling!")

while True:
    foydalanuvchi_input = int(input("Raqamni kiriting: "))
    urinishlar += 1

    if foydalanuvchi_input < maxfiy_son:
        print("Noto'g'ri, kattaroq son kiritib ko'ring.")
    elif foydalanuvchi_input > maxfiy_son:
        print("Noto'g'ri, kichikroq son kiritib ko'ring.")
    else:
        print(f"Tabriklaymiz! Siz {urinishlar} urinishda topdingiz.")
        break

password = "something"

while True:
    foydalanuvchi_parol = input("Parolni kiriting: ")
    
    if foydalanuvchi_parol == password:
        print("Parol to'g'ri!")
        break
    else:
        print("Parol noto'g'ri, qayta urinib ko'ring.")
