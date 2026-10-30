# Görme Alanı Haritası

Evde görme alanı takibi için tarayıcıda çalışan bir PWA. Görme alanındaki lekeyi ölçer, kaydeder ve önceki testlerle karşılaştırır. Aynı gün tekrarlanan testlerden "anlamlı değişim" eşiğini hesaplar.

> Tanı aracı değildir. Ev takibi ve Ar-Ge amaçlıdır.

## Modlar

- **Otomatik tam alan:** Kalibre edilmiş ekranda eşik üstü (suprathreshold) test yapılır. 3° veya 2° aralıklı ızgaradaki noktalar 200 ms gösterilir; görülmeyen noktalar bir kez daha sorulur.
- **Kör nokta doğrulama:** Temporal 10–21°, −8…+5° bölgesi 1° aralıkla taranır. Ölçülen fizyolojik kör nokta literatürle (merkez 15,5° / −1,5°, 5,5° × 7,5°) karşılaştırılır. Uygulamanın doğruluğu bu ölçümle gösterilir.
- **Elle işaretleme:** 25×25 harf ızgarasında görülmeyen ve bulanık bölgeler işaretlenir.

## Güvenilirlik

- **Sabitleme kaybı (Heijl-Krakau):** Uyaranların ~%8'i kör noktaya gösterilir. Kişi bunları "gördüm" derse sabitleme kaybı sayılır. Kör nokta konumu olarak, varsa kullanıcının kendi doğrulama ölçümlerinin ortalaması, yoksa literatür değeri kullanılır.
- **Yanlış pozitif:** Uyaranların ~%8'inde hiçbir şey gösterilmez; bunlara verilen cevaplar yanlış pozitif sayılır.
- Sabitleme kaybı ≤ %20 ve yanlış pozitif ≤ %15 olan testler **güvenilir** sayılır. Anlamlılık hesabına yalnızca güvenilir testler girer.

## Anlamlı değişim

Aynı gün aynı ayarla en az 3 güvenilir test yapılırsa tekrarlanabilirlik katsayısı hesaplanır: **CoR = 2,77 × SD**. İki test arasındaki alan farkı CoR'u aşarsa "anlamlı değişim", aşmazsa "gürültü içinde" yazılır.

## Geometri

`px = tan(θ) × mesafe_mm × px_per_mm`. Ekran ölçeği banka kartıyla (85,6 mm) kalibre edilir, mesafe elle girilir.

## Geliştirme

```
src/app.html            kaynak (tek dosya: HTML + CSS + JS)
build.py                docs/index.html (GitHub Pages) ve dist/artifact.html üretir
docs/                   yayınlanan PWA
```

```
python build.py
```

GitHub Pages: Settings → Pages → Branch `main`, klasör `/docs`.

Veriler tarayıcının localStorage'ında tutulur. "Yedekle / geri yükle" bölümünden JSON olarak taşınabilir.

## Yol haritası

- [x] Elle işaretleme, alan / yüzde / kadran, önceki testle bindirme
- [x] Otomatik eşik üstü test motoru, tekrar sorma, duraklatma
- [x] Sabitleme kaybı ve yanlış pozitif kontrolü, güvenilirlik etiketi
- [x] Kör nokta doğrulama modu, literatürle kıyas
- [x] Tekrarlanabilirlik katsayısı ve anlamlı değişim etiketi
- [ ] Kör nokta doğrulaması: sağ ve sol göz için 5'er tekrar, sonuçların raporlanması
- [ ] Web kamerası ile mesafe ölçümü (MediaPipe iris, ~11,7 mm)
- [ ] Web kamerası ile sabitleme takibi
- [ ] Flask + SQLite ile cihazlar arası senkronizasyon
- [ ] Service worker ile çevrimdışı çalışma
