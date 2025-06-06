import requests

def test_license_key(key):
    url = "https://cloud-licensing-api.onrender.com/verify"
    params = {"key": key}
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            print(f"✅ Key '{key}' is valid.")
        else:
            print(f"❌ Key '{key}' is invalid. Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    key = input("Enter license key to test: ").strip()
    test_license_key(key)
