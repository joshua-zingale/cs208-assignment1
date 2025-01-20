from flask import Flask, send_file
import os

try:
    break_file = os.environ['BREAK_FILE'] == "TRUE"
except:
    break_file = False

app = Flask(__name__)

@app.route("/")
def download_file():
    if break_file:
        return send_file("./mydata_corrupted.txt", as_attachment = True, download_name="mydata_client_copy.txt")
    else:
        return send_file("./mydata.txt", as_attachment = True, download_name="mydata_client_copy.txt")

@app.route("/checksum.txt")
def download_checksum():
    return send_file("./checksum.txt", as_attachment = True)