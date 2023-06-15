
#BSM 1.SINIF BAHAR DÖNEMİ ALGORİTMA VE PROGLAMA PROJESİ#
#Deprem sonrası enkaz altında kalma durumuna karşı kullanılacak program. #
#İlk olarak program karşınıza enkaz altında kalma durumunda yapılacakları sesli ve yazılı biçimde hatırlatıyor. #
#Sonrasında belirli zaman aralıklarında bayılma durumuna karşı program kendisi alarm çalıyor. #
#Bu aynı zamanda dışardaki insanların sizi duymasını da sağlar. Program çalıştığı sürece geçen zaman ilerledikçe alarmları sıklaştırır.#
 #Program açıldığı andan itibaren çalışmaya devam eder.#













import time
from playsound import playsound
import sqlite3


conn = sqlite3.connect('hatirlatmalar.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS hatirlatmalar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hatirlatma_metni TEXT
    )
''')
conn.commit()

def hatirlatma():
    cursor.execute('SELECT hatirlatma_metni FROM hatirlatmalar')
    hatirlatmalar = cursor.fetchall()
    
    for hatirlatma in hatirlatmalar:
        print(hatirlatma[0])
        time.sleep(2)

def alarmcal():
    print("Alarm! Sizi duyabilmeleri için dışarıdaki insanlara seslenin.")
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


conn.close()
