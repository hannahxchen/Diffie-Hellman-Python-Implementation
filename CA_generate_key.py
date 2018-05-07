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


file1=open("privatekey1.txt","w")
file2=open("publickey1.txt","w")
file3=open("privatekey2.txt","w")
file4=open("publickey2.txt","w")

file1.write(privatekey1.exportKey())
file2.write(publickey1.exportKey())
file3.write(privatekey2.exportKey())
file4.write(publickey2.exportKey())
file1.close()
file2.close()
file3.close()
file4.close()

print "Finish genrating key pairs"
