from boek_transacties import *
from leden_transacties import *
from tijd import *

def hoofd_menu():
    while True:
        print("\n=== KÜTÜPHANE SİSTEMİ ===")
        print("1. Üyelik işlemleri")
        print("2. Kitap işlemleri")
        print("3. Çıkış")
        sec = input("Seçiminiz: ")
        if sec == "1":
            leden_menu()
        elif sec == "2":
            boeken_menu()
        elif sec == "3":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim.")

def leden_menu():
    while True:
        print("\n--- ÜYELİK İŞLEMLERİ ---")
        print("1. Tüm üyeleri listele")
        print("2. Üye ekle")
        print("3. Üye ara")
        print("4. Üye sil")
        print("5. Üyeye kitap ödünç ver")
        print("6. İade edilen kitabı al")
        print("7. Bir üyenin aldığı kitapları listele")
        print("8. Geri (ana menü)")
        sec = input("Seçiminiz: ")
        if sec == "1":
            uyeleri_listele()
        elif sec == "2":
            uye_ekle()
        elif sec == "3":
            uye_ara()
        elif sec == "4":
            uye_sil()
        elif sec == "5":
            kitap_odunc_ver()
        elif sec == "6":
            kitap_iade_al()
        elif sec == "7":
            uye_aldiklarini_listele()
        elif sec == "8":
            break
        else:
            print("Geçersiz seçim.")

def boeken_menu():
    while True:
        print("\n--- KİTAP İŞLEMLERİ ---")
        print("1. Tüm kitapları listele")
        print("2. Kitap ekle")
        print("3. Kitap güncelle")
        print("4. Kitap ara (kısmi eşleşme destekli)")
        print("5. Kitap sil")
        print("6. Geri (ana menü)")
        sec = input("Seçiminiz: ")
        if sec == "1":
            boek_lijst()
        elif sec == "2":
            boek_toevoegen()
        elif sec == "3":
            boek_bijwerken()
        elif sec == "4":
            boek_zoeken()
        elif sec == "5":
            boek_verwijderen()
        elif sec == "6":
            break
        else:
            print("Geçersiz seçim.")



if __name__ == "__main__":
    hoofd_menu()