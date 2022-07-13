import hashlib

data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)

data2 = 'hello world'.encode()
hash_object2 = hashlib.sha1()
hash_object2.update(data2)
hex_dig2 = hash_object2.hexdigest()
print(hex_dig2)
