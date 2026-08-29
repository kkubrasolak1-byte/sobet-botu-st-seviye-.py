import requests
import os

# Ses klasörü oluştur
if not os.path.exists('sounds'):
    os.makedirs('sounds')

# MyInstants sayfasından ses dosyasını indir
url = "https://www.myinstants.com/en/instant/fart/?utm_source=copy&utm_medium=share"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    
    # HTML'den ses dosyasının URL'sini çıkart
    import re
    audio_urls = re.findall(r'https://[^\s"<>]+\.(?:mp3|wav|ogg|m4a)', response.text)
    
    if audio_urls:
        audio_url = audio_urls[0]
        print(f"Ses dosyası URL'si bulundu: {audio_url}")
        
        # Ses dosyasını indir
        audio_response = requests.get(audio_url, headers=headers, timeout=10)
        audio_response.raise_for_status()
        
        # Dosyayı kaydet
        with open('sounds/tirt.mp3', 'wb') as f:
            f.write(audio_response.content)
        print("Ses dosyası başarıyla indirildi: sounds/tirt.mp3")
    else:
        print("Ses dosyası URL'si bulunamadı!")
except Exception as e:
    print(f"Hata: {e}")
