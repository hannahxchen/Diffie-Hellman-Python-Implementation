import socket
import random
import math
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
import hashlib
##import os

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    server.connect(('localhost', 8080))

## Log in to server//////////////////////////////////////////
    ID=raw_input("Enter your ID:")
    server.send(ID)

    challenge=server.recv(1024)
    password=raw_input("Enter your password:")
    key=hashlib.sha256(password).digest() #generate a 32-byte key from password
    IV = 16 * '\x00'
    encryptor=AES.new(key, AES.MODE_CFB, IV)
    response=encryptor.encrypt(challenge)
    ##print "Response:"+response
    server.send(response)
    ack=server.recv(1024)
    print ack
    if ack == "Incorrect password!":
        break
##    os.system('pause')

## Generate session key/////////////////////////////////////
    g=5
    p=23
    server.send(str(g))
    server.send(str(p))

##    a=random.randint(10,20)
    a=6
    print "secret value a:"+str(a)
    A=(g**a)%p #g^a mod(p)
    server.send(str(A))
    hashA=hashlib.sha256(str(A)).digest() 

    file=open("publickey1.txt","r")
    RSAkey1=file.read()
    file.close()
##    print "Client RSA private key:"+RSAkey1
    RSAkey1=RSA.importKey(RSAkey1)
    
    signA=RSAkey1.encrypt(hashA, 32)
    server.send(signA[0])
    print "g:"+str(g)
    print "p:"+str(p)
    print "A:"+str(A)
    print "signA:"+signA[0]
    print "Send g, p, g^a mod(p), sign(A) to Server"

    file=open("privatekey2.txt","r")
    RSAkey2=file.read()
    file.close()
##    print "Client RSA public key:"+RSAkey2
    RSAkey2=RSA.importKey(RSAkey2)

    B=server.recv(1024)
    signB=server.recv(1024)
    print "Receive g^b mod(p), sign(B) from Server"
    print "B:"+str(B)
    print "signB"+signB

##    os.system('pause')

    hashB=hashlib.sha256(B).digest()
    checkHash=RSAkey2.decrypt(signB)
    print "hashB:"+hashB
    print "CheckHashB:"+checkHash

    if hashB == checkHash:
        print "CheckHash Sucess!"

        sessionKey=str((int(B)**a)%p)
        print "Generate session key:"+ sessionKey
    else:
        print "CheckHash Failed!"
        break
##    os.system('pause')

    encryptedEMR=server.recv(1024)
    print "Recieve encrypted EMR from Server"
    
    sessionKey=hashlib.sha256(sessionKey).digest()
    decryptor=AES.new(sessionKey,AES.MODE_CFB,IV)
    decryptedEMR=decryptor.decrypt(encryptedEMR)
    print "Decrypted EMR:"+decryptedEMR
    break
    



