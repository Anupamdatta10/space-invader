import pygame as pg
import time
from pygame import mixer
import math
import random
pg.init()

screen=pg.display.set_mode((800,600))
pg.display.set_caption("space invader")
icon=pg.image.load("ufo.png")
player_img=pg.image.load("space-ship.png")
bg_img=pg.image.load("bg.png")
bullet=pg.image.load("bullet.png")
pg.display.set_icon(icon)
mixer.music.load("background.wav")
mixer.music.play(-1)
running=True
score=0
px=370
py=480
px_change=0

num_enemy=10

enemy=[]
ex=[]
ey=[]
ex_change=[]
ey_change=[]



for i in range(num_enemy):
    enemy.append(pg.image.load("alien.png"))
    ex.append(random.randint(0,768))
    ey.append(random.randint(20,150))
    ex_change.append(1)
    ey_change.append(20)

bx=px
by=480
bstate="ready"
by_change=5

font=pg.font.Font("freesansbold.ttf",32)
tx=10
ty=550
def show_score(x,y):
    s=font.render("score: "+str(score),True,(255,255,255))
    screen.blit(s,(x,y))
    go=font.render("created by Anupam",True,(255,0,0))
    screen.blit(go,(450,y))
def player(x,y):
    screen.blit(player_img,(x,y))


def enemy_pos(x,y):
    screen.blit(enemy[i],(x,y))

def fire(x,y):
    global bstate
    bstate="fire"
    screen.blit(bullet,(x+10,y))

def dis(x1,y1,x2,y2):
    dis=math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2)) 
    if dis<=25:
        return True
    else:
        return False

while running:
    screen.fill((16,16,46))
    screen.blit(bg_img,(0,0))
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_LEFT:
                px_change=-2
            if event.key==pg.K_RIGHT:
                px_change=2
            if event.key==pg.K_SPACE and bstate=="ready":
                bs=mixer.Sound("laser.wav")
                bs.play()
                bx=px
                fire(bx,by)
        if event.type==pg.KEYUP:
             if event.key==pg.K_LEFT or event.key==pg.K_RIGHT:
                 px_change=0 
    



    px=px+px_change
    if px<=0:
        px=0
    elif px>=768:
        px=768

    for i in range(num_enemy):

        if ey[i]>200:
            for j in range(num_enemy):
                ey[j]=2000
            go=font.render("GAME OVER",True,(255,255,255))
            screen.blit(go,(270,250))
            break
        if score==10:
            go=font.render("YOU WIN",True,(255,255,255))
            screen.blit(go,(270,250))
            break


        ex[i]+=ex_change[i]
        if ex[i]<=0:
            ex_change[i]=1
            ey[i]+=ey_change[i]
        elif ex[i]>=768:
            ex_change[i]=-1
            ey[i]+=ey_change[i]
        
        colition=dis(ex[i],ey[i],bx,by)
        if colition:
            bls=mixer.Sound("explosion.wav")
            bls.play()
            bstate="ready"
            score+=1
            ex[i]=random.randint(0,768)
            ey[i]=-2000
            by=480
        enemy_pos(ex[i],ey[i])



    if by<=0:
        bstate="ready"
        by=py
        bx=px
    if bstate == "fire":
        fire(bx,by)
        by-=by_change
    



    player(px,py)
    show_score(tx,ty)
    pg.display.update()
