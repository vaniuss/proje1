telefon_rehberi = {}

def kisi_ekle():
    ad = input("Kişinin adını girin: ")
    telefon = input("Kişinin telefon numarasını girin: ")
    telefon_rehberi[ad] = telefon
    print(f"{ad} kişisi listeye eklendi.")

def kisileri_listele():
    print("Rehberdeki kişiler:")
    for ad, telefon in telefon_rehberi.items():
        print(f"{ad}: {telefon}")

while True:
    seçim = input("Yeni kişi eklemek için 'yeni', kişileri listelemek için 'rehber' yazın: ")
    if seçim == "yeni":
        kisi_ekle()
    elif seçim == "rehber":
        kisileri_listele()
    else:
        print("Geçersiz seçenek! 'yeni' veya 'rehber' yazmalısınız.")

#vanius