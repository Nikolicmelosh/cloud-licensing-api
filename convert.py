import sqlite3

DB = "database.db"

keys = {
    "18PG-6YL0-XV0F": True,
    "6OM6-9CDB-B19Y": True,
    "PPP9-AWI5-SKDW": True,
    "I5R6-LOV7-9ZH4": True,
    "XDFH-ZV43-2BER": True,
    "G8IY-IVQI-R5B6": True,
    "I69Q-IFIL-93TH": True,
    "QZXL-ML7F-Z1OQ": True,
    "SY41-GVDW-L37A": True,
    "YR55-9MFD-K842": True,
    "UKQA-LBNM-I0HS": True,
    "37X0-79GV-UBJB": True,
    "GMZJ-38IE-UVMN": True,
    "BYJ0-Q5NZ-96SY": True,
    "9SRX-QE26-6WK0": True,
    "QUMO-V989-ZFE7": True,
    "9YYY-GZBG-V1JQ": True,
    "V3U5-0QDR-UNCH": True,
    "L3ST-GSKG-C0R0": True,
    "9KWF-XC30-CDF5": True,
    "2R4N-M9A5-ZIKV": True,
    "VVKE-VOP6-S5IE": True,
    "7N9C-ZRUV-R21E": True,
    "2ILI-90W4-68BK": True,
    "IRP1-OK04-I0CM": True,
    "6VB8-QE29-YNPK": True,
    "5T58-TGMK-Y843": True,
    "DCO4-NWV4-KBZZ": True,
    "1O11-CIKC-2WXZ": True,
    "7SHD-V92W-F7LX": True
}

with sqlite3.connect(DB) as conn:
    c = conn.cursor()
    for key in keys.keys():
        # set expiration far in the future or your desired date
        c.execute("INSERT OR IGNORE INTO licenses (key, activated, expires) VALUES (?, ?, ?)",
                  (key, 0, "2099-12-31"))
    conn.commit()

print("Keys imported.")
