"""
🤖 Crypto Trading Bot Sederhana
================================
Bot ini mengambil harga crypto dari API CoinGecko (gratis, tanpa API key)
dan menggunakan strategi sederhana untuk memberi sinyal BUY/SELL/HOLD.

Strategi: Moving Average Crossover
- Jika harga naik di atas rata-rata → BUY
- Jika harga turun di bawah rata-rata → SELL
- Jika tidak ada sinyal jelas → HOLD
"""

import requests
import time
from datetime import datetime


# ==========================================
# PENGATURAN BOT
# ==========================================
COIN = "bitcoin"          # Coin yang ingin dipantau (bitcoin, ethereum, dll)
CURRENCY = "usd"          # Mata uang (usd, idr, dll)
INTERVAL = 60             # Cek harga setiap 60 detik
SHORT_WINDOW = 3          # Rata-rata jangka pendek (3 data terakhir)
LONG_WINDOW = 7           # Rata-rata jangka panjang (7 data terakhir)


# ==========================================
# FUNGSI AMBIL HARGA
# ==========================================
def get_price(coin, currency):
    """Mengambil harga terkini dari CoinGecko API."""
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin, "vs_currencies": currency}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data[coin][currency]
    except requests.exceptions.RequestException as e:
        print(f"❌ Gagal ambil harga: {e}")
        return None


# ==========================================
# FUNGSI HITUNG MOVING AVERAGE
# ==========================================
def moving_average(prices, window):
    """Menghitung rata-rata dari sejumlah data harga terakhir."""
    if len(prices) < window:
        return None
    return sum(prices[-window:]) / window


# ==========================================
# FUNGSI STRATEGI TRADING
# ==========================================
def get_signal(prices):
    """
    Menentukan sinyal trading berdasarkan Moving Average Crossover.
    
    Returns:
        str: "BUY", "SELL", atau "HOLD"
    """
    short_ma = moving_average(prices, SHORT_WINDOW)
    long_ma = moving_average(prices, LONG_WINDOW)

    if short_ma is None or long_ma is None:
        return "HOLD"  # Data belum cukup

    if short_ma > long_ma:
        return "BUY"
    elif short_ma < long_ma:
        return "SELL"
    else:
        return "HOLD"


# ==========================================
# FUNGSI TAMPILKAN STATUS
# ==========================================
def print_status(price, signal, prices):
    """Menampilkan informasi trading ke layar."""
    now = datetime.now().strftime("%H:%M:%S")
    short_ma = moving_average(prices, SHORT_WINDOW)
    long_ma = moving_average(prices, LONG_WINDOW)

    emoji = {"BUY": "🟢", "SELL": "🔴", "HOLD": "🟡"}

    print(f"\n{'='*45}")
    print(f"  🤖 CRYPTO TRADING BOT - {COIN.upper()}")
    print(f"{'='*45}")
    print(f"  ⏰ Waktu       : {now}")
    print(f"  💰 Harga       : ${price:,.2f}")
    
    if short_ma:
        print(f"  📈 MA Pendek   : ${short_ma:,.2f} (rata-rata {SHORT_WINDOW} data)")
    if long_ma:
        print(f"  📉 MA Panjang  : ${long_ma:,.2f} (rata-rata {LONG_WINDOW} data)")
    
    print(f"  {emoji[signal]} Sinyal      : {signal}")
    print(f"  📊 Data harga  : {len(prices)} titik terkumpul")
    print(f"{'='*45}")

    # Penjelasan sinyal
    if signal == "BUY":
        print("  ✅ MA pendek > MA panjang → Tren NAIK, pertimbangkan BELI")
    elif signal == "SELL":
        print("  ⚠️  MA pendek < MA panjang → Tren TURUN, pertimbangkan JUAL")
    else:
        print("  ⏳ Belum ada sinyal kuat, sebaiknya TAHAN posisi")


# ==========================================
# FUNGSI UTAMA (MAIN)
# ==========================================
def main():
    print("\n🚀 Memulai Crypto Trading Bot...")
    print(f"   Memantau  : {COIN.upper()}")
    print(f"   Interval  : setiap {INTERVAL} detik")
    print(f"   Strategi  : Moving Average Crossover")
    print(f"\n⚠️  PERINGATAN: Bot ini hanya untuk EDUKASI.")
    print(f"   Jangan gunakan sebagai saran investasi nyata!\n")
    
    prices = []  # Menyimpan riwayat harga

    while True:
        price = get_price(COIN, CURRENCY)

        if price:
            prices.append(price)
            signal = get_signal(prices)
            print_status(price, signal, prices)

        print(f"\n⏳ Menunggu {INTERVAL} detik untuk pengecekan berikutnya...")
        print("   (Tekan Ctrl+C untuk menghentikan bot)")
        
        try:
            time.sleep(INTERVAL)
        except KeyboardInterrupt:
            print("\n\n👋 Bot dihentikan. Sampai jumpa!")
            break


# ==========================================
# JALANKAN BOT
# ==========================================
if __name__ == "__main__":
    main()
