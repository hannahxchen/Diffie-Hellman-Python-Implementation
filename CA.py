import socket
from Crypto import Random
from Crypto.PublicKey import RSA

rng1 = Random.new().read
RSAkey1=RSA.generate(1024,rng1)

privatekey1=RSAkey1
publickey1=RSAkey1.publickey()
##print(privatekey.exportKey()) #export under the 'PEM' format
##print(publickey.exportKey())

rng2 = Random.new().read
RSAkey2=RSA.generate(1024,rng2)

privatekey2=RSAkey2
publickey2=RSAkey2.publickey()

mydict1={'Client':privatekey1.exportKey(), 'Server':publickey1.exportKey()}
mydict2={'Client':publickey2.exportKey(), 'Server':privatekey2.exportKey()}

CA=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket created"

CA.bind(('localhost',9999))
print "Socket bind complete"
CA.listen(5) #socket listens for connections, maximum 5 connections
print "Server is now listening..."

while True:
    connection, address = CA.accept()
    print "Connected with "+address[0]

    user=connection.recv(1024)
    for name, key1 in mydict1.items():
        if name == user:
            connection.sendall(key1)
            print "key1 sended"
        else:
            print "Access denied!"
            connection.close()

    for name, key2 in mydict2.items():
        if name == user:
            connection.sendall(key2)
            print "key2 sended"
        else:
            print "Access denied!"
            connection.close()
            
            
    CA.close()

    
