# importing the socket library.
import mimetypes
from socket import *
# set the port to 7000.
serverPort = 7000
# creating the socket and initialize it.
serverSocket = socket(AF_INET, SOCK_STREAM)
# defines a relationship between the socket and theIP address that are available on the host.
serverSocket.bind(('192.168.1.158', serverPort))# 192.168.1.158 is the IP address vresion 4 of my PC
# opens the bound port so the socket can then start receiving connections from clients.
serverSocket.listen(1)
# print a work done message.
print ("The server is ready to receive")

while True:
    # server waits on accept() for incoming requests, new socket created on return
    connectionSocket, addr = serverSocket.accept()
    # read bytes from socket (but not address as in UDP)
    sentence = connectionSocket.recv(1024).decode()
    # send the web style by the response.
    if sentence[sentence.find("Get /") + len("GET /"):sentence.find(" HTTP")].strip() == "/1":
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n")
        connectionSocket.send(b"Content-Type: text/html; charset=ISO-8859-1\r\n\r\n")
        connectionSocket.send('''<html>
                                <head> 
                                <title> ENCS434 WebServer</title>
                                </head>
                                <body>
                                <h1 style=font-weight: bold; font-size: 50px;>Maen Khdour 1171944</h1>
                                <br>
                                <h1 style=font-weight: bold; font-size: 50px;>Mohammad Bassam 1172348</h1>
                                <br>
                                <p style=font-size: 30px;>Welcome to our course <span style=color:green>Computer Networks</span></p>
                                <h3>The IP : {}</h3>
                                <h3>The Port Number : {}</h3>
                                </body>
                                </html>'''.format(addr[0],addr[1]).encode())

    if sentence[sentence.find("Get /") + len("GET /"):sentence.find(" HTTP")].strip() == "/2":
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n")
        connectionSocket.send(b"Content-Type: text/html; charset=ISO-8859-1\r\n\r\n")
        htmlFile=open("D:/University/NETWORK/Proj1/index.html",'rb',1024).read()
        connectionSocket.send(htmlFile)

    if sentence[sentence.find("Get /") + len("GET /"):sentence.find(" HTTP")].strip() == "/3":
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n")
        connectionSocket.send(b"Content-Type:image/png; charset=ISO-8859-1\r\n\r\n")
        img=open("D:/University/NETWORK/Proj1/Image.jpeg",'rb',1024).read()
        connectionSocket.send(img)

    # print(sentence[sentence.find("Get /") + len("GET /"):sentence.find(" HTTP")].strip())
    # print the IP and port number of the client on command line window.
    print(sentence)
# close the connection of the socket.
connectionSocket.close()
