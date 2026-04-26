# ============================================================
#  expert_engine.py
#  Implementasi Sistem Pakar — SkinSight
#  Metode  : Forward Chaining
# ============================================================


# ── KNOWLEDGE BASE ───────────────────────────────────────────
KNOWLEDGE_BASE = {
    "acne": {
        "name":     "Kulit Berjerawat (Acne-Prone)",
        "subtitle": (
            "Kulitmu cenderung rentan terhadap jerawat akibat produksi sebum berlebih "
            "dan penyumbatan pori. Perlu perawatan konsisten dan produk non-komedogenik."
        ),
        "rules": [
            {"id": "R1",  "conditions": ["g2_1"],        "desc": "IF jerawat aktif/meradang THEN acne-prone"},
            {"id": "R2",  "conditions": ["g1_1", "g2_2"], "desc": "IF berminyak AND komedo THEN acne-prone"},
            {"id": "R3",  "conditions": ["g2_1", "g3_2"], "desc": "IF jerawat aktif AND pori besar THEN acne-prone"},
        ],
        "cards": [
            {
                "icon":  "🔬",
                "title": "Penyebab Utama",
                "body":  "Produksi sebum berlebih, bakteri C. acnes, dan pori tersumbat oleh sel kulit mati menjadi pemicu utama terbentuknya jerawat.",
            },
            {
                "icon":  "⚠️",
                "title": "Perlu Diwaspadai",
                "body":  "Jangan memencet jerawat — bisa menyebabkan bekas luka permanen dan menyebarkan bakteri ke area sekitar.",
            },
        ],
        "ingredients_good": ["Salicylic Acid (BHA)", "Niacinamide", "Benzoyl Peroxide", "Tea Tree Oil", "Zinc", "Azelaic Acid"],
        "ingredients_bad":  ["Coconut Oil", "Isopropyl Myristate", "Minyak Mineral", "Alkohol Tinggi", "Produk Komedogenik"],
        "routine": [
            {"step": "Cleanser (pagi & malam)", "desc": "Gunakan pembersih berbahan Salicylic Acid 0.5–2% untuk membersihkan pori secara mendalam."},
            {"step": "Toner Eksfoliasi (malam)", "desc": "BHA toner untuk mengangkat sel kulit mati dan mencegah penyumbatan pori."},
            {"step": "Serum Niacinamide",        "desc": "Aplikasikan serum niacinamide 5–10% untuk mengontrol sebum dan menenangkan kulit."},
            {"step": "Moisturizer Non-Komedogenik", "desc": "Pilih gel moisturizer atau lotion ringan berbasis air."},
            {"step": "Sunscreen SPF 30+",        "desc": "Wajib setiap pagi! Cari yang bertuliskan non-comedogenic atau oil-free."},
        ],
    },

    "dry": {
        "name":     "Kulit Kering (Dry Skin)",
        "subtitle": (
            "Kulitmu kekurangan kelembaban dan lipid alami sehingga terasa kencang, kasar, "
            "dan mudah mengelupas. Fokus utama adalah hidrasi dan memperkuat skin barrier."
        ),
        "rules": [
            {"id": "R4",  "conditions": ["g1_2"],         "desc": "IF kulit kering & kencang THEN dry skin"},
            {"id": "R5",  "conditions": ["g1_2", "g2_6"], "desc": "IF kering AND mengelupas THEN dry skin"},
            {"id": "R6",  "conditions": ["g2_6", "g3_4"], "desc": "IF mengelupas AND tekstur kasar THEN dry skin"},
        ],
        "cards": [
            {
                "icon":  "💧",
                "title": "Kondisi Kulit",
                "body":  "Skin barrier yang lemah menyebabkan TEWL (Trans Epidermal Water Loss) tinggi — air menguap lebih cepat dari permukaan kulit.",
            },
            {
                "icon":  "🌡️",
                "title": "Faktor Pemicu",
                "body":  "Cuaca dingin/berangin, mandi air panas, produk keras berbahan alkohol, dan kurang minum air dapat memperparah kondisi.",
            },
        ],
        "ingredients_good": ["Hyaluronic Acid", "Ceramide", "Glycerin", "Squalane", "Shea Butter", "Peptida", "Panthenol"],
        "ingredients_bad":  ["Alkohol Denat", "Fragrance/Pewangi", "Retinol (awal)", "AHA konsentrasi tinggi", "SLS/SLES"],
        "routine": [
            {"step": "Oil / Cream Cleanser",    "desc": "Pembersih berbasis krim atau minyak yang tidak merusak lapisan lipid alami kulit."},
            {"step": "Hydrating Toner",          "desc": "Toner berbasis hyaluronic acid atau essence untuk lapisan hidrasi pertama."},
            {"step": "Serum Hyaluronic Acid",    "desc": "HA menarik kelembaban dari udara ke dalam kulit. Aplikasikan di kulit yang sedikit lembab."},
            {"step": "Moisturizer Kaya Lipid",   "desc": "Krim tebal dengan ceramide untuk mengunci kelembaban dan memperbaiki skin barrier."},
            {"step": "Face Oil (malam)",         "desc": "Tambahkan facial oil sebagai lapisan terakhir malam hari untuk mencegah penguapan air."},
        ],
    },

    "hyperpigmentation": {
        "name":     "Hiperpigmentasi",
        "subtitle": (
            "Kulitmu mengalami produksi melanin berlebih yang menyebabkan noda gelap, "
            "bekas jerawat, atau warna kulit tidak merata. Diperlukan bahan aktif pencerah yang konsisten."
        ),
        "rules": [
            {"id": "R7",  "conditions": ["g2_3"],         "desc": "IF flek/noda gelap THEN hiperpigmentasi"},
            {"id": "R8",  "conditions": ["g2_3", "g2_4"], "desc": "IF flek AND kusam THEN hiperpigmentasi"},
            {"id": "R9",  "conditions": ["g2_1", "g2_3"], "desc": "IF jerawat aktif AND flek THEN hiperpigmentasi post-acne"},
        ],
        "cards": [
            {
                "icon":  "🌑",
                "title": "Jenis Hiperpigmentasi",
                "body":  "PIH (Post Inflammatory Hyperpigmentation) akibat bekas jerawat, melasma karena hormon/sinar UV, dan sunspot dari paparan matahari.",
            },
            {
                "icon":  "☀️",
                "title": "Pentingnya Sunscreen",
                "body":  "Sinar UV memperparah produksi melanin. Tanpa sunscreen, semua produk pencerah tidak akan bekerja optimal.",
            },
        ],
        "ingredients_good": ["Vitamin C (L-Ascorbic Acid)", "Niacinamide", "Alpha Arbutin", "Kojic Acid", "Tranexamic Acid", "AHA/Glikolik Acid", "Retinol"],
        "ingredients_bad":  ["Paparan UV tanpa SPF", "Fragrance Tinggi", "Produk pemutih mengandung merkuri", "Eksfoliasi berlebihan"],
        "routine": [
            {"step": "Gentle Cleanser",          "desc": "Pembersih lembut yang tidak mengiritasi — iritasi dapat memperburuk hiperpigmentasi."},
            {"step": "Vitamin C Serum (pagi)",   "desc": "Antioksidan kuat yang menghambat produksi melanin dan melindungi dari radikal bebas."},
            {"step": "Serum Alpha Arbutin / Niacinamide", "desc": "Kombinasi pencerah efektif untuk meratakan warna kulit tanpa iritasi berlebihan."},
            {"step": "Moisturizer",              "desc": "Jaga skin barrier tetap sehat agar bahan aktif bekerja lebih optimal."},
            {"step": "Sunscreen SPF 50+ (WAJIB)","desc": "Ini langkah TERPENTING. Tanpa proteksi UV, noda gelap tidak akan memudar."},
        ],
    },

    "sensitive": {
        "name":     "Kulit Sensitif & Reaktif",
        "subtitle": (
            "Kulitmu memiliki skin barrier yang tipis atau reaktif terhadap berbagai stimulus. "
            "Pendekatan gentle dan minimal adalah kuncinya."
        ),
        "rules": [
            {"id": "R10", "conditions": ["g2_5"],          "desc": "IF kemerahan/ruam THEN sensitif"},
            {"id": "R11", "conditions": ["g3_1", "g3_3"],  "desc": "IF gatal/perih AND sangat sensitif THEN sensitif"},
            {"id": "R12", "conditions": ["g3_3", "g2_5"],  "desc": "IF sensitif AND kemerahan THEN sensitif reaktif"},
        ],
        "cards": [
            {
                "icon":  "🛡️",
                "title": "Skin Barrier",
                "body":  "Kulit sensitif umumnya memiliki skin barrier yang terganggu sehingga iritan lebih mudah masuk dan menyebabkan reaksi.",
            },
            {
                "icon":  "🧪",
                "title": "Patch Test Dulu!",
                "body":  "Selalu lakukan patch test 24–48 jam sebelum mencoba produk baru untuk menghindari reaksi alergi.",
            },
        ],
        "ingredients_good": ["Centella Asiatica", "Ceramide", "Allantoin", "Panthenol", "Oat Extract", "Aloe Vera", "Zinc Oxide"],
        "ingredients_bad":  ["Fragrance/Parfum", "Alkohol Denat", "Essential Oil", "Retinol (awal)", "AHA/BHA konsentrasi tinggi", "Pewarna sintetis"],
        "routine": [
            {"step": "Micellar Water / Gentle Cleanser", "desc": "Hindari pembersih berbusa tinggi. Pilih yang pH-balanced dan bebas SLS."},
            {"step": "Calming Toner",            "desc": "Toner dengan Centella Asiatica atau Aloe Vera untuk menenangkan dan menghidrasi."},
            {"step": "Barrier Repair Serum",     "desc": "Serum dengan ceramide dan panthenol untuk memperkuat lapisan pelindung kulit."},
            {"step": "Rich Moisturizer",         "desc": "Krim pelembab yang memperkuat skin barrier dan mengurangi reaktivitas."},
            {"step": "Physical Sunscreen",       "desc": "Pilih sunscreen mineral (Zinc Oxide/Titanium Dioxide) yang lebih ramah untuk kulit sensitif."},
        ],
    },

    "oily": {
        "name":     "Kulit Berminyak (Oily Skin)",
        "subtitle": (
            "Kelenjar sebum kulitmu aktif memproduksi minyak berlebih. "
            "Perlu perawatan yang menyeimbangkan produksi sebum tanpa over-stripping."
        ),
        "rules": [
            {"id": "R13", "conditions": ["g1_1", "g3_2"], "desc": "IF berminyak AND pori besar THEN oily skin"},
            {"id": "R14", "conditions": ["g1_1", "g2_2"], "desc": "IF berminyak AND komedo THEN oily skin"},
            {"id": "R15", "conditions": ["g1_1"],          "desc": "IF berminyak berlebih THEN oily skin"},
        ],
        "cards": [
            {
                "icon":  "✨",
                "title": "Silver Lining",
                "body":  "Kulit berminyak cenderung lebih lambat keriput! Sebum alami memberikan lapisan perlindungan ekstra dan menjaga kelembaban.",
            },
            {
                "icon":  "⚖️",
                "title": "Jangan Over-Strip",
                "body":  "Terlalu sering cuci muka justru memicu kulit memproduksi lebih banyak minyak sebagai kompensasi.",
            },
        ],
        "ingredients_good": ["Niacinamide", "Salicylic Acid", "Zinc", "Clay/Kaolin", "Retinol", "BHA", "Witch Hazel"],
        "ingredients_bad":  ["Minyak berat (coconut oil)", "Petrolatum tebal", "Heavy cream", "Alkohol berlebihan"],
        "routine": [
            {"step": "Foaming Cleanser (2x sehari)", "desc": "Pembersih busa ringan untuk mengangkat kelebihan sebum tanpa merusak barrier."},
            {"step": "Balancing Toner",          "desc": "Toner mengandung niacinamide atau witch hazel untuk mengecilkan tampilan pori."},
            {"step": "Serum Niacinamide 10%",    "desc": "Mengontrol produksi minyak secara efektif sekaligus menyamarkan pori."},
            {"step": "Oil-Free Gel Moisturizer", "desc": "Jangan lewatkan pelembab! Pilih yang berbahan dasar air dan non-komedogenik."},
            {"step": "Matte Sunscreen",          "desc": "Sunscreen gel atau fluid yang tidak meninggalkan rasa berminyak."},
        ],
    },
}


# ── FORWARD CHAINING ENGINE ──────────────────────────────────
class ExpertEngine:
    """
    Mesin inferensi sistem pakar menggunakan metode Forward Chaining.
    Fakta (gejala) yang dipilih user dicocokkan dengan basis aturan
    untuk menghasilkan diagnosis dan rekomendasi.
    """

    def _fire_rules(self, facts: set) -> dict:
        """
        Evaluasi semua rule terhadap fakta yang ada.
        Kembalikan skor tiap diagnosis dan rule yang aktif.
        """
        scores     = {}
        fired      = []

        for diag_key, diag in KNOWLEDGE_BASE.items():
            score = 0
            for rule in diag["rules"]:
                if all(c in facts for c in rule["conditions"]):
                    score += len(rule["conditions"])
                    fired.append({
                        "rule_id": rule["id"],
                        "desc":    rule["desc"],
                        "diag":    diag["name"],
                    })
            if score > 0:
                scores[diag_key] = score

        return scores, fired

    def _confidence(self, scores: dict, top_key: str) -> int:
        """Hitung tingkat keyakinan diagnosis utama (0–95%)."""
        total = sum(scores.values())
        if total == 0:
            return 0
        raw = (scores[top_key] / total) * 100
        return min(95, round(raw))

    def evaluate(self, facts: set) -> dict:
        """
        Jalankan forward chaining dan kembalikan hasil lengkap.

        Parameters
        ----------
        facts : set of str — kode gejala yang dipilih user (mis. {'g1_1', 'g2_2'})

        Returns
        -------
        dict — diagnosis, confidence, detail, ingredients, routine, rule trace
        """
        if not facts:
            return {"error": "Tidak ada gejala yang dipilih."}

        scores, fired_rules = self._fire_rules(facts)

        if not scores:
            # Fallback jika tidak ada rule yang cocok
            top_key = "dry"
            confidence = 30
        else:
            top_key    = max(scores, key=scores.get)
            confidence = self._confidence(scores, top_key)

        diag = KNOWLEDGE_BASE[top_key]

        # Rule trace — hanya rule yang relevan dengan diagnosis utama
        relevant_rules = [r for r in fired_rules if r["diag"] == diag["name"]]

        return {
            "diagnosis":        top_key,
            "name":             diag["name"],
            "subtitle":         diag["subtitle"],
            "confidence":       confidence,
            "cards":            diag["cards"],
            "ingredients_good": diag["ingredients_good"],
            "ingredients_bad":  diag["ingredients_bad"],
            "routine":          diag["routine"],
            "fired_rules":      relevant_rules,
            "all_scores":       scores,
        }
