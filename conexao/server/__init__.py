import socket
def connectServer(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    conn, docl = sock.accept()
    if docl:
        print(f'servidor iniciado na maquina {docl}')
    while True:
        
        Menss_Rec = conn.recv(1024)

        if Menss_Rec:
            print(str(Menss_Rec))
    
connectServer('localhost',8082)