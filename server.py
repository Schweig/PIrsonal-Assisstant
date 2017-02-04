#!/usr/bin/env python

import socket
import speech_recognition as sr



server = socket.socket()
host = '192.168.1.106'
port = 5150
server.bind((host,port))
server.listen(5)
print('listenting for a client')
client,addr = server.accept()
print('Accepted connection from',addr)
client.send(str.encode('Welcome'))
def callback(recognizer, audio):                          # this is called from the background thread
    try:
        value = r.recognize_google(audio)
        print("You said " + value)# received audio data, now need to recognize it
        if('lights' in value):
            print('lights')
            client.send(str.encode('lights'))
        
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
r = sr.Recognizer()
m = sr.Microphone()
try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    stop_listening = r.listen_in_background(m,callback)
    
    while True:
        data = client.recv(1024)
        client.send(data)
        if(bytes.decode(data) == 'exit'):
            break
        else:
            print('Received data from client:',bytes.decode(data))
            
except KeyboardInterrupt:
    pass
print('Cleaning up')
stop_listening()
client.send(str.encode('exit'))
client.close()
