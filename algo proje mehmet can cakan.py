
#BSM 1.SINIF BAHAR DÖNEMİ ALGORİTMA VE PROGLAMA PROJESİ#
#Deprem sonrası enkaz altında kalma durumuna karşı kullanılacak program. #
#İlk olarak program karşınıza enkaz altında kalma durumunda yapılacakları sesli ve yazılı biçimde hatırlatıyor. #
#Sonrasında belirli zaman aralıklarında bayılma durumuna karşı program kendisi alarm çalıyor. #
#Bu aynı zamanda dışardaki insanların sizi duymasını da sağlar. Program çalıştığı sürece geçen zaman ilerledikçe alarmları sıklaştırır.#
 #Program açıldığı andan itibaren çalışmaya devam eder.#













import time
from playsound import playsound

def hatirlatma():
    hatirlatmalar = [
        "1. Sakin kalmaya çalışın: Panik yapmak yerine sakin kalmaya çalışın.",
        "2. Yardım çağırın: Enkaz altında olduğunuzda, mümkün olan en kısa sürede yardım çağırmanız önemlidir.",
        "3. Yaralıysanız dikkatlice hareket edin: Eğer yaralanmışsanız, kendinizi daha fazla yaralamamak için dikkatlice hareket etmelisiniz.",
        "4. Nefes alabilmeniz için boşluklar arayın: Enkaz altında nefes alabilmek için hava boşlukları arayın.",
        "5. Sinyal verin: Sinyal verebileceğiniz herhangi bir nesneyi kullanarak yardım çağırın.",
        "6. Mümkün olduğunca yer değiştirin: Enkaz altında olduğunuzda, hareket etmek için uygun bir alan arayın.",
        "7. Yardım gelene kadar bekleyin: Yardım ekipleri enkaz altındaki insanları kurtarmak için çalışırken, bekleyin ve umutsuzluğa kapılmayın."
    ]
    
    for hatirlatma in hatirlatmalar:
        print(hatirlatma)
        time.sleep(2)  
    
def alarmcal():
    print("Alarm! Sizi duyabilmeleri için dışardaki insanlara seslenin.")
    playsound("alarm.mp3") 
    
def program():
    zamanaraligi = 60  
    zamangecikmesi = 10  
    
    while True:
        hatirlatma()
        alarmcal()
        
        time.sleep(zamanaraligi)
        
        zamanaraligi -= zamangecikmesi
        if zamanaraligi <= 0:
            zamanaraligi = 1  

program()
