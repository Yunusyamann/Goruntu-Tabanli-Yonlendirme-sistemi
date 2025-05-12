
# VisionDrive: Görüntü Tabanlı Yönlendirme Sistemi 🚗📷

Python, OpenCV ve Arduino kullanılarak geliştirilen bu proje, kamera üzerinden yeşil renkli nesneleri tespit edip konumlarına göre Arduino’ya yön komutları göndererek robotik bir sistemi yönlendirmeyi amaçlar.

---

## 🔧 Özellikler

- Gerçek zamanlı kamera analizi
- HSV renk uzayında yeşil nesne tespiti
- Nesnenin konumuna göre "F", "L", "R" komutları
- Arduino ile seri haberleşme
- Görsel olarak geliştirilmiş ve kullanıcıya bilgi sunan arayüz

---

## 🧰 Gereksinimler

### Donanım:
- Bilgisayar (Windows/Linux)
- Kamera (USB Webcam önerilir)
- Arduino (Uno/Nano vb.)
- Arduino ile bağlantılı hareketli sistem (örneğin 2 tekerli robot)

### Yazılım:
- Python 3.x
- OpenCV (`opencv-python`)
- NumPy
- PySerial (`pyserial`)
- Arduino IDE (Arduino tarafı için)

---

## 💻 Kurulum

1. Bu projeyi klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/VisionDrive.git
   cd VisionDrive
   ```

2. Python bağımlılıklarını yükleyin:
   ```bash
   pip install opencv-python numpy pyserial
   ```

3. Arduino'yu `COM` portuna bağlayın ve doğru portu `.py` dosyasında güncelleyin:
   ```python
   arduino = serial.Serial('COM11', 9600)
   ```

---

## ▶️ Kullanım

1. Arduino tarafında aşağıdaki gibi basit bir kod kullanabilirsiniz:
   ```cpp
   void setup() {
     Serial.begin(9600);
     pinMode(13, OUTPUT); // Örnek LED uyarı
   }

   void loop() {
     if (Serial.available()) {
       char cmd = Serial.read();
       if (cmd == 'F') {
         // İleri git
       } else if (cmd == 'L') {
         // Sola dön
       } else if (cmd == 'R') {
         // Sağa dön
       }
     }
   }
   ```

2. Python scriptini çalıştırın:
   ```bash
   python vision_drive.py
   ```

3. Kameradaki yeşil nesneyi hareket ettirin. Nesnenin konumuna göre Arduino'ya `"F"`, `"L"`, `"R"` komutları gönderilecektir.

---

## 🧠 Uygulama Alanları

- Otonom robotlar
- Görüntü işleme tabanlı yön bulma sistemleri
- Eğitim ve STEM projeleri
- Arduino-Python entegrasyon demo projeleri

---


## 📝 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına göz atabilirsiniz.

---

## 👨‍💻 Geliştiren

**Yunus Yaman**  
📍 Kahramanmaraş Sütçü İmam Üniversitesi  

