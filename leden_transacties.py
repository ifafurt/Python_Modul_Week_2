import json
import os
#from tijd import datum_en_terug
#from boek_transacties import boeken_laden, boeken_opslaan
from datetime import datetime,timedelta

LEDEN_BESTAND = "leden.json"
UITLEEN_BESTAND = "uitleeningen.json"
BOEKEN_BESTAND= "boeken.json"

def dosyadan_uyeleri_oku():
    if not os.path.exists(LEDEN_BESTAND):
        return []
    with open("leden.json", "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.decoder.JSONDecodeError:
            return []

def dosyaya_uyeleri_yaz(uyeler):
    with open("leden.json", "w", encoding="utf-8") as f:
        json.dump(uyeler, f, ensure_ascii=False, indent=4)

def uyeleri_listele():
    print("Tüm üyeler listeleniyor...")
    uyeler = dosyadan_uyeleri_oku()
    for uye in uyeler:
        print(f"ID: {uye['id']}, Adı: {uye['ad']}")


def uye_ekle():
    print("Yeni üye ekleme işlemi...")
    uyeler = dosyadan_uyeleri_oku()
    ad = input("Yeni üyenin adını giriniz: ")
    yeni_id = max(int(uye["id"]) for uye in uyeler) + 1  # otomatik ID oluşturur
    uyeler.append({"id": yeni_id, "ad": ad})
    dosyaya_uyeleri_yaz(uyeler)
    print(f"{ad} adlı üye eklendi.")

def uye_ara():
    print("Üye arama işlemi...")
    uyeler = dosyadan_uyeleri_oku()
    ad = input("Aramak istediğiniz üyenin adını girin: ")
    bulunan = [uye for uye in uyeler if ad.lower() in uye["ad"].lower()]
    if bulunan:
        for uye in bulunan:
            print(f"ID: {uye['id']}, Adi: {uye['ad']}")
    else:
        print("Üye bulunamadı.")

def uye_sil():
    print("Üye silme işlemi...")
    uyeler = dosyadan_uyeleri_oku()
    silinecek_id = input("Silmek istediğiniz üyenin ID numarasını girin: ")

    yeni_liste = [uye for uye in uyeler if str(uye["id"]) != silinecek_id]

    if len(yeni_liste) == len(uyeler):
        print("Belirtilen ID'ye sahip üye bulunamadı.")
    else:
        dosyaya_uyeleri_yaz(yeni_liste)
        print(f"ID {silinecek_id} olan üye silindi.")


def kitap_odunc_ver():
    with open(LEDEN_BESTAND, "r", encoding="utf-8") as f:
        uyeler = json.load(f)
    try:
        with open(UITLEEN_BESTAND, "r", encoding="utf-8") as f:
            uitleeningen = json.load(f)
    except FileNotFoundError:
        uitleeningen = []
    with open(BOEKEN_BESTAND, "r", encoding="utf-8") as f:
        kitaplar = json.load(f)

    uye_id = input("Üye ID'sini girin: ").strip()
    barkod = input("Kitap barkodunu girin: ").strip()

    uye = next((u for u in uyeler if str(u["id"]) == uye_id), None)
    kitap = next((k for k in kitaplar if str(k.get("barkod")) == barkod), None)

    if not uye:
        print("Üye bulunamadı.")
        return
    if not kitap:
        print("Kitap bulunamadı.")
        return

    alis = datetime.now()
    iade = alis + timedelta(days=14)

    yeni = {
        "uye_id": str(uye["id"]),
        "uye": uye["ad"],
        "kitap": kitap,
        "alis_tarihi": alis.strftime("%Y-%m-%d %H:%M:%S"),
        "iade_tarihi": iade.strftime("%Y-%m-%d %H:%M:%S")
    }
    uitleeningen.append(yeni)

    # Dosyaları kaydet (her durumda)
    with open(UITLEEN_BESTAND, "w", encoding="utf-8") as f:
        json.dump(uitleeningen, f, ensure_ascii=False, indent=4)

    print(f"{uye['ad']} adlı üyeye '{kitap['baslik']}' ödünç verildi; iade: {iade.strftime('%d.%m.%Y')}")



def kitap_iade_al():
    try:
        with open(UITLEEN_BESTAND, "r", encoding="utf-8") as f:
            uitleeningen = json.load(f)
    except FileNotFoundError:
        print("Henüz ödünç verilen kitap yok.")
        return

    uye_id = input("Üye ID'sini girin: ").strip()
    barkod = input("İade edilen kitabın barkodunu girin: ").strip()

    # kaydı bul
    for kayit in uitleeningen:
        if str(kayit["uye_id"]) == uye_id and str(kayit["kitap"].get("barkod")) == barkod:
            uitleeningen.remove(kayit)
            print(f"{kayit['uye']} adlı üye '{kayit['kitap']['baslik']}' kitabını iade etti.")
            break
    else:
        print("Kayit bulunamadı.")

    with open(UITLEEN_BESTAND, "w", encoding="utf-8") as f:
        json.dump(uitleeningen, f, ensure_ascii=False, indent=4)


def uye_aldiklarini_listele():
    with open(LEDEN_BESTAND, "r", encoding="utf-8") as f:
        uyeler = json.load(f)
    try:
        with open(UITLEEN_BESTAND, "r", encoding="utf-8") as f:
            uitleeningen = json.load(f)
    except FileNotFoundError:
        print("Henüz ödünç kayıt yok.")
        return

    uye_id = input("Üye ID'sini girin: ").strip()
    uye = next((u for u in uyeler if str(u["id"]) == uye_id), None)
    if not uye:
        print("Üye bulunamadı.")
        return

    kayitlar = [k for k in uitleeningen if str(k["uye_id"]) == uye_id]
    if not kayitlar:
        print("Bu üyenin aldığı kitap yok.")
        return

    print(f"{uye.get('ad','(isim yok)')} adlı üyenin aldığı kitaplar:")
    for k in kayitlar:
        kitap = k['kitap']
        print(f"- {kitap['baslik']} (Alış: {k['alis_tarihi']}, İade: {k['iade_tarihi']})")

