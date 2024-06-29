import socket
from datetime import datetime
print('''\033[1;31m
╦╔═╔═╗╦ ╦╦ ╔═╗╔═╗╔═╗╔═╗╦═╗ 
╠╩╗║╣ ╚╦╝║ ║ ║║ ╦║ ╦║╣ ╠╦╝ 
\033[m\033[1;34m╩ ╩╚═╝ ╩ ╩═╝╚═╝╚═╝╚═╝╚═╝╩╚═\033[m''')

timenow = datetime.now()
host = 'localhost'  # Ip do server
port = 8082 # porta do server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)
conn, docl = sock.accept()

if docl:
    print('\033[1;32m='*42)
    print(f'| servidor iniciado na maquina {docl[0]} |')
    print('='*42)
    print('\033[m')
while True:
        
    Menss_Rec = str(conn.recv(1024), 'utf-8')

    if Menss_Rec:
        print(f'[{timenow.strftime('%d/%m/%Y, %H:%M:%S')}]\033[1;31m -> \033[m{Menss_Rec}')
    