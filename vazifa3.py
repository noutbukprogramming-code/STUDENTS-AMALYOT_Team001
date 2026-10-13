id_talaba = int(input("Talaba ID sini kiriting: "))

topildi = False

with open("talaba.txt", "r", encoding="utf-8") as file:
    for qator in file:
        malumot = qator.strip().split(",")

        if int(malumot[0]) == id_talaba:
            print("Talaba topildi!")
            print("ID:", malumot[0])
            print("Ismi:", malumot[1])
            print("Yoshi:", malumot[2])
            topildi = True
            break

if not topildi:
    print("Talaba topilmadi!")