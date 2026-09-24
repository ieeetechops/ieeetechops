<div align="center">

<img src="assets/techops-logo.png" alt="IEEE İKÇÜ TechOps" width="150">

# IEEE İKÇÜ TechOps

### Dijital Altyapı · Otomasyon · Teknik Operasyonlar

**IEEE İzmir Kâtip Çelebi Üniversitesi Öğrenci Kolu'nun teknik operasyon ve dijital dönüşüm ekibi**

<br>

![Status](https://img.shields.io/badge/Durum-Aktif-2E7D32?style=flat-square)
![IEEE](https://img.shields.io/badge/IEEE-İKÇÜ-00629B?style=flat-square\&logo=ieee\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-TechOps-181717?style=flat-square\&logo=github\&logoColor=white)

<br>

**[Hakkımızda](#techops-nedir) · [Çalışma Alanları](#çalışma-alanları) · [Altyapı](#dijital-altyapı) · [Projeler](#aktif-çalışmalar) · [Dokümantasyon](#dokümantasyon) · [İş Birlikleri](#iş-birlikleri)**

</div>

---

## TechOps Nedir?

**TechOps**, IEEE İzmir Kâtip Çelebi Üniversitesi Öğrenci Kolu bünyesinde kullanılan dijital sistemlerin geliştirilmesi, entegrasyonu, sürdürülebilirliği ve teknik operasyonlarından sorumlu çalışma yapısıdır.

TechOps'un temel amacı; organizasyonun dijital altyapısını kişilere bağımlı yapılardan uzaklaştırarak **kurumsal, dokümante edilmiş, aktarılabilir ve sürdürülebilir** bir yapıya dönüştürmektir.

Bu kapsamda yalnızca yeni sistemler geliştirmek değil, mevcut sistemlerin standardizasyonu, entegrasyonu, bakım süreçleri ve sonraki dönemlere güvenli şekilde devredilmesi de TechOps'un sorumluluk alanına girer.

> **Temel yaklaşım:**
> Teknik altyapının bireylere değil organizasyona ait olması ve her yeni yönetim döneminin mevcut sistemlerin üzerine geliştirme yapabilmesi.

---

## Amaç

Öğrenci organizasyonlarında dijital süreçler zaman içerisinde farklı hesaplara, dosyalara ve platformlara dağılabilmektedir.

Bu durum;

* kurumsal bilginin kaybolmasına,
* erişim yetkilerinin belirsizleşmesine,
* verilerin farklı platformlarda parçalanmasına,
* operasyonel süreçlerin kişilere bağımlı hale gelmesine,
* yeni yönetimlerin mevcut sistemleri yeniden kurmak zorunda kalmasına

neden olabilir.

TechOps, bu problemlerin sistematik ve sürdürülebilir bir teknik yapı ile azaltılmasını hedefler.

| Mevcut Problem                  | TechOps Yaklaşımı                            |
| ------------------------------- | -------------------------------------------- |
| Kişisel hesaplara bağımlılık    | Organizasyon merkezli hesap ve erişim yapısı |
| Dağınık veri ve dosyalar        | Merkezi veri ve arşiv standartları           |
| Manuel operasyonlar             | Otomasyon ve entegrasyon sistemleri          |
| Yönetim değişiminde bilgi kaybı | Dokümantasyon ve devir süreçleri             |
| Bağımsız çalışan platformlar    | API ve veri entegrasyonları                  |
| Belirsiz erişim yetkileri       | Rol bazlı erişim modeli                      |
| Tekrar kurulan sistemler        | Sürdürülebilir teknik mimari                 |

---

## Çalışma Alanları

<table>
<tr>
<td width="50%" valign="top">

### Üyelik ve Organizasyon Sistemleri

* Üyelik altyapısının yönetimi
* Kullanıcı doğrulama
* Yetkilendirme
* Gönüllü ve ekip yapılarının yönetimi
* Organizasyon yapısının dijitalleştirilmesi

</td>

<td width="50%" valign="top">

### Etkinlik Operasyonları

* Etkinlik başvuru süreçleri
* Katılımcı yönetimi
* Check-in süreçleri
* Sertifika süreçleri
* Etkinlik verilerinin aktarılması
* Etkinlik sonrası veri arşivleme

</td>
</tr>

<tr>
<td width="50%" valign="top">

### Otomasyon ve Entegrasyon

* Tekrarlayan operasyonların otomasyonu
* Veri senkronizasyonu
* API entegrasyonları
* Raporlama süreçleri
* Operasyonel workflow geliştirme

</td>

<td width="50%" valign="top">

### Dokümantasyon ve Bilgi Yönetimi

* Teknik dokümantasyon
* Sistem envanteri
* Devir dokümanları
* Mimari karar kayıtları
* Operasyonel prosedürler

</td>
</tr>

<tr>
<td width="50%" valign="top">

### Web ve Dijital Servisler

* IEEE İKÇÜ web altyapısı
* İç operasyon araçları
* Yönetim panelleri
* API servisleri
* Organizasyon içi uygulamalar

</td>

<td width="50%" valign="top">

### Altyapı ve Süreklilik

* Hesap ve erişim yönetimi
* Yedekleme süreçleri
* Veri arşivleme
* Sistem sürekliliği
* Yönetim dönemleri arası teknik devir

</td>
</tr>
</table>

---

## Dijital Altyapı

TechOps'un hedefi tüm süreçleri tek ve büyük bir platform altında toplamak değildir.

Bunun yerine mevcut sistemlerin gerektiğinde birbirleriyle iletişim kurabildiği, bileşenlerin bağımsız olarak değiştirilebildiği ve yeni servislerin sisteme kontrollü biçimde eklenebildiği **modüler bir dijital altyapı** hedeflenmektedir.

```text
                        IEEE İKÇÜ
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Üyeler ve Gönüllüler │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Web ve Üyelik Sistemi│
                 └──────────┬──────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
     ┌──────────────────┐        ┌──────────────────┐
     │ Etkinlik Yönetimi│        │ Proje Yönetimi   │
     └────────┬─────────┘        └────────┬─────────┘
              │                           │
              ├── Başvurular              │
              ├── Katılımcılar            │
              ├── Check-in                │
              ├── Sertifikalar            │
              │                           │
              └────────────┬──────────────┘
                           ▼
                ┌──────────────────────┐
                │ Organizasyon Verisi │
                └──────────┬───────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
      Otomasyon        Raporlama        Arşivleme
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                ┌──────────────────────┐
                │ Dokümantasyon ve KB │
                └──────────────────────┘
```

---

## Mevcut Teknoloji Altyapısı

<div align="center">

![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square\&logo=github\&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square\&logo=git\&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square\&logo=firebase\&logoColor=black)
![WordPress](https://img.shields.io/badge/WordPress-21759B?style=flat-square\&logo=wordpress\&logoColor=white)
![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=flat-square\&logo=googledrive\&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-34A853?style=flat-square\&logo=googlesheets\&logoColor=white)

</div>

<br>

| Alan                   | Sistem                     |
| ---------------------- | -------------------------- |
| Web sitesi             | WordPress                  |
| Kimlik doğrulama       | Firebase Authentication    |
| Üye verileri           | Firebase Realtime Database |
| Etkinlik yönetimi      | HeptaCert                  |
| Form süreçleri         | Google Forms               |
| Operasyonel veri       | Google Sheets              |
| Dosya yönetimi         | Google Drive               |
| Kaynak kod yönetimi    | GitHub                     |
| Sistem entegrasyonları | REST API / CSV / Webhook   |

---

## Aktif Çalışmalar

| Çalışma                    | Kapsam                                                         | Durum        |
| -------------------------- | -------------------------------------------------------------- | ------------ |
| **Drive Yapılandırması**   | Dosya, klasör ve erişim standartlarının oluşturulması          | Devam Ediyor |
| **Üyelik Altyapısı**       | WordPress ve Firebase tabanlı üyelik sisteminin geliştirilmesi | Devam Ediyor |
| **HeptaCert Entegrasyonu** | Etkinlik verilerinin IEEE altyapısına aktarılması              | Devam Ediyor |
| **Raporlama Otomasyonu**   | Etkinlik ve dönem raporlarının otomatik oluşturulması          | Planlama     |
| **Merkezi Veri Yapısı**    | Organizasyon verilerinin ortak standart altında düzenlenmesi   | Planlama     |
| **Erişim Yönetimi**        | Görev ve komite bazlı yetkilendirme modelinin oluşturulması    | Devam Ediyor |
| **TechOps Dokümantasyonu** | Teknik ve operasyonel süreçlerin belgelenmesi                  | Aktif        |

---

## Teknik İlkeler

### Organizasyon Sahipliği

Kritik hesapların, sistemlerin ve verilerin tek bir kişinin kişisel hesabına bağımlı olmaması hedeflenir.

### Sürdürülebilirlik

Kurulan altyapının yalnızca mevcut yönetim dönemi için değil, sonraki ekipler tarafından da kullanılabilir olması gerekir.

### Devredilebilirlik

Yeni TechOps ekipleri mevcut altyapıyı yeniden keşfetmek yerine, dokümantasyon üzerinden sistemi anlayabilmeli ve geliştirmeye devam edebilmelidir.

### Modülerlik

Farklı sistemlerin gerektiğinde birbirlerinden bağımsız olarak güncellenebilmesi veya değiştirilebilmesi amaçlanır.

### Düşük Operasyon Maliyeti

Mümkün olduğu ölçüde ücretsiz, açık kaynak, eğitim amaçlı veya topluluk destekli servisler tercih edilir.

### Dokümantasyon

Teknik bilginin yalnızca sistemi geliştiren kişide kalmaması temel gereksinimlerden biridir.

### Veri Minimizasyonu

Sistemlerde yalnızca operasyon için gerekli verilerin tutulması ve gereksiz veri kopyalarının azaltılması hedeflenir.

---

## Repository Yapısı

Bu repository, TechOps'un merkezi teknik dokümantasyon ve koordinasyon alanı olarak kullanılmaktadır.

```text
techops/
│
├── assets/
│   └── techops-logo.png
│
├── docs/
│   ├── architecture/
│   ├── infrastructure/
│   ├── policies/
│   ├── workflows/
│   └── guides/
│
├── automation/
│
├── integrations/
│
├── scripts/
│
├── templates/
│
├── CONTRIBUTING.md
│
└── README.md
```

Bağımsız uygulamalar ve kapsamlı servisler gerektiğinde ayrı repository'lerde yönetilebilir.

---

## Dokümantasyon

TechOps kapsamında aşağıdaki temel dokümanların oluşturulması ve güncel tutulması planlanmaktadır.

* [ ] TechOps Dijital Dönüşüm Bildirgesi
* [ ] Sistem ve Servis Envanteri
* [ ] Teknik Mimari Dokümanı
* [ ] Google Drive Yapısı
* [ ] Erişim ve Yetkilendirme Politikası
* [ ] Etkinlik Veri Yaşam Döngüsü
* [ ] Yedekleme ve Arşivleme Politikası
* [ ] API ve Entegrasyon Dokümantasyonu
* [ ] Yönetim Devir Rehberi
* [ ] Sistem Kurtarma Rehberi
* [ ] Katkı ve Geliştirme Rehberi

---

## Açık Kaynak Yaklaşımı

TechOps kapsamında geliştirilen ve diğer öğrenci topluluklarının da faydalanabileceği genel amaçlı araçların mümkün olduğu ölçüde açık kaynak olarak paylaşılması hedeflenmektedir.

Aşağıdaki içerikleri barındıran repository'ler ise herkese açık tutulmaz:

* kişisel veriler,
* üye ve katılımcı bilgileri,
* erişim anahtarları ve kimlik bilgileri,
* kurum içi kayıtlar,
* hassas sistem yapılandırmaları,
* paylaşımı kısıtlı IEEE verileri.

---

## İş Birlikleri

IEEE İKÇÜ TechOps; öğrenci topluluklarının sürdürülebilir teknik altyapılar oluşturmasını destekleyen şirketler, geliştirici toplulukları ve teknoloji kuruluşlarıyla iş birliklerine açıktır.

Öncelikli iş birliği alanlarımız:

| Alan                   | İhtiyaç                                    |
| ---------------------- | ------------------------------------------ |
| Cloud Infrastructure   | Uygulama ve servis barındırma              |
| Storage & Backup       | Kurumsal veri saklama ve yedekleme         |
| Hosting & CDN          | Web servisleri ve içerik dağıtımı          |
| CI/CD                  | Yazılım geliştirme süreçleri               |
| Developer Tools        | Ekip geliştirme araçları                   |
| Monitoring             | Sistem gözlemlenebilirliği                 |
| Technical Mentorship   | Teknik bilgi ve danışmanlık                |
| Community Partnerships | Öğrenci teknoloji ekosistemi iş birlikleri |

---

## Yol Haritası

```mermaid
flowchart LR
    A[Mevcut Sistemlerin Analizi]
    --> B[Standardizasyon]
    --> C[Merkezi Veri Yapısı]
    --> D[Entegrasyonlar]
    --> E[Otomasyon]
    --> F[Dokümantasyon]
    --> G[Sürdürülebilir Devir]
```

---

## IEEE İKÇÜ Hakkında

**IEEE İzmir Kâtip Çelebi Üniversitesi Öğrenci Kolu**, İzmir Kâtip Çelebi Üniversitesi bünyesinde faaliyet gösteren öğrenci organizasyonlarından biridir.

TechOps, öğrenci kolunun teknik, operasyonel ve organizasyonel faaliyetlerini destekleyen dijital altyapının geliştirilmesi ve sürdürülebilirliği üzerine çalışır.

---

## İletişim

**IEEE İzmir Kâtip Çelebi Üniversitesi Öğrenci Kolu**
**TechOps**

İzmir Kâtip Çelebi Üniversitesi
İzmir, Türkiye

---

<div align="center">

**IEEE İKÇÜ TechOps**

Sürdürülebilir dijital altyapı.
Dokümante edilmiş süreçler.
Devredilebilir sistemler.

</div>
