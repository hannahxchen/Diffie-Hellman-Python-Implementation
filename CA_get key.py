import socket

CA= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    CA.connect(('localhost', 9999))
    username=raw_input("Enter your name:")
    CA.send(username)

    key1=CA.recv(1024)
    key2=CA.recv(1024)

    if username=="Client":
        file1=open("privatekey1.txt","w")
        file2=open("publickey2.txt","w")
    if username=="Server":
        file1=open("publickey1.txt","w")
        file2=open("privateckey2.txt","w")
    else:
        break
        
    file1.write(key1)
    file2.write(key2)
    file1.close()
    file2.close()
    
    print "Get key1:"+key1
    print "Get key2:"+key2

    CA.close()
