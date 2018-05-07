Main Concept
--------

Transferring Electronic Medical Records(EMR)using Diffie-Hellman Key Exchange & AES encryption


Concept Graph
--------

![](graph/concept-graph.JPG)


User Log in to Server
--------

![](graph/user-login-to-server.JPG)

Diffie-Hellman Key Exchange, Generate Session Key
--------

![](graph/key-exchange.JPG)

User Access EMR from Server
--------

![](graph/access-emr.JPG)


Environment
--------

Python 2.7


Required Packages:
--------

-pycrypto

-hashlib

How to Run:
--------

1. run CA.py to generate AES key pair
2. run Server.py & Client.py