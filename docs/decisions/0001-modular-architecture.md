# ADR-0001: Modüler servis mimarisi

- **Durum:** Kabul
- **Tarih:** 2026-09-24
- **Karar sahibi:** IEEE İKÇÜ TechOps

## Bağlam

Operasyonlar WordPress, Firebase, HeptaCert, Google Workspace ve GitHub gibi farklı servislerden yararlanır. Her şeyi tek uygulamada yeniden geliştirmek yüksek bakım maliyeti ve yeni bir tek hata noktası oluşturur.

## Karar

Alanında güçlü servisler korunacak; açık sahiplik, veri sınırları ve belgelenmiş entegrasyonlarla modüler bir sistem kurulacaktır. Bu repo ortak standartların ve teknik hafızanın merkezi olacaktır. Bağımsız ürünler ayrı repolarda yaşayacaktır.

## Sonuçlar

- Servisler bağımsız geliştirilebilir veya değiştirilebilir.
- Her entegrasyonun sahibi, veri akışı ve hata davranışı belgelenmelidir.
- Veri kopyaları ve manuel dışa aktarımlar kontrol altında tutulmalıdır.
- Yeni platform eklemeden önce mevcut araçlarla ihtiyacın karşılanıp karşılanmadığı değerlendirilir.

