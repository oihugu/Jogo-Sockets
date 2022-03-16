import pygame
import json

class Caracter():
    def __init__(self, surface, x, y, width, height, color, in_queue, out_queue, type):
        self.type = type
        self.in_queue, self.out_queue = in_queue, out_queue
        self.surface = surface
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)

    def draw(self):
        self.surface.blit(self.image, self.rect)
    
    def move(self, x, y):
        self.x += x
        self.y += y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)


    def move_to(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
    
    def io(self):
        if self.type:
            self.out_queue.put({"x": self.x, "y": self.y}) # Send the position to the server
        else: 
            if not self.in_queue.empty():
                dct_str = self.in_queue.get() # get the data from the queue in json format
                mv_dct = json.loads(dct_str) # convert the json string to a dictionary
                self.move_to(mv_dct['x'], mv_dct['y']) # move the caracter to the new position
