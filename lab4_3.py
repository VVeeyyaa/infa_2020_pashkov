import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((400, 550))
green = (18, 252, 1)
blue = (0, 250, 250)
yellow = (250, 250, 0)
gray = (233, 249, 245)
dark_green = (23, 152, 44)
pink = (255, 189, 189)
rotten = (0,0,0)
white = (255, 255, 255)
black = (0, 0, 0)
unicorn1 = (171, 225, 242)
unicorn2 = (246, 187, 236)
unicorn3 = (238, 245, 175)
light_green = (0, 255, 26)
S2 = pygame.Surface((400, 400))


rect(screen, blue, (0, 0, 400, 550 / 2))

rect(S2, blue, (0, 0, 400, 550))
for i in range (10):
    arc(S2, (250, 250, 0), rect(screen, blue, (0, 0, 400, 400)), 3.1 + i * 0.2, 3.15 + i * 0.2, 200)
screen.blit(S2, (200, -200))
circle(screen, (250, 250, 0), (400, 0), 70)
rect(screen, green, (0, 550 / 2, 400, 550 / 2))


FPS = 30

'''
Function tree() draw tree
x, y = position of tree
scale = size of tree
'''

def tree(x, y, scale):
    rect(screen, gray, (x - int(120 / scale), y - int(37.5 / scale), int(30 / scale), int(100 / scale)))
    '''leafes'''
    ellipse(screen, black, (x - int(180 / scale) - 1, y - int(110 / scale) - 1, int(155 / scale) + 2, int(100 / scale) + 2))
    ellipse(screen, black, (x - int(220 / scale) - 1, y - int(180 / scale) - 1, int(230 / scale) + 2, int(120 / scale) + 2))
    ellipse(screen, black, (x - int(170 / scale) - 1, y - int(260 / scale) - 1, int(140 / scale) + 2, int(160 / scale) + 2))
    ellipse(screen, dark_green, (x - int(180 / scale), y - int(110 / scale), int(155 / scale), int(100 / scale)))
    ellipse(screen, dark_green, (x - int(220 / scale), y - int(180 / scale), int(230 / scale), int(120 / scale)))
    ellipse(screen, dark_green, (x - int(170 / scale), y - int(260 / scale), int(140 / scale), int(160 / scale)))
    '''apples on tree'''
    circle(screen, pink, (x - int(60 / scale), y - int(210 / scale)), int(17 / scale))
    circle(screen, pink, (x - int(20 / scale), y - int(120 / scale)), int(16 / scale))
    circle(screen, pink, (x - int(195 / scale), y - int(115 / scale)), int(18 / scale))
    circle(screen, pink, (x - int(145 / scale), y - int(40 / scale)), int(15 / scale))
    '''apples on ground'''
    circle(screen, rotten, (x - int(65 / scale), y + int(70 / scale)), int(13 / scale))
    circle(screen, rotten, (x - int(120 / scale), y + int(80 / scale)), int(12 / scale))
    circle(screen, rotten, (x - int(150 / scale), y + int(55 / scale)), int(16 / scale))

'''
Function body() draw body, head, legs
x, y = position of left bottom angle of body
scale = size of unicorn
orientation: 1 - unicorn look to the right, 0 - to the left
'''

def body(x, y, scale, orientation):
    ellipse(screen, white, (x - int(160 / scale) * int((1 - orientation) / 2), y, int(160 / scale), int(80 / scale)))
    rect(screen, white, (x + orientation * int(40 / scale) - int(19 / scale) * int((1 - orientation) / 2), y + int(70 / scale), int(19 / scale), int(60 / scale)))
    rect(screen, white, (x + orientation * int(8 / scale) - int(15 / scale) * int((1 - orientation) / 2), y + int(50 / scale), int(15 / scale), int(90 / scale)))
    rect(screen, white, (x + orientation * int(98 / scale) - int(17 / scale) * int((1 - orientation) / 2), y + int(50 / scale), int(17 / scale), int(93 / scale)))
    rect(screen, white, (x + orientation * int(130 / scale) - int(15 / scale) * int((1 - orientation) / 2), y + int(50 / scale), int(15 / scale), int(77 / scale)))
    rect(screen, white, (x + orientation * int(100 / scale) - int(50 / scale) * int((1 - orientation) / 2), y - int(50 / scale), int(50 / scale), int(100 / scale)))
    ellipse(screen, white, (x + orientation * int(100 / scale) - int(65 / scale) * int((1 - orientation) / 2), y - int(78 / scale), int(65 / scale), int(50 / scale)))
    ellipse(screen, white, (x + orientation * int(118 / scale) - int(70 / scale) * int((1 - orientation) / 2), y - int(65 / scale), int(70 / scale), int(30 / scale)))
    circle(screen, (229, 153, 206), (x + orientation * int(138 / scale) - int(8 / scale) * int((1 - orientation) / 2), y - int(60 / scale)), int(8 / scale))
    ellipse(screen, white, (x + orientation * int(132 / scale) - int(8 / scale) * int((1 - orientation) / 2), y - int(65 / scale), int(8 / scale), int(5 / scale)))
    polygon(screen, pink, [[x + orientation * int(120 / scale), y - int(75 / scale)], [x + orientation * int(135 / scale), y - int(145 / scale)], [x + orientation * int(138 / scale), y - int(77 / scale)]])
    
'''
Function mane() draw mane
x, y = position of left bottom angle of body
scale = size of unicorn
orientation: 1 - unicorn look to the right, 0 - to the left
'''

def mane(x, y, scale, orientation):
    ellipse(screen, unicorn1, (x + orientation * int(65 / scale) - int(63 / scale) * int((1 - orientation) / 2), y - int(30 / scale), int(63 / scale), int(15 / scale)))
    ellipse(screen, pink, (x + orientation * int(70 / scale) - int(50 / scale) * int((1 - orientation) / 2), y - int(80 / scale), int(50 / scale), int(18 / scale)))
    ellipse(screen, unicorn2, (x + orientation * int(67 / scale) - int(53 / scale) * int((1 - orientation) / 2), y - int(65 / scale), int(53 / scale), int(25 / scale)))
    ellipse(screen, unicorn1, (x + orientation * int(65 / scale) - int(60 / scale) * int((1 - orientation) / 2), y - int(50 / scale), int(60 / scale), int(14 / scale)))
    ellipse(screen, pink, (x + orientation * int(68 / scale) - int(43 / scale) * int((1 - orientation) / 2), y - int(75 / scale), int(43 / scale), int(15 / scale)))
    ellipse(screen, unicorn3, (x + orientation * int(62 / scale) - int(49 / scale) * int((1 - orientation) / 2), y - int(40 / scale), int(49 / scale), int(25 / scale)))
    ellipse(screen, unicorn1, (x + orientation * int(50 / scale) - int(60 / scale) * int((1 - orientation) / 2), y - int(34 / scale), int(60 / scale), int(15 / scale)))
    ellipse(screen, unicorn2, (x + orientation * int(45 / scale) - int(75 / scale) * int((1 - orientation) / 2), y - int(20 / scale), int(75 / scale), int(15 / scale)))
    ellipse(screen, pink, (x + orientation * int(30 / scale) - int(75 / scale) * int((1 - orientation) / 2), y - int(10 / scale), int(75 / scale), int(13 / scale)))
    ellipse(screen, unicorn1, (x + orientation * int(13 / scale) - int(55 / scale) * int((1 - orientation) / 2), y + int(5 / scale), int(55 / scale), int(15 / scale)))
    ellipse(screen, unicorn2, (x - int(55 / scale) * int((1 - orientation) / 2), y - int(5 / scale), int(55 / scale), int(18 / scale )))

'''
Function tail() draw tail
x, y = position of left bottom angle of body
scale = size of unicorn
orientation: 1 - unicorn look to the right, 0 - to the left
'''

def tail(x, y, scale, orientation):
    ellipse(screen, unicorn1, (x - orientation * int(30 / scale) - int(60 / scale) * int((1 - orientation) / 2), y + int(36 / scale), int(60 / scale), int(15 / scale)))
    ellipse(screen, unicorn2, (x - orientation * int(40 / scale) -int(75 / scale) * int((1 - orientation) / 2), y + int(50 / scale), int(75 / scale), int(15 / scale)))
    ellipse(screen, pink, (x -  orientation *int(60 / scale) - int(75 / scale) * int((1 - orientation) / 2), y + int(60 / scale), int(75 / scale), int(13 / scale)))
    ellipse(screen, unicorn3, (x - orientation * int(70 / scale) - int(65 / scale) * int((1 - orientation) / 2), y + int(65 / scale), int(65 / scale), int(13 / scale)))
    ellipse(screen, unicorn1, (x - orientation * int(65 / scale) - int(60 / scale) * int((1 - orientation) / 2), y + int(70 / scale), int(60 / scale), int(15 / scale)))
    ellipse(screen, unicorn3, (x - orientation * int(80 / scale) - int(70 / scale) * int((1 - orientation) / 2), y + int(75 / scale), int(70 / scale), int(13 / scale)))
    ellipse(screen, unicorn2, (x - orientation * int(95 / scale) - int(75 / scale) * int((1 - orientation) / 2), y + int(84 / scale), int(75 / scale), int(18 / scale)))
    ellipse(screen, unicorn3, (x - orientation * int(70 / scale) - int(85 / scale) * int((1 - orientation) / 2), y + int(94 / scale), int(85 / scale), int(13 / scale)))
    ellipse(screen, unicorn1, (x - orientation * int(65 / scale) - int(80 / scale) * int((1 - orientation) / 2), y + int(104 / scale), int(80 / scale), int(17 / scale)))
    ellipse(screen, unicorn3, (x - orientation * int(60 / scale) - int(80 / scale) * int((1 - orientation) / 2), y + int(114 / scale), int(80 / scale), int(19 / scale)))
    ellipse(screen, unicorn2, (x - orientation * int(50 / scale) - int(85 / scale) * int((1 - orientation) / 2), y + int(115 / scale), int(85 / scale), int(18 / scale)))

'''
Function unicorn() draw unicorn
x, y = position of left bottom angle of body
scale = size of unicorn
orientation: 1 - unicorn look to the right, 0 - to the left
'''

def unicorn(x, y, scale, orientation):
    body(x, y, scale, orientation)
    mane(x, y, scale, orientation)
    tail(x, y, scale, orientation)

unicorn(380, 360, 1.7, -1)
unicorn(165, 435, 1.5, 1)
unicorn(205, 300, 2.3, 1)
unicorn(380, 280, 3, -1)
tree(200, 300, 0.9)
tree(110, 340, 1)
tree(185, 400, 1.4)
tree(140, 460, 1.4)
tree(110, 500, 1.5)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
