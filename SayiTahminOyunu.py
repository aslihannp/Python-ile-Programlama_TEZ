import random

#Tanımlanan fonksiyon
def sayiTahmin(parametre1):
    while True:
        global sayac
        sayac+=1
        puan=100
        if parametre1==TutulanSayi:
            print("Tebrikler!",sayac,". denemede doğru bildiniz.")
            print("Puanınız:",puan-(sayac*10))
            break
        elif(parametre1<TutulanSayi):
            print("Üzgünüm yanlış oldu. Daha büyük bir sayı dene!")
            parametre1=int(input("Yeni sayi:"))   
        else:
            print("Üzgünüm yanlış oldu. Daha küçük bir sayı dene!")
            parametre1=int(input("Yeni sayi:"))
 
#Ana program    
TutulanSayi=random.randint(1,50)
sayac=0
print("***Sayi tahmin etme oyununa hoş geldiniz***")
print("1 ile 50 arasında bir sayı tuttuk, bu sayıyı tahmin etmek ister misiniz?")
n=int(input("İlk tahmininizi girin:"))
sayiTahmin(n)
