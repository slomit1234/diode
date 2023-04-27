import os

filename = "test.txt"
filesize = 100 * 1024 * 1024 # 100 MB

with open(filename, "wb") as f:
    f.write(os.urandom(filesize))
