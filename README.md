# 🤖 Crypto Trading Bot

Bot trading crypto sederhana berbasis Python yang menggunakan strategi **Moving Average Crossover** untuk menghasilkan sinyal BUY / SELL / HOLD secara otomatis.

> ⚠️ **Disclaimer**: Project ini hanya untuk tujuan **edukasi**. Bukan saran investasi.

---

## ✨ Fitur

- 📡 Harga real-time dari [CoinGecko API](https://www.coingecko.com/) (gratis, tanpa API key)
- 📈 Strategi Moving Average Crossover
- 🟢 Sinyal BUY / 🔴 SELL / 🟡 HOLD otomatis
- 🔄 Update otomatis setiap 60 detik
- 👶 Cocok untuk pemula Python

---

## 🚀 Cara Menjalankan

### 1. Clone repository
```bash
git clone https://github.com/farenzar/crypto-trading-bot.git
cd crypto-trading-bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan bot
```bash
python bot.py
```

---

## ⚙️ Pengaturan

Buka file `bot.py` dan ubah bagian ini sesuai keinginan:

```python
COIN = "bitcoin"    # Ganti dengan: ethereum, dogecoin, solana, dll
CURRENCY = "usd"    # Ganti dengan: idr, eur, dll
INTERVAL = 60       # Interval pengecekan (dalam detik)
SHORT_WINDOW = 3    # Jendela rata-rata pendek
LONG_WINDOW = 7     # Jendela rata-rata panjang
```

---

## 📊 Cara Kerja Strategi

```
MA Pendek (3 data) > MA Panjang (7 data)  →  Sinyal BUY  🟢
MA Pendek (3 data) < MA Panjang (7 data)  →  Sinyal SELL 🔴
MA Pendek = MA Panjang                    →  Sinyal HOLD 🟡
```

**Moving Average** adalah rata-rata harga dalam periode tertentu. Ketika rata-rata jangka pendek melewati rata-rata jangka panjang ke atas, itu pertanda tren naik (bullish).

---

## 📁 Struktur Project

```
crypto-trading-bot/
├── bot.py            # File utama bot
├── requirements.txt  # Library yang dibutuhkan
└── README.md         # Dokumentasi ini
```

---

## 🛠️ Tech Stack

- **Python 3.x**
- **requests** - untuk mengambil data dari API

---

## 📜 Lisensi

MIT License - bebas digunakan dan dimodifikasi.
