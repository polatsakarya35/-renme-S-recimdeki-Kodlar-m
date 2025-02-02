import matplotlib.pyplot as plt
import time

para = {}
hedef = {}

def para_yatırma_yada_alma():
    while True:
        seçim = input("\nSeçim yapınız:\n1. Para eklemek için '1'\n2. Para çıkarmak için '2'\nÇıkmak için 'q'\nSeçiminiz: ")
        
        if seçim == 'q':
            break
        elif seçim == '1':  # Para ekleme
            miktar = int(input("Eklemek istediğiniz miktar nedir? "))
            nedeni = input("Neden eklediniz? ")
            süre = input("Ne zaman eklediniz? ")
            
            # Para ekle
            para[miktar] = {"nedeni": nedeni, "süre": süre}
            print(f"\n{miktar} TL başarıyla eklendi!")
            time.sleep(2)

        elif seçim == '2':  # Para çıkarma
            miktar = int(input("Çıkarmak istediğiniz miktar nedir? "))
            if miktar > 0:
                nedeni = input("Neden aldınız? ")
                süre = input("Ne zaman aldınız? ")
                
                # Para çıkar
                para[-miktar] = {"nedeni": nedeni, "süre": süre}
                print(f"\n{miktar} TL başarıyla çıkarıldı!")
                time.sleep(2)

        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")
    
    print("\nParanı tutumlu kullanmayı unutma!")
    print("Mevcut para işlemleri:", para)


def para_biriktirme_hedefi():
    while True:
        karar = input("\nBiriktirme hedefinizi girin ('q' ile çıkabilirsiniz): ")
        if karar == 'q':
            break
        
        miktar1 = int(input("Biriktirmek istediğiniz miktar nedir? "))
        hedef[karar] = miktar1  # Hedefi ekle
        print(f"\nHedef kaydedildi: {karar} için {miktar1} TL")
    
    print("\nMevcut biriktirme hedefleri:", hedef)


def main():
    while True:
        print("\n=== Finans Yönetim Uygulaması ===")
        print("1. Para ile ilgili işlemler")
        print("2. Para biriktirme hedefi ekle")
        print("3. Çıkış")
        
        secim = input("Seçiminizi yapın (1-3): ")

        if secim == "1":
            para_yatırma_yada_alma()
        elif secim == "2":
            para_biriktirme_hedefi()
        elif secim == "3":
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Programı başlat
main()
