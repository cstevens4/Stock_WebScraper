from socket import *
serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
      
while True:
     connectionSocket, addr = serverSocket.accept()
     print(addr)
     message = connectionSocket.recv(1024).decode()
     modifiedMessage = message.upper()
     connectionSocket.send(modifiedMessage.encode())                                                     
     connectionSocket.close()
