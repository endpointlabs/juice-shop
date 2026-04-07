import subprocess
import pickle
import hashlib
import sqlite3
import os


password = "admin123"
secret = "my_secret_key_12345"
token = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

user = input("Enter username: ")
cursor.execute("SELECT * FROM users WHERE name = '" + user + "'")

cmd = input("Enter command: ")
subprocess.call(cmd, shell=True)
os.system("rm -rf " + cmd)
os.popen(cmd)

data = open("data.pkl", "rb").read()
obj = pickle.loads(data)

expr = input("Enter expression: ")
result = eval(expr)

h = hashlib.md5(b"password")
h2 = hashlib.sha1(b"token")

f = open("/tmp/debug.log", "w")
f.write(password)

assert user == "admin"

exec("print('hello')")
