from pygame import *
from random import *
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, a, b, p_speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image),(a, b))
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y 
        self.speed = p_speed
 
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys= key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_r(self):
        keys= key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed


window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
ball = GameSprite('ball3.png', 320, 220, 50, 50 , 4)
platform1 = Player("Platform.png", 5, 10, 30, 150, 4)
platform2 = Player("Platform.png", 665, 340, 30, 150, 4)
bg = transform.scale(image.load('galaxy.jpg'), (700, 500))
game = True
finish = False
font.init()
font1 = font.SysFont('Arial',70)
clock = time.Clock()
win = font1.render('P2 WIN!!!', True, (255,215,0))
win2 = font1.render('P1 WIN!!!', True, (180,0,0))

Vx = 4
Vy = 4

while game:
    for evnt in event.get():
        if evnt.type == QUIT:
            game = False

    if finish == False:
        window.blit(bg, (0, 0)) 
        platform1.reset()
        platform1.update_l()
        platform2.reset()
        platform2.update_r()
        ball.reset()
        ball.rect.x += Vx
        ball.rect.y -= Vy

        if sprite.collide_rect(platform1, ball) or sprite.collide_rect(platform2, ball):
            Vx = Vx*-1
        if ball.rect.y < 1 or ball.rect.y > 450:
            Vy = Vy*-1
        if ball.rect.x < 1:
            finish = True
            window.blit(win,(200,200))
        if ball.rect.x > 650:
            finish = True
            window.blit(win2,(200,200))            


    display.update()
    clock.tick(60)
