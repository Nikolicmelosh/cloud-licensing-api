import json
import os
import random
import string

LICENSE_FILE = "licenses.json"

def generate_license_key():
    # Format: XXXX-XXXX-XXXX (A-Z and 0-9)
    return '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(3))

def save_license_keys(keys):
    if os.path.exists(LICENSE_FILE):
        with open(LICENSE_FILE, "r") as f:
            licenses = json.load(f)
    else:
        licenses = {}

    for key in keys:
        licenses[key] = True

    with open(LICENSE_FILE, "w") as f:
        json.dump(licenses, f, indent=4)

def generate_bulk_keys(amount):
    keys = []
    for _ in range(amount):
        key = generate_license_key()
        keys.append(key)
    return keys

if __name__ == "__main__":
    try:
        amount = int(input("How many license keys do you want to generate? "))
        keys = generate_bulk_keys(amount)
        save_license_keys(keys)

        print("\n✅ Successfully generated and saved the following keys:\n")
        for key in keys:
            print(key)
    except Exception as e:
        print(f"❌ Error: {e}")

