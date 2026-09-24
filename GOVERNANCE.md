# TechOps Yönetişim Modeli

## İlkeler

- Kritik sistemler kişilere değil organizasyona aittir.
- Yetki, görev için gereken en düşük seviyede verilir.
- Kalıcı teknik kararlar yazılı ve izlenebilir olmalıdır.
- Üretim değişiklikleri gözden geçirilebilir ve geri alınabilir olmalıdır.
- Güvenlik ve kişisel veri, hız uğruna ikinci plana atılmaz.

## Roller

| Rol | Sorumluluk |
| --- | --- |
| Branch Chair | Kurumsal hesap verebilirlik ve yüksek riskli kararlar |
| TechOps Lead | Teknik yön, öncelik, erişim ve servis sahipliği |
| Proje/Servis Sahibi | Projenin sağlığı, dokümantasyonu ve devamlılığı |
| Maintainer | Kod ve belge incelemesi, bakım ve yayınlama |
| Contributor | Issue kapsamındaki geliştirme ve dokümantasyon |

Bir kişi birden fazla rol üstlenebilir; ancak kritik erişim ve kararlar mümkün olduğunda ikinci kişi tarafından doğrulanır.

## Karar modeli

- Küçük ve geri alınabilir değişiklikler pull request incelemesiyle kabul edilir.
- Yeni servis, veri kaynağı veya önemli mimari değişiklik ADR gerektirir.
- Kişisel veri, maliyet veya kurum çapı risk içeren kararlar TechOps Lead ve ilgili yönetim rolünün onayını gerektirir.
- Acil olayda önce zarar sınırlandırılabilir; karar ve takip işleri sonradan kayıt altına alınır.

## Çalışma ritmi

- Haftalık: öncelikler, sorumlular ve engeller
- Aylık: proje/servis sağlığı ve teknik borç
- Dönem ortası: erişim ve sahiplik kontrolü
- Dönem sonu: devir provası ve kurtarma doğrulaması

## Değişiklik süreci

Öneri → issue → sahip ve kabul kriterleri → pull request → inceleme → yayınlama → dokümantasyon. Kritik değişiklikte geri alma planı zorunludur.

