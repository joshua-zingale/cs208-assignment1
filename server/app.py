from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def download_file():
    return send_file("./mydata.txt", as_attachment = True, download_name="mydata_client_copy.txt")

@app.route("/checksum.txt")
def download_checksum():
    return send_file("./checksum.txt", as_attachment = True)