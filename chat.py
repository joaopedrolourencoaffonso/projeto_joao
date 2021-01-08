from socket import *;
import threading

serverName = '192.168.0.113';
serverPort = 12000;
serverSocket = socket(AF_INET, SOCK_STREAM); 
serverSocket.bind(('', serverPort));
serverSocket.listen(2);


bserverName = '192.168.0.113';
bserverPort = 11000;
clientSocket = socket(AF_INET, SOCK_STREAM); 
clientSocket.connect((bserverName, bserverPort));


def readmessage():
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024);
        sentence = sentence.decode("utf-8");
        print(sentence);
        connectionSocket.close();

threadObj = threading.Thread(target=readmessage)
threadObj.start()

def sendmessage():
    while True:
        sentence = input('Input lowercase sentence:'); 
        sentence = bytes(sentence, 'utf-8');
        clientSocket.send(sentence);

threadObj = threading.Thread(target=sendmessage)
threadObj.start()

print("The server is ready to receive");

while True:
    continue;

#ConnectionAbortedError: [WinError 10053] Uma conexão estabelecida foi anulada pelo software no computador host
