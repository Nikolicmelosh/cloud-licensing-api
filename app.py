from flask import Flask, request, jsonify
import sqlite3
import datetime

app = Flask(__name__)
DB = "database.db"

# Initialize the database (only once)
def init_db():
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS licenses (
                key TEXT PRIMARY KEY,
                activated BOOLEAN DEFAULT 0,
                expires TEXT,
                hwid TEXT
            )
        ''')
        # Add sample key
        c.execute("INSERT OR IGNORE INTO licenses (key, expires) VALUES (?, ?)",
                  ("ABC123-XYZ789", "2025-12-31"))
        conn.commit()

@app.route('/verify', methods=['GET'])
def verify():
    key = request.args.get('key')
    hwid = request.args.get('hwid', '')

    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute("SELECT key, activated, expires, hwid FROM licenses WHERE key = ?", (key,))
        row = c.fetchone()
        if not row:
            return jsonify({'status': 'error', 'message': 'Invalid key'}), 400

        key, activated, expires, db_hwid = row
        now = datetime.datetime.utcnow().date()

        if db_hwid and db_hwid != hwid:
            return jsonify({'status': 'error', 'message': 'Key already bound to another device'}), 403

        if datetime.datetime.strptime(expires, "%Y-%m-%d").date() < now:
            return jsonify({'status': 'error', 'message': 'Key expired'}), 403

        if not db_hwid:
            c.execute("UPDATE licenses SET activated = 1, hwid = ? WHERE key = ?", (hwid, key))
            conn.commit()

        return jsonify({'status': 'success', 'message': 'Valid key'}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
