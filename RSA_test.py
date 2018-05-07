from Crypto.PublicKey import RSA
import hashlib

file=open("privatekey1.txt","r")
RSApr=file.read()
file.close()
##    print "Client RSA private key:"+RSApr
RSApr=RSA.importKey(RSApr)

file=open("publickey1.txt","r")
RSApb=file.read()
file.close()
##    print "Server RSA public key:"+RSApb
RSApb=RSA.importKey(RSApb)

A="abcdef12345678"
hashA=hashlib.sha256(str(A)).digest()
print "hashA:"+ hashA

signA=RSApb.encrypt(hashA, 32)
print "signA:"+ signA[0]

DcryptedsignA=RSApr.decrypt(signA[0])
print "decrypted:"+ DcryptedsignA
