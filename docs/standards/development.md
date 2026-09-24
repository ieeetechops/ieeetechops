# Geliştirme Standartları

## Repository

- `main` her zaman yayınlanabilir durumda tutulur.
- Değişiklikler kısa ömürlü dallar ve pull request üzerinden birleştirilir.
- Üretilen dosyalar, yerel ortamlar ve secret'lar `.gitignore` dışında tutulur.
- Bağımsız ürünler kendi reposunda yaşar; bu repo ortak belge ve standartların kaynağıdır.

## Değişiklik

- Küçük, tek amaçlı pull request tercih edilir.
- Kullanıcı davranışı değişiyorsa belge ve test birlikte güncellenir.
- Üretim etkili değişiklikte doğrulama ve geri alma adımı bulunur.
- Kalıcı mimari kararlar [ADR](../decisions/index.md) olarak kaydedilir.

## Commit

```text
feat: başvuru filtrelerini ekle
fix: yinelenen katılım kaydını engelle
docs: devir rehberini güncelle
chore: dokümantasyon bağımlılığını güncelle
```

## Kalite kapıları

Her proje teknolojisine uygun olarak en az biçim denetimi, statik analiz, test ve build kontrolü çalıştırmalıdır. Güvenlik taramaları kişisel veri veya secret'ı loglamamalıdır.

## Bağımlılıklar

Yeni bağımlılık; lisans, bakım durumu, güvenlik geçmişi, paket boyutu ve gerçekten gerekli olup olmadığı değerlendirilerek eklenir. Sabitlenmiş veya kontrollü sürüm aralığı kullanılır.

