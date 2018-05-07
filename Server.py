import socket
import random
import math
##import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
import hashlib

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket created"
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('localhost',8080))
print "Socket bind complete"
server.listen(5) #socket listens for connections, maximum 5 connections
print "Server is now listening..."

while True:
    connection, address = server.accept()
    print "Connected with "+address[0]

## Log in to server/////////////////////////////////////////////////
    data = connection.recv(1024)
    print "Receive ID:"+data

    challenge=Random.new().read(16)
    connection.sendall(challenge)

    response=connection.recv(1024)
##    print "Recieve response:"+response
    password="Abc1234"
    key=hashlib.sha256(password).digest()
    IV = 16 * '\x00'
    decryptor=AES.new(key, AES.MODE_CFB, IV)
    plain=decryptor.decrypt(response)
##    print "decrypt response:"+plain

    if plain == challenge:
        connection.sendall("Welcome!")
        print "Client logged in"
    else:
        connection.sendall("Incorrect password!")
        break

## Generate session key////////////////////////////////////////////
    g=connection.recv(1024)
    p=connection.recv(1024)
    A=connection.recv(1024)
    signA=connection.recv(1024)
    print "Recieve g, p, g^a mod(p), sign(A) from Client"
    print "g:"+str(g)
    print "p:"+str(p)
    print "A:"+str(A)
    print "signA:"+signA

##    os.system('pause')

    file=open("privatekey1.txt","r")
    RSAkey1=file.read()
    file.close()
##    print "Server RSA public key:"+RSAkey1
    RSAkey1=RSA.importKey(RSAkey1)
    
    checkHash=RSAkey1.decrypt(signA)
    hashA=hashlib.sha256(A).digest()

    file=open("publickey2.txt","r")
    RSAkey2=file.read()
    file.close()
##    print "Server RSA private key:"+RSAkey2
    RSAkey2=RSA.importKey(RSAkey2)

    print "hashA:"+hashA
    print "CheckHashA:"+checkHash
    
    if hashA==checkHash:
        print "CheckHash Success!"

##        os.system('pause')
##        b=random.randint(5, 10)
        b=15
        B=(int(g)**b)%int(p) #g^b mod(p)
        print "secret value b:"+str(b)
        
        hashB=hashlib.sha256(str(B)).digest()
        signB=RSAkey2.encrypt(hashB, 32)
        connection.sendall(str(B))
        connection.sendall(signB[0])
        print "B:"+str(B)
        print "signB:"+signB[0]
        print "Send g^b mod(p), sign(B) to Client"

        sessionKey=str((int(A)**b)%int(p))
        print "Generate session key:"+ sessionKey
    else:
        print "CheckHash failed!"
        break
##    os.system('pause')
        
    file=open("EMR.txt","r")
    EMRfile=file.read()
    file.close()

    sessionKey=hashlib.sha256(sessionKey).digest()
    encryptor=AES.new(sessionKey, AES.MODE_CFB, IV)
    encryptedEMR=encryptor.encrypt(EMRfile)

    connection.send(encryptedEMR)
    print "Send encrypted EMR to Client"
    print "Encrypted file:"+encryptedEMR
    break   

connection.close()   
server.close()
    
    
    

