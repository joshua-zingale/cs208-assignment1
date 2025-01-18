import requests
import hashlib
import os

try:
    URL = os.environ['SERVER_URL']
except:
    URL = "http://127.0.0.1:5000"

# Get checksum
try:
    checksum = requests.get(f"{URL}/checksum.txt").text
except Exception as e:
    print(f"Could not download checksum:")
    raise e

# Get file
try:
    file_text = requests.get(URL).text
except Exception as e:
    print(f"Could not download file:")
    raise e

# Compare file against checksum
if hashlib.md5(str.encode(file_text)).hexdigest() == checksum:

    # Write file if checksum matches
    with open("mydata_client_copy.txt", "w") as f:
        f.write(file_text)
    # File has been downloaded, validated, and saved. The file's contents are
    print(file_text)
else:
    print("Downloaded file did not match the checksome and was discarded.")


