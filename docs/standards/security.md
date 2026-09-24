# Güvenlik İlkeleri

## Kimlik ve erişim

- Her kullanıcı ayrı hesap ve çok faktörlü kimlik doğrulama kullanır.
- Erişim göreve göre, gereken en düşük yetkiyle ve mümkünse süreli verilir.
- Görev değişimi ve ekipten ayrılmada erişim aynı gün gözden geçirilir.
- Kritik hesapların kurtarma yöntemi organizasyon kontrolünde olur.

## Secret yönetimi

- Parola, API anahtarı, token, private key ve webhook URL'si repoya yazılmaz.
- Yerel geliştirmede gerçek değerleri içermeyen `.env.example` kullanılır.
- Otomasyon secret'ları platformun secret store'unda tutulur.
- Sızan secret derhal iptal edilir veya döndürülür.

## Veri

- Yalnızca operasyon için gereken veri toplanır.
- Gerçek üye/katılımcı verisi test ortamında kullanılmaz.
- Dışa aktarılan dosyaların sahibi, amacı ve silme tarihi olur.
- Loglar parola, token veya gereksiz kişisel veri içermez.

## Bildirim

Bir açık veya sızıntı şüphesinde herkese açık issue açmayın. Repodaki [`SECURITY.md`](https://github.com/ieeetechops/ieeetechops/security/policy) politikasını izleyin.

!!! danger "Önce erişimi kesin"
    Bir secret'ın sızdığını düşünüyorsanız önce iptal edin/döndürün. Commit'i silmek veya repoyu private yapmak tek başına koruma sağlamaz.

