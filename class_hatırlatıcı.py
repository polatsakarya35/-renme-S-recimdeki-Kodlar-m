import json
import hashlib
import os

class PasswordManager:
    def __init__(self, users_file="users.json", passwords_file="passwords.json"):
        """
        Sınıf başlatıcı (constructor) metodu.
        - Dosya adlarını (`users_file`, `passwords_file`) alır veya varsayılan dosya adlarını kullanır.
        - Kullanıcı ve şifre bilgilerini tutacak sözlükleri (`users`, `passwords`) başlatır.
        - `load_data` metodunu çağırarak dosyadan mevcut verileri yükler.
        """
        self.users_file = users_file  # Kullanıcı adlarını tutacak dosya adı
        self.passwords_file = passwords_file  # Şifreleri tutacak dosya adı
        self.users = {}  # Kullanıcı isimlerini saklayacak sözlük
        self.passwords = {}  # Şifreleri saklayacak sözlük
        self.load_data()  # Dosyalardan kullanıcı ve şifre verilerini yükle

    def load_data(self):
        """
        Kullanıcı ve şifre verilerini dosyalardan yükler.
        - Eğer dosyalar mevcutsa, veriler JSON formatında okunur ve sınıfın `users` ve `passwords` değişkenlerine atanır.
        """
        if os.path.exists(self.users_file):  # Kullanıcı dosyası varsa
            with open(self.users_file, "r") as f:  # Dosyayı okuma modunda aç
                self.users = json.load(f)  # JSON verisini `self.users` içine yükle
        if os.path.exists(self.passwords_file):  # Şifre dosyası varsa
            with open(self.passwords_file, "r") as f:  # Dosyayı okuma modunda aç
                self.passwords = json.load(f)  # JSON verisini `self.passwords` içine yükle

    def save_data(self):
        """
        Kullanıcı ve şifre verilerini dosyalara kaydeder.
        - Kullanıcılar `users_file` dosyasına, şifreler ise `passwords_file` dosyasına JSON formatında yazılır.
        """
        with open(self.users_file, "w") as f:  # Kullanıcı dosyasını yazma modunda aç
            json.dump(self.users, f)  # Kullanıcı verilerini JSON olarak kaydet
        with open(self.passwords_file, "w") as f:  # Şifre dosyasını yazma modunda aç
            json.dump(self.passwords, f)  # Şifre verilerini JSON olarak kaydet

    def hash_password(self, password):
        """
        Şifreyi SHA-256 algoritması ile hash'ler.
        - Hashing, şifrelerin güvenli bir şekilde saklanmasını sağlar.
        - Orijinal şifreyi kurtarmak mümkün değildir, ancak aynı şifre tekrar hash'lendiğinde aynı sonuç üretilir.
        """
        return hashlib.sha256(password.encode()).hexdigest()  # SHA-256 ile hash'ler

    def add_user(self, username, password):
        """
        Yeni bir kullanıcı ekler.
        - Eğer kullanıcı zaten mevcutsa, bir uyarı verir.
        - Kullanıcı adı ve şifreyi alır, şifreyi hash'ler ve kaydeder.
        - Kullanıcılar ve şifreler dosyaya kaydedilir.
        """
        if username in self.users:  # Kullanıcı zaten varsa
            print("Bu kullanıcı zaten mevcut.")
        else:
            self.users[username] = username  # Kullanıcı adı eklenir
            self.passwords[username] = self.hash_password(password)  # Şifre hash'lenip eklenir
            self.save_data()  # Güncel veriler dosyaya kaydedilir
            print(f"{username} kullanıcısı eklendi.")

    def check_user(self, username, password):
        """
        Kullanıcı adı ve şifre doğrulaması yapar.
        - Kullanıcı adı ve şifre doğruysa, giriş başarılı mesajı verir.
        - Yanlış şifre veya bulunamayan kullanıcı için hata mesajı gösterir.
        """
        if username in self.users:  # Kullanıcı adı kontrol edilir
            hashed_password = self.passwords[username]  # Kullanıcıya ait hash'lenmiş şifre alınır
            if hashed_password == self.hash_password(password):  # Şifre hash'i doğrulanır
                print(f"Giriş başarılı! Hoş geldiniz, {username}.")
            else:
                print("Yanlış şifre!")
        else:
            print("Kullanıcı bulunamadı!")

    def delete_user(self, username):
        """
        Kullanıcıyı sistemden siler.
        - Kullanıcı adı listeden çıkarılır, şifresi de silinir.
        - Kullanıcı bulunamazsa, hata mesajı gösterir.
        """
        if username in self.users:  # Kullanıcı var mı kontrol edilir
            del self.users[username]  # Kullanıcı adı listeden silinir
            del self.passwords[username]  # Şifre listeden silinir
            self.save_data()  # Güncel veriler dosyaya kaydedilir
            print(f"{username} kullanıcısı silindi.")
        else:
            print("Kullanıcı bulunamadı.")

# Kullanıcı işlemleri
pm = PasswordManager()

# Kullanıcı ekleme
pm.add_user("ahmet", "1234")  # Yeni kullanıcı ekler

# Kullanıcı kontrolü
pm.check_user("ahmet", "1234")  # Giriş kontrolü

# Kullanıcı silme
pm.delete_user("ahmet")  # Kullanıcıyı siler

"""
Modül	   İşlev	                                         Kullanıldığı Yer
json	   JSON formatında veri okuma ve yazma	             Kullanıcı ve şifre verilerini JSON formatında dosyadan okuma (json.load) ve dosyaya yazma (json.dump).
hashlib	   Şifre hash'leme	                                 Şifreleri SHA-256 algoritması ile hash'lemek için kullanıldı.
os	       Dosya kontrolü	                                 Dosyanın mevcut olup olmadığını kontrol etmek için os.path.exists kullanıldı.

"""

