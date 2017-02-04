#!/usr/bin/env python

import socket
##import RPi.GPIO as GPIO

server = socket.socket()
host = socket.gethostbyaddr('192.168.1.104')
port = 5150
status = 'nominal'
##GPIO.setmode(GPIO.BOARD)
lights_pin = 12
##GPIO.setup(lights_pin, GPIO.OUT)
##GPIO.output(lights_pin,0)
light_status = False;

server.connect((host,port))
data = server.recv(1024)
print(bytes.decode(data))
while True:
    data = input('Enter Text')
    server.send(str.encode(data))
    data = server.recv(1024)
    print('Recived from server',bytes.decode(data))
    if(bytes.decode(data) == 'exit'):
       break
    if(bytes.decode(data) == 'status'):
        server.send(str.encode(status))
    if(bytes.decode(data) == 'lights;'):
        if(not light_status):
         ##   GPIO.output(lights_pin,True)
            print("on")
            light_status =True
        else:
          ##  GPIO.output(lights_pin,False)
            print("off")
            light_status = False
            
        
        
print('Closing Connection')
server.close()
