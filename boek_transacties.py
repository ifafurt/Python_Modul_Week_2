import json
import os

BOEKEN_BESTAND = "boeken.json"
UITLEEN_BESTAND = "uitleeningen.json"
#-------------------------------------------------------

def lees_boeken():
    if not os.path.exists(BOEKEN_BESTAND):
        return[]
    with open(BOEKEN_BESTAND, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return[]
#-----------------------------------------------------------------

def schrijf_boeken(boeken):
    with open(BOEKEN_BESTAND, "w",encoding="utf-8") as file:
        json.dump(boeken, file, ensure_ascii=False, indent=4)
#---------------------------------------------------------------------

# def boek_lijst():
#     boeken = lees_boeken()
#     if not boeken:
#         print("henuz hic kitap eklenmemis ")
#         return

#     boeken_sorted= sorted(boeken,key=lambda b: b["baslik"].lower())
#     print("\n==== KITAP LISTESI ====")
#     for boek in boeken_sorted:
#         print(f"Barkod: {boek['barkod']} | Adi:{boek['baslik']} |"
#               f"Yil: {boek['yil']} | Yazar: {boek['yazar']}")
        
def boek_lijst():
    boeken = lees_boeken()  # ← düzeltildi
    if not boeken:
        print("Henüz hiç kitap eklenmemiş.")
        return

    boeken_sorted = sorted(boeken, key=lambda b: b["baslik"].lower())
    print("\n==== KİTAP LİSTESİ ====")
    for boek in boeken_sorted:
        print(f"barkod: {boek['barkod']} | Adı: {boek['baslik']} | "
              f"Yıl: {boek['yil']} | Yazar: {boek['yazar']}")

#--------------------------------------------------------------------------------

# def boek_toevoegen():
#     boeken = lees_boeken()
#     barkod= input("Barkod numarasi: ").strip()


#     for boek in boeken:
#         if str(boek["Barkod"])== barkod:
#             print("bu barkod zaten kayitli!")
#             return

#     baslik= input("Kitap adi: ").strip()
#     yil= input("Yil: ").strip()
#     yazar = input("Yazar: ").strip()

#     nieuw_boek={
#         "Barkod": barkod,
#         "Kitap_Adi": baslik,
#         "yil": yil,
#         "Yazar": yazar,
#         "tur" : tur
#     }

#     boeken.append(nieuw_boek)
#     schrijf_boeken(boeken)
#     print(" Yeni kitap basariyle eklendi! ")

def boek_toevoegen():
    boeken = lees_boeken()
    barkod = input("Barkod numarası: ").strip()

    for boek in boeken:
        if str(boek["barkod"]) == barkod:
            print("Bu barkod zaten kayıtlı!")
            return

    baslik = input("Kitap adı: ").strip()
    yil = input("Yıl: ").strip()
    yazar = input("Yazar: ").strip()
    tur = input("Tür: ").strip()

    nieuw_boek = {
        "barkod": barkod,
        "baslik": baslik,
        "yil": yil,
        "yazar": yazar,
        "tur": tur
    }

    boeken.append(nieuw_boek)
    schrijf_boeken(boeken)
    print("Yeni kitap başarıyla eklendi!")

#---------------------------------------------------------------------------------------------------

def boek_bijwerken():
    boeken=lees_boeken()
    barkod = input("Guncellenecek kitabin barkodu: ").strip()

    for boek in boeken:
        if str(boek["barkod"]) == barkod:
            print(f"Mevcut bilgiler: {boek}")
            boek["baslik"] = input("Yeni kitap adi(bos birakmak icin enter):") or boek["baslik"]
            boek["yil"] = input("yil ( bos birakmak icin enter):") or boek["yil"]
            boek["yazar"] = input("Yeni yazar ( bos birakmak icin enter):") or boek["yazar"]
            schrijf_boeken(boeken)
            print("Kitap basariyla guncellendi!")
            return
    print ("Bu barkoda sahip kitap bulunamadi")
#----------------------------------------------------------------------------------------------------------

def boek_zoeken():
    boeken = lees_boeken()
    if not boeken:
        print("Henuz kitap eklenmemis ")
        return
    keyword= input("Aranacak kitap adi veya yazari: ").lower().strip()
    resultaten= [
        boek for boek in boeken
        if keyword in boek["baslik"].lower() or keyword in boek["yazar"].lower()
    ]

    if not resultaten:
        print(" Hicbir sonuc bulunamadi.")
        return
    print("\n=== ARAMA SONUCLARI ====")
    for boek in resultaten:
        print(f"{ boek['baslik']} - {boek['yazar']} - ({boek['yil']})")
    print(f"=== {len(resultaten)} kitap bulundu.====")
#------------------------------------------------------------------------------------------------------------
def boek_verwijderen():
    boeken= lees_boeken()
    barkod= input(" Silmek istediginiz kitabin barkodu: ").strip()
    nieuwe_lijst= [b for b in boeken if str(b["barkod"]) != barkod]

    if len(boeken) == len(nieuwe_lijst):
        print(" Bu barkoda sahip kitap bulunamadi.")
    else:
        schrijf_boeken(nieuwe_lijst)
        print(" Kitap basariyla silindi! ")
#-------------------------------------------------------------------------------------------------------------



