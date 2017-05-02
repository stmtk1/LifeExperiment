from random import randrange
import pygame
from pygame.locals import *
import sys

class Animal(object):
    def __init__(self):
        Animal.r = 5
        self.age = 0

    def set_pos(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def get_pos(self):
        return (self.x, self.y)

    def get_age(self):
        return self.age

    def add_age(self):
        if self.limit > self.age:
            self.age += 1
        else:
            self.age = -2

class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__()
        self.limit = 10
        Cat.color = (255, 0, 0)

    def display(self, screen):
        pygame.draw.circle(screen, Cat.color, [self.x, self.y], Animal.r)

class Rat(Animal):
    def __init__(self):
        super(Rat, self).__init__()
        self.limit = 2
        Rat.color = (0, 255, 0)
    
    def display(self, screen):
        pygame.draw.circle(screen, Rat.color, [self.x, self.y], Animal.r)

class Field(object):
    def __init__(self):
        self.rats = []
        self.cats = []
        
        self.size = 100
        pygame.init()
        self.disp_size = (400, 300)
        self.screen = pygame.display.set_mode(self.disp_size)
        pygame.display.set_caption("Experiment")

    """
    def add(self, ani):
        self.animals.append(ani)
    """
    def add_cat(self, ani):
        self.cats.append(ani)
    
    def add_rat(self, ani):
        self.rats.append(ani)

    def add_age(self):
        for c in self.cats:
            c.add_age()
        for r in self.rats:
            r.add_age()

    def delete_dead(self):
       self.cats = [animal for animal in self.cats if animal.age >= 0] 
       self.rats = [animal for animal in self.rats if animal.age >= 0] 

    def print_age(self):
        for animal in self.cats:
            print animal.get_age()
        for animal in self.rats:
            print animal.get_age()
    def display(self):
        for animal in self.cats:
            animal.display(self.screen)
        for animal in self.rats:
            animal.display(self.screen)
    

field = Field()

for i in range(100):
    animal = Cat()
    animal.set_pos(randrange(field.size), randrange(field.size))
    field.add_cat(animal)
    animal = Rat()
    animal.set_pos(randrange(field.size), randrange(field.size))
    field.add_rat(animal)

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    field.screen.fill((255, 255, 255))
    field.display()

"""
for i in range(4):
     field.add_age()
field.print_age()
print(len(field.rats))
field.delete_dead()
print(len(field.rats))
"""
