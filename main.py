import requests
import time
from config import API_KEY, API_SECRET, BASE_URL

HEADERS = {
    'APCA-API-KEY-ID': API_KEY,
    'APCA-API-SECRET-KEY': API_SECRET
}

def get_account():
    url = f"{BASE_URL}/v2/account"
    try:
        r = requests.get(url, headers=HEADERS)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def is_market_open():
    url = f"{BASE_URL}/v2/clock"
    try:
        r = requests.get(url, headers=HEADERS)
        r.raise_for_status()
        return r.json().get('is_open', False)
    except Exception as e:
        print(f"❌ Error checking market: {e}")
        return False

def run_bot():
    print("🔄 Starting Aurum Core bot...")
    if not is_market_open():
        print("🚫 Market is closed.")
        return

    account = get_account()
    if account:
        print(f"✅ Connected to Alpaca — Buying Power: ${account.get('buying_power', 'N/A')}")
    else:
        print("❌ Failed to get account info.")

    while True:
        print("📡 Scanning market... (this is a placeholder)")
        time.sleep(30)

if __name__ == "__main__":
    run_bot()
