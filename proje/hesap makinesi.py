birincisayı = int(input("İlk sayıyı giriniz: "))
ikincisayı = int(input("İkinci sayıyı giriniz: "))

üçüncüsayı = input("Bir sayı daha girmek ister misiniz? (Evet için 'y', hayır için 'n'): ")

if üçüncüsayı == "y":
    üçüncüsayı = int(input("Üçüncü sayıyı giriniz: "))
    
islem = input("""Toplama: +
              Çıkartma: -
              Çarpma: * 
              Bölme: / 
              Yapmak istediğiniz işlemi giriniz:""")

if islem == "+": 
    print("Sonuç: " + str(birincisayı + ikincisayı))
    
elif islem == "-": 
    print("Sonuç: " + str(birincisayı - ikincisayı))

elif islem == "*": 
    print("Sonuç: " + str(birincisayı * ikincisayı))

elif islem == "/": 
    print("Sonuç: " + str(birincisayı / ikincisayı))

#vanius