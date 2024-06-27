#arayüz konusunda internetten destek aldım



import tkinter as tk
from tkinter import messagebox

def ise_alim():
    adiniz = entry_adiniz.get()
    cinsiyet = entry_cinsiyet.get()
    bilgi = entry_bilgi.get()
    dil = entry_dil.get()
    yas = entry_yas.get()
    maas_beklentisi = entry_maas_beklentisi.get()

    try:
        yas = int(yas)
        maas_beklentisi = int(maas_beklentisi)
    except:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")
        return

    if yas >= 18 and yas <= 50 and "python" in bilgi.lower():
        maas = 20000

        if "," in bilgi:
            maas += 10000

        if maas_beklentisi >= 17000 and maas_beklentisi <= 30000 and maas >= maas_beklentisi:
            maas = maas_beklentisi

        is_karti_goster = messagebox.askquestion("İş Kartı", "İş kartınızı görmek istiyor musunuz?")
        if is_karti_goster == "yes":
            kart_bilgisi = (
                "Adınız: " + adiniz + "\n" +
                "Cinsiyetiniz: " + cinsiyet + "\n" +
                "Yaşınız: " + str(yas) + "\n" +
                "Bildiğiniz Yazılım Dilleri: " + bilgi + "\n" +
                "Bildiğiniz Diller: " + dil + "\n" +
                "İş Saatleri: 09:00 - 18:00\n" +
                "Maaş: " + str(maas) + " TL"
            )
            messagebox.showinfo("İş Kartı", kart_bilgisi)
        else:
            messagebox.showinfo("Bilgi", "İş kartı gösterilmeyecek.")
    else:
        messagebox.showerror("Hata", "Üzgünüz, işe alım kriterlerimize uymuyorsunuz.\n"
                                      "Yaşınız 18-50 arasında olmalı ve Python bilgisi gereklidir.")

root = tk.Tk()
root.title("Vanius Yazılım Şirketi İşe Alım")

tk.Label(root, text="Adınız:").grid(row=0)
tk.Label(root, text="Cinsiyetiniz:").grid(row=1)
tk.Label(root, text="Bildiğiniz Yazılım Dilleri:").grid(row=2)
tk.Label(root, text="Bildiğiniz Diller:").grid(row=3)
tk.Label(root, text="Yaşınız:").grid(row=4)
tk.Label(root, text="Maaş Beklentiniz (TL):").grid(row=5)

entry_adiniz = tk.Entry(root)
entry_cinsiyet = tk.Entry(root)
entry_bilgi = tk.Entry(root)
entry_dil = tk.Entry(root)
entry_yas = tk.Entry(root)
entry_maas_beklentisi = tk.Entry(root)

entry_adiniz.grid(row=0, column=1)
entry_cinsiyet.grid(row=1, column=1)
entry_bilgi.grid(row=2, column=1)
entry_dil.grid(row=3, column=1)
entry_yas.grid(row=4, column=1)
entry_maas_beklentisi.grid(row=5, column=1)

tk.Button(root, text="Başvur", command=ise_alim).grid(row=6, columnspan=2)

root.mainloop()

#vanius
