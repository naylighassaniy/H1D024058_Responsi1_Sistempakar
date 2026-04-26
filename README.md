# SkinSight — Sistem Pakar Pendeteksi Masalah Kulit
### Berbasis Metode Forward Chaining

> Dibuat sebagai bagian dari Responsi Kecerdasan Buatan — Semester 4

---

## 🌸 Tentang Aplikasi

**SkinSight** adalah sistem pakar berbasis kecerdasan buatan yang membantu kamu mengidentifikasi jenis masalah kulit wajah berdasarkan gejala yang dirasakan. Setelah diagnosis, sistem juga memberikan rekomendasi bahan aktif skincare yang tepat beserta rutinitas perawatan yang sesuai.

Aplikasi ini dibangun menggunakan metode **Forward Chaining** — teknik inferensi pada sistem pakar yang meniru cara seorang dermatologis menganalisis kondisi kulit pasiennya secara sistematis.

---

## 🧠 Penjelasan Sistem

### Apa itu Sistem Pakar?

Sistem pakar (*expert system*) adalah program komputer yang meniru kemampuan seorang ahli dalam bidang tertentu untuk memecahkan masalah. Sistem ini terdiri dari dua komponen utama:

- **Basis Pengetahuan (Knowledge Base)** — kumpulan fakta dan aturan IF-THEN yang diperoleh dari pengetahuan pakar
- **Mesin Inferensi (Inference Engine)** — mekanisme yang memproses aturan untuk menghasilkan kesimpulan

---

### Metode: Forward Chaining

**Forward Chaining** adalah strategi inferensi yang bergerak dari **fakta → kesimpulan**. Sistem memulai dari gejala yang dipilih pengguna, lalu mencocokkannya dengan aturan-aturan yang ada hingga menemukan diagnosis.

```
Fakta (Gejala) → Pencocokan Rule → Fakta Baru → ... → Kesimpulan (Diagnosis)
```

**Alur kerja:**

```
1. User memilih gejala
        ↓
2. Sistem mencocokkan gejala dengan kondisi setiap rule
        ↓
3. Rule yang semua kondisinya terpenuhi → AKTIF (fired)
        ↓
4. Skor tiap diagnosis dihitung berdasarkan rule yang aktif
        ↓
5. Diagnosis dengan skor tertinggi → OUTPUT
```

---

### Basis Pengetahuan

Sistem memiliki **5 kategori diagnosis** dengan total **15 aturan IF-THEN**:

| Kode | Diagnosis |
|---|---|
| D1 | Kulit Berjerawat (Acne-Prone) |
| D2 | Kulit Kering (Dry Skin) |
| D3 | Hiperpigmentasi |
| D4 | Kulit Sensitif & Reaktif |
| D5 | Kulit Berminyak (Oily Skin) |

---

### Gejala yang Digunakan

**Kelompok 1 — Kondisi Umum:**

| Kode | Gejala |
|---|---|
| G1_1 | Kulit terasa berminyak |
| G1_2 | Kulit terasa kering & kencang |
| G1_3 | Kulit kombinasi |
| G1_4 | Kulit terasa normal |

**Kelompok 2 — Masalah yang Terlihat:**

| Kode | Gejala |
|---|---|
| G2_1 | Jerawat aktif / meradang |
| G2_2 | Komedo / blackhead |
| G2_3 | Flek / noda gelap |
| G2_4 | Kulit kusam & tidak cerah |
| G2_5 | Kemerahan / ruam |
| G2_6 | Kulit mengelupas / flaky |

**Kelompok 3 — Sensasi yang Dirasakan:**

| Kode | Gejala |
|---|---|
| G3_1 | Gatal atau perih |
| G3_2 | Pori-pori terasa besar |
| G3_3 | Kulit sangat sensitif |
| G3_4 | Tekstur tidak rata |

---

### Contoh Aturan (Rule Base)

```
R1  : IF jerawat aktif                         → Acne-Prone
R2  : IF berminyak AND komedo                  → Acne-Prone
R4  : IF kulit kering & kencang                → Dry Skin
R5  : IF kering AND mengelupas                 → Dry Skin
R7  : IF flek/noda gelap                       → Hiperpigmentasi
R10 : IF kemerahan/ruam                        → Kulit Sensitif
R11 : IF gatal/perih AND sangat sensitif       → Kulit Sensitif
R13 : IF berminyak AND pori besar              → Oily Skin
```

---

### Perhitungan Confidence

Tingkat keyakinan (*confidence*) diagnosis dihitung berdasarkan proporsi skor diagnosis utama terhadap total skor seluruh diagnosis yang aktif:

```
Confidence = (Skor Diagnosis Utama / Total Skor) × 100%
```

Nilai maksimum yang ditampilkan adalah **95%** untuk menghindari kesan terlalu deterministik.

---

### Output Sistem

Untuk setiap diagnosis, sistem memberikan:
- ✅ **Nama & deskripsi** kondisi kulit
- ✅ **Tingkat keyakinan** dalam persen
- ✅ **Penjelasan penyebab** dan hal yang perlu diwaspadai
- ✅ **Bahan aktif skincare** yang direkomendasikan dan perlu dihindari
- ✅ **Rutinitas perawatan** langkah demi langkah
- ✅ **Jejak rule** yang aktif (transparansi inferensi)

---

## 🛠️ Teknologi yang Digunakan

| Komponen | Teknologi |
|---|---|
| Backend | Python + Flask |
| Frontend | HTML, CSS, JavaScript |
| Template Engine | Jinja2 |
| Hosting | Vercel |
| Metode Inferensi | Forward Chaining (implementasi manual) |

---

## 📁 Struktur Project

```
skinsight/
├── app.py              ← Entry point Flask & routing API
├── expert_engine.py    ← Knowledge base & Forward Chaining engine
├── requirements.txt    ← Daftar dependencies Python
├── vercel.json         ← Konfigurasi hosting Vercel
├── templates/
│   └── index.html      ← Halaman utama (Jinja2)
└── static/
    ├── css/style.css   ← Styling antarmuka
    └── js/main.js      ← Logika frontend & komunikasi API
```

---

## 🔗 Cara Menggunakan Aplikasi

1. Buka aplikasi melalui link yang tersedia
2. Baca petunjuk di halaman utama
3. **Pilih semua gejala** yang saat ini kamu rasakan pada kulit wajah (minimal 2 gejala)
4. Klik tombol **"Mulai Analisis → Diagnosis"**
5. Sistem akan menampilkan:
   - Diagnosis jenis masalah kulit
   - Tingkat keyakinan sistem
   - Rekomendasi bahan aktif skincare
   - Rutinitas perawatan yang disarankan
   - Jejak rule forward chaining yang aktif
6. Klik **"Ulangi Diagnosa"** untuk mencoba kombinasi gejala berbeda

---

## 👩‍💻 Pengembang

**Nayligha Ssaniy** — Mahasiswa Informatika Semester 4

---

*Responsi Kecerdasan Buatan 2026*
