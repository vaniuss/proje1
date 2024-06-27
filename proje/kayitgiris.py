kullanıcı_veri_tabanı = {}

def kayıt_ekranı():
    kullanıcı_adı = input("Kullanıcı adını giriniz: ")
    şifre = input("Şifrenizi giriniz: ")
    kullanıcı_veri_tabanı[kullanıcı_adı] = şifre  
    print("Kayıt olundu")
    
    
def giriş_ekranı():
    kullanıcı_adı2 = input("Kullanıcı adı: ")
    şifre2 = input("Şifrenizi giriniz: ")
    if kullanıcı_adı2 in kullanıcı_veri_tabanı and kullanıcı_veri_tabanı[kullanıcı_adı2] == şifre2:
        print("Giriş başarılı!")
    else:
        print("Kullanıcı adı veya şifre hatalı!")

while True:
    secim = input("Yeni kullanıcı eklemek için 'kayıt', giriş yapmak için 'giriş' yazın: ")
    if secim == "kayıt":
        kayıt_ekranı()
    elif secim == "giriş":
        giriş_ekranı()
    else:
        print("Geçersiz seçenek kayıt veya giriş yazmalısınız.")
        

#vanius
