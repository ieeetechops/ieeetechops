# Güvenlik Politikası

## Güvenlik açığı bildirimi

Güvenlik açıklarını herkese açık issue olarak paylaşmayın. Bu repo için GitHub'ın **Security → Report a vulnerability** alanını kullanın. Private vulnerability reporting etkin değilse IEEE İKÇÜ'nün doğrulanmış kurumsal iletişim kanalından TechOps sorumlusuna ulaşın.

Bildirimde hassas veriyi kopyalamadan şu bilgileri paylaşın:

- Etkilenen proje veya servis
- Sorunun kısa açıklaması ve olası etkisi
- Güvenli yeniden üretim adımları
- Varsa geçici çözüm önerisi

## Temel güvenlik kuralları

- Parola, token, API anahtarı ve servis hesabı dosyası commit edilmez.
- Her kullanıcı kendi hesabını ve çok faktörlü kimlik doğrulamayı kullanır.
- Üretim verisi test ortamına kopyalanmaz.
- Kişisel veri issue, commit, log veya ekran görüntüsüne eklenmez.
- Şüpheli secret önce iptal edilir/döndürülür; yalnızca Git geçmişinden silmek yeterli değildir.

## Yanıt süreci

Bildirim alındığında etki değerlendirilir, zarar sınırlandırılır, gerekli anahtarlar döndürülür ve düzeltme koordineli şekilde yayımlanır. Kritik olayların ardından suçlayıcı olmayan bir olay sonrası inceleme yapılır.

