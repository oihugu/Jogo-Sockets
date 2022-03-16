from http import client
import socket, threading, queue, time

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 5000  # Port to listen on (non-privileged ports are > 1023)

def complete_package_size(package, size):
    package += '$' * (size - len(package))
    return package

def handle_client(client_socket, player_id, in_q, out_q):
    running = True
    size = 128
    client_socket.sendall(f'{player_id}'.encode())
    print(f'player{player_id} has connected')

    while running:
        request = client_socket.recv(size)
        r_ = request.decode().replace('$', '')
        out_q.put(r_)
        if not(in_q.empty()):
            client_socket.sendall(complete_package_size(in_q.get(), size).encode())

        if r_ == 'quit' or r_ == '':
            return

    client_socket.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    player = 1
    io = {'p1': {
                 'out': queue.Queue()
                },
          'p2': {
                 'out': queue.Queue()
                }
          }

    s.bind((HOST, PORT))
    s.listen()
    
    while player < 3:
        other_player = 2 if player == 1 else 1
        c, addr = s.accept()
        threading.Thread(target=handle_client, args=(c, player, io[f'p{player}']['out'], io[f'p{other_player}']['out'])).start()
        player += 1

    while True:
        pass