import socket
import sys
messaggio = sys.argv[1]
s = socket.socket()
s. settimeout (2)
indirizzo = '127.0.0.1'
porta = 6364
s. connect((indirizzo, porta))
s.sendal1(messaggio.encode())
risposta = s.recv(1024)
print(risposta.decode())
s. close ()
