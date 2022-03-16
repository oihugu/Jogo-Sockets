import pygame, socket, threading
import sys, time, os, queue
import assets

host = "127.0.0.1"
port = 5000



def socket_set_up(in_q, out_q):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    threading.Thread(target=assets.client_sockets.recive_data, args=(s, in_q)).start() # create a thread to receive data
    threading.Thread(target=assets.client_sockets.send_data, args=(s, out_q)).start() # create a thread to send data
    return s

def quit(out_queue, s):
    pygame.quit()
    out_queue.put('quit')
    s.shutdown(socket.SHUT_RDWR)
    s.close()
    sys.exit()

def main():
    pygame.init()
    size = [1000, 700] # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock() # Used to manage how fast the screen updates
    in_queue, out_queue = queue.Queue(), queue.Queue() 
    pygame.display.set_caption("Client") # Set the title of the window
    s = socket_set_up(in_queue, out_queue) # Set up the socket
    actual_player = int(in_queue.get())
    other_player = 1 if actual_player == 2 else 2 

    players = {
    'p1': assets.caracter.Caracter(screen, 100, 100, 50, 50, (255, 0, 0), in_queue, out_queue, True if actual_player == 1 else False),
    'p2': assets.caracter.Caracter(screen, 100, 200, 50, 50, (0, 0, 255), in_queue, out_queue, True if actual_player == 2 else False)
    } # Create a dictionary of players

    assets.game_loop.game_loop(False, clock, screen, players[f'p{actual_player}'], players[f'p{other_player}']) #  Main Program Loop

    quit(out_queue, s) # Quit the game


if __name__ == "__main__":
    main() 