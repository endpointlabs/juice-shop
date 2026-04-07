import os
import subprocess
import hashlib
import pickle
import yaml
import sqlite3
import tempfile


# B608 - SQL Injection (High)
def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


# B602 - Subprocess with shell=True (High)
def run_command(user_input):
    result = subprocess.call(user_input, shell=True)
    return result


# B301 - Pickle deserialization (High)
def load_data(data):
    return pickle.loads(data)


# B506 - YAML unsafe load (High)
def parse_config(config_str):
    return yaml.load(config_str)


# B303 - Use of insecure MD5 hash (High)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# B605 - Start process with shell (High)
def ping_host(host):
    os.system("ping -c 3 " + host)


# B108 - Hardcoded temp directory (Medium)
def write_temp():
    with open('/tmp/secrets.txt', 'w') as f:
        f.write('secret_key=abc123')


# B105 - Hardcoded password (High)
DB_PASSWORD = "SuperSecret123!"
API_KEY = "sk-proj-1234567890abcdef"


# B201 - Flask debug mode (High)
def start_app():
    from flask import Flask
    app = Flask(__name__)
    app.run(debug=True)


# B104 - Bind to all interfaces (Medium)
def start_server():
    from flask import Flask
    app = Flask(__name__)
    app.run(host='0.0.0.0')


# B307 - Use of eval (High)
def calculate(expression):
    return eval(expression)


# B324 - Use of insecure SHA1 hash (High)
def hash_token(token):
    return hashlib.sha1(token.encode()).hexdigest()
