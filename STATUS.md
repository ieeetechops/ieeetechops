# Sistem Durumu

Son gözden geçirme: **24 Eylül 2026**

Bu sayfa servislerin yaşam döngüsü ve izleme hazırlığını gösterir; gerçek zamanlı uptime ekranı değildir. Bir kesinti yaşıyorsanız teknik destek issue'su açın. Güvenlik şüphesinde [özel bildirim yöntemini](SECURITY.md) kullanın.

| Servis alanı | Yaşam döngüsü | İzleme | Operasyon sahibi |
| --- | --- | --- | --- |
| WordPress web sitesi | Üretim | Manuel kontrol | Belirlenecek |
| Firebase Authentication | Üretim | Sağlayıcı paneli | Belirlenecek |
| Firebase üye verisi | Üretim | Sağlayıcı paneli | Belirlenecek |
| HeptaCert | Üretim / dış servis | Sağlayıcı bildirimi | Belirlenecek |
| Google Workspace | Üretim / dış servis | Sağlayıcı durum ekranı | Belirlenecek |
| GitHub organizasyonu | Üretim / dış servis | GitHub Actions ve durum ekranı | TechOps |
| TechOps dokümantasyon sitesi | Kurulum aşaması | GitHub Actions | TechOps |

## Durum seviyeleri

- **Üretim:** Günlük operasyonlarda kullanılıyor.
- **Bakım:** Kullanılıyor, ancak yalnızca hata ve güvenlik bakımı alıyor.
- **Kurulum aşaması:** Henüz resmi üretim servisi değil.
- **Arşiv:** Yeni kullanım yok; kontrollü kapatma veya veri çıkarma için tutuluyor.

## Sıradaki iyileştirmeler

- Her servis için rol bazlı sahip ve yedek tanımlamak
- Kullanıcı açısından önemli kontrolleri otomatikleştirmek
- Uyarıların tek bir TechOps operasyon kanalına ulaşmasını sağlamak
- Kesinti iletişimi ve olay sonrası inceleme akışını test etmek

