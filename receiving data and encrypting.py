import network
import socket
from machine import UART
import machine
import esp
import gc
import time
import os


gc.collect()
esp.osdebug(None)


wlan = network.WLAN(network.STA_IF)
wlan.active(True)


w = "Galaxy A73 5G 5354" #wifi name
p = "oqry3557" #wfi password


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    if wlan.isconnected() == False:
        wlan.connect(w,p)
except:
    print('Not connected, please check if the WiFi network is active')


while wlan.isconnected() == False:
    pass


print(f'Connected successfully to {w}')
#print(wlan.ifconfig()[0])

HOST = wlan.ifconfig()[0]
PORT = 9999


s.bind((HOST, PORT))
s.listen(5)


uart = UART(1, baudrate=9600, tx=17, rx=16)


n=6910782171213996658397253121710630123795235324197483219005527369298065059694620267925472189305202037262152652525687783466320955431741311010423968405213211
e=65537

while True:
  if uart.any():
    data = uart.read(8)  
    if data:
        pass
    else:
        data = b'Voltage : 0     '
  else:
    data = b'Voltage : 0'
  time.sleep(0.1)
  num = int.from_bytes(data,"big")
  x = pow(num,e,n)
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  html = str(x)
  conn.sendall(html)
  time.sleep(0.1)
  conn.close()