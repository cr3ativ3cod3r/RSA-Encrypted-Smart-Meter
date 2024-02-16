import socket
import time

HOST = '192.168.148.194'  
PORT = 9999

d=2150096105574765275565253080728134461818283538465091213139489190228230565438910995975697840909546354787766196691225386423585219924380226667961609237941713
n=6910782171213996658397253121710630123795235324197483219005527369298065059694620267925472189305202037262152652525687783466320955431741311010423968405213211

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024) 
        #print() 
        try:
            a=int(str(data.decode('utf-8')))
            t = pow(a,d,n)
            f = t.to_bytes(17,'big')
            a=f.decode('ascii').strip()
            b=a[9::]
            print(f.decode('ascii').strip())
            time.sleep(1)
            file = open('javascript file for refreshing data in HTML website.js','w')
            file.write("""
var voltage = document.querySelector('#voltage');
var button = document.querySelector('#button');
const text = document.querySelector('#dynamic-text');

button.addEventListener('click', function() {
    var voltages = """+b+""";
    voltage.innerHTML = voltages;
})
            """
            )

            file.close()

        except:
            pass