import time
import socket
import json

def complete_package_size(package, size):
    package += '$' * (size - len(package))
    return package

def recive_data(s, in_q):
    running = True
    while running:
        data = s.recv(128)

        if not data:
            break
        
        in_q.append(data.decode().replace('$', ''))

        if data.decode() == 'quit':
            running = False

def send_data(s, out_q):
    running = True
    while running:

        if out_q.empty():
            time.sleep(0.05)
        else:
            data = out_q.get()
            s.send(complete_package_size(json.dumps(data), 128).encode())
            time.sleep(0.05)
            if data == 'quit':
                running = False