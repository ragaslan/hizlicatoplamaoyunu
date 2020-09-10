import time
import random
from datetime import datetime
start = datetime.now()
def toplama(sayi1,sayi2):
    sonuc = sayi1 + sayi2
    return sonuc
def oyundancik():
    print("Oyundan Çıkıılıyor!!")
    time.sleep(1)
    exit()
def oyunbaslat():
    i = 0

    while True:
        rasgele1 = random.randrange(0, 100)
        rasgele2 = random.randrange(0, 100)
        soru = str(rasgele1) + "+" + str(rasgele2) + " kaç yapar ?"
        print(soru)

        oyunsonuc = toplama(rasgele1, rasgele2)
        cevap = int(input("işlemi Yap: "))

        if (cevap == oyunsonuc):
            print("dogru erkeksen bir soru daha bil")
            i += 1
        else:
            gecenzaman = str(datetime.now() - start)
            print("Kaybettinn ibne")
            print("Toplamda  " + str(i) + " tane soru bildin")
            print("Süren " + gecenzaman)

            print("Oyun Bitti hadi evine..!")
            while True:
                cevap = input("Yoksa tekrar mı oynamak istiyorsun :)  E/H")
                if cevap == "E":
                    oyunbaslat()
                elif cevap == "H":
                    oyundancik()
                else:
                    print("Hatalı Cevap")
            break

            time.sleep(2)
            break
        if i == 2:
            gecenzaman = str(datetime.now() - start)
            print("ama 2 soruyu bilerek oyunu tamamladın!")
            print("Süren " + gecenzaman)


            while True:
                cevap = input("Tekrar Oynamak İster Misin? E/H")
                if cevap == "E":
                    oyunbaslat()
                elif cevap == "H":
                    oyundancik()
                else:
                    print("Hatalı Cevap")
                    break



            break

oyunbaslat()

