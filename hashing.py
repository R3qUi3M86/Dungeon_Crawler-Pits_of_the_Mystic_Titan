import hashlib

md5_hash = hashlib.md5()

md5_hash.update("7QcuSs2ihej nic bo gupiimage".encode())

print(md5_hash.hexdigest())