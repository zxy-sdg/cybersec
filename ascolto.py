import socket
server_socket = socket. socket()
host = '127.0.0.1'
port = 6364
server_socket.bind((host, port))
server_socket.listen(1)
f = open('logfile.txt','w')
f.write(f"Server listening on {host}:{port} \n")
for i in range(1000):
    conn, addr = server_socket.accept()
    f.write(f"Connected by {addr} \n")
    richiesta = 'SHUTDOWN'
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            richiesta = data. decode()
            if richiesta == 'SHUTDOWN':
                break
            risposta = f"Ho ricevuto il tuo messaggio: {richiesta} \n"
            f. write(risposta)
            conn.sendall(risposta.encode())
        if richiesta == 'SHUTDOWN':
            break
    finally:
        conn.close()
f. close()
server_socket.close()
