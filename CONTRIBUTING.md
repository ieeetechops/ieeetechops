# Katkı Rehberi

Katkılar yalnızca kodla sınırlı değildir; belge düzeltmeleri, hata raporları, süreç iyileştirmeleri ve proje önerileri değerlidir.

## Başlamadan önce

1. Uygun issue formuyla ihtiyacı kaydedin veya mevcut bir issue seçin.
2. Büyük değişikliklerde uygulamaya başlamadan önce yaklaşım üzerinde anlaşın.
3. Kişisel veri, erişim bilgisi veya kurum içi gizli bilgiyi issue'ya eklemeyin.

## Geliştirme akışı

```bash
git checkout -b docs/kisa-konu
# Değişikliklerinizi yapın
python scripts/check_docs.py
git commit -m "docs: kısa açıklama"
```

Önerilen dal önekleri: `feat/`, `fix/`, `docs/`, `chore/`.

## Commit biçimi

Conventional Commits kullanılır:

- `feat:` yeni özellik
- `fix:` hata düzeltmesi
- `docs:` yalnızca belge değişikliği
- `chore:` bakım ve araç değişikliği
- `refactor:` davranışı değiştirmeyen yeniden düzenleme

## Pull request beklentileri

- Tek, anlaşılır bir amacı olmalı.
- İlgili issue'yu bağlamalı.
- Doğrulama yöntemini açıklamalı.
- Kullanıcı veya operasyon etkisi varsa belgeyi de güncellemeli.
- Otomatik kontroller geçmeli ve en az bir maintainer tarafından incelenmeli.

## Tamamlanma tanımı

Kabul kriterleri karşılanmış, ilgili test/denetimler geçmiş, belgeler güncellenmiş ve takip gerektiren işler ayrı issue olarak kaydedilmişse iş tamamlanmıştır.

