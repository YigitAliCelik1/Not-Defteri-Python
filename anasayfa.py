komut = input("""
Girebileceğiniz Komutlar:
1- Eğer yeni bir not sayfası açmak istiyorsanız "yeni" yazın !!!Küçük Harflerle!!!
2- Eğer eski bir not sayfası açmak istiyorsanız dosyanın adını yazın !!!Küçük Harflerle!!!
""")

try:
    assert komut==("yeni")
    def rastgele_dosya_olustur():
        import random
        import string
        
        harfler = string.ascii_lowercase
        rastgele_isim = ''.join(random.choice(harfler) for _ in range(5))
        dosya_adi = (f"{rastgele_isim}.txt")
        dosya=open(rastgele_isim,mode="w")
        print(f"Rastgele dosya oluşturuldu: {dosya_adi}")
        yazılacaklar=input("""
        Ne yazmak istersiniz""")
        dosya.write(yazılacaklar)
        dosya.close()
    rastgele_dosya_olustur()
except:
    try:
        assert komut!=("yeni")
        try:
            dosya_adi = f"{komut}.txt"
            dosya=open(dosya_adi,mode="a")
            print(f"Dosya Açıldı: {dosya_adi}")
            yazılacaklar=input("""
            Ne yazmak istersiniz""")
            dosya.write(yazılacaklar)
            dosya.close()
        except:
           print("Nedeni Bilinmeyen bir sorun oluştu")
    except:
        print("Böyle bir dosya yok")
        