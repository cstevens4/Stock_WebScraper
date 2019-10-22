from socket import *
serverName = '10.220.112.74'
serverPort =  12345
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = input('Input lowercase sentence:')
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(1024)
print ('From Server: ', modifiedMessage.decode())
clientSocket.close()
