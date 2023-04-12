girisyap=1
uyeol=2
sifremiunuttum=3

while True:

  islem = input("Hosgeldiniz. Yapmak istediginiz islem icin belirlenen tuslardan birine basiniz.\n 1-Giris Yap \n 2-Uye ol \n 3-Sifremi unuttum.\n")



  if(islem == "1"):

    kullaniciadi=input("kullanici adi girin.\n")

    sifre=input("sifre girin\n")

    print("bilgiler dogrulaniyor...")
   
    break

  
  if(islem == "2"):

    kullaniciadi=input("kullanici adi belirleyiniz.\n")

    sifre=input("sifre belirleyin \n")
    
    eposta=input("e postanizi girin \n")

    print("hesabiniz basari ile olusturuldu. \n")

    break



  if(islem == "3"):

    kurtarmaislem1=input("kullanici adinizi giriniz.\n")

    kurtarmaislem2=input("hesabiniza ait olan e postaniza gonderdigimiz kodu giriniz.\n")
      
  break 
 
else:
 print("Hatali tuslama yaptiniz.Tekrar deneyiniz.")



   
