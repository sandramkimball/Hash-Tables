import hashlib

n = 10
key = b'string' #b = bite array
key2 = 'string'.encode()
#a string in python is an obj with meta data

index = hash(key) % 8 #(capacity)
print(index)

for i in range(n):
    #what do you predict will happen, scientist?
    print(hash(key)) #python hash func salts the value
    
    print(hashlib.sha256(key).hexdigest())