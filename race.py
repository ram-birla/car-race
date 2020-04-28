import pygame
import time 
import random
import sys
pygame.init()

#colors
gray = (64, 62, 57)
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
blue = (0,0,200)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)

window_width = 800
window_height = 600
car_width = 56
pause = False


#display
gd = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("CAR-RACE")
carimg = pygame.image.load('c3.png')
clock = pygame.time.Clock()
bgimg = pygame.image.load('bg.png')
intro_bg = pygame.image.load('b-1.jpg')
instrct_bg = pygame.image.load('b-2.jpg')
pause_bg = pygame.image.load('b-3.jpg')
wstrip = pygame.image.load('white.png')
y1 = pygame.image.load('y1.png')
yy2 = pygame.image.load('y-2.png')
y3 = pygame.image.load('y-3.png')
llane = pygame.image.load('lane.png')
rlane = pygame.image.load('rlane.png')
bgd = pygame.image.load('bg-4.png')

crash_sound = pygame.mixer.Sound("pexp.wav")
car_sound = pygame.mixer.Sound("car.wav")
horn_sound = pygame.mixer.Sound("horn.wav")


def intro_loop():
    intro =True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gd.blit(intro_bg,(0,0))
        largetext = pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect = text_objects("CITY RACE",largetext)
        TextRect.center = (400,100)
        gd.blit(TextSurf,TextRect)
        button("START",150,520,100,50,green,bright_green,"play")
        button("QUIT",550,520,100,50,red,bright_red,"quit")
        button("INSTRUCTIONS",300,520,200,50,blue,bright_blue,"instrct")
        pygame.display.update()
        clock.tick(50)

def countdown_bg():
    font = pygame.font.SysFont(None,25)
    x = (window_width*0.45)
    y = (window_height*0.8)
    gd.blit(bgimg,(0,0))
    text = font.render("Car Passed : 0",True,black)
    score = font.render("SCORE : 0",True,bright_red)
    gd.blit(text,(0,50))
    gd.blit(score,(0,30))
    button("Pause",675,0,100,50,green,bright_green,"pause")

def countdown():
    cntdwn = True
    while cntdwn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        countdown_bg()
        largetext = pygame.font.Font('freesansbold.ttf',90)
        ts,tr = text_objects("3",largetext)
        tr.center = ((window_width/2),(window_height/2))
        gd.blit(ts,tr)
        pygame.display.update()
        clock.tick(1)

        countdown_bg()
        largetext = pygame.font.Font('freesansbold.ttf',90)
        ts,tr = text_objects("2",largetext)
        tr.center = ((window_width/2),(window_height/2))
        gd.blit(ts,tr)
        pygame.display.update()
        clock.tick(1)
        
        countdown_bg()
        largetext = pygame.font.Font('freesansbold.ttf',90)
        ts,tr = text_objects("1",largetext)
        tr.center = ((window_width/2),(window_height/2))
        gd.blit(ts,tr)
        pygame.display.update()
        clock.tick(1)
        
        countdown_bg()
        largetext = pygame.font.Font('freesansbold.ttf',90)
        ts,tr = text_objects("GO",largetext)
        tr.center = ((window_width/2),(window_height/2))
        gd.blit(ts,tr)
        pygame.display.update()
        clock.tick(1)
        gameLoop()

def paused():
    global pause
    pygame.mixer.music.pause()
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gd.blit(pause_bg,(0,0))
        largetext = pygame.font.Font('freesansbold.ttf',80)
        ts,tr = text_objects("PAUSED",largetext)
        tr.center = ((window_width/2),(window_height/2))
        gd.blit(ts,tr)
        button("CONTINUE",125,450,150,50,green,bright_green,"unpause")
        button("RESTART",325,450,150,50,blue,bright_blue,"play")
        button("MAIN MENU",525,450,200,50,red,bright_red,"home")
        pygame.display.update()
        clock.tick(30)

def unpaused():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def button(msg,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] >x and y+h >mouse[1] > y:
        pygame.draw.rect(gd,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                countdown()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "instrct":
                instruction()
            elif action == "home":
                intro_loop()
            elif action == "pause":
                paused()
            elif action == "unpause":
                unpaused()

            
    else:
        pygame.draw.rect(gd,ic,(x,y,w,h))
    smalltext = pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect = text_objects(msg,smalltext)
    textrect.center = ((x+(w/2)),(y+(h/2)))
    gd.blit(textsurf,textrect)





def instruction():
    instruction = True
    while instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gd.blit(instrct_bg,(0,0))
        largetext = pygame.font.Font('freesansbold.ttf',80)
        mediumtext = pygame.font.Font('freesansbold.ttf',60)
        smalltext = pygame.font.Font('freesansbold.ttf',20)
        textSurf,textRect = text_objects("City Racing is a 2d racing game made for entertainment.",smalltext)
        textRect.center = (400,180)
        ts,tr = text_objects("The game is consist of  many levels with increasing speed.",smalltext)
        tr.center = (400,210)
        TextSurf,TextRect = text_objects("INSTRUCTIONS",largetext)
        TextRect.center = (400,100)
        gd.blit(ts,tr)
        gd.blit(TextSurf,TextRect)
        gd.blit(textSurf,textRect)
        stextSurf,stextRect = text_objects("Left Arrow : TURN LEFT",smalltext)
        stextRect = (15,350)
        htextSurf,htextRect = text_objects("Right Arrow : TURN RIGHT",smalltext)
        htextRect = (15,400)
        atextSurf,atextRect = text_objects("Press A : ACCELERATION",smalltext)
        atextRect = (520,350)
        btextSurf,btextRect = text_objects("Press B : BRAKE",smalltext)
        btextRect = (520,400)
        ptextSurf,ptextRect = text_objects("Press P : PAUSE",smalltext)
        ptextRect = (15,450)
        ctextSurf,ctextRect = text_objects("CONTROLS",mediumtext)
        ctextRect.center = (400,275)
        gd.blit(stextSurf,stextRect)
        gd.blit(htextSurf,htextRect)
        gd.blit(atextSurf,atextRect)
        gd.blit(btextSurf,btextRect)
        gd.blit(ptextSurf,ptextRect)
        gd.blit(ctextSurf,ctextRect)
        button("Back",350,500,100,50,blue,bright_blue,"home")
        pygame.display.update()
        clock.tick(30)





def obstacle(obs_startx,obs_starty,obs):
    if obs == 0:
        obs_pic = pygame.image.load("c1.png")
    elif obs == 1:
        obs_pic = pygame.image.load("c2.png")
    elif obs == 2:
        obs_pic = pygame.image.load("c4.png")
    elif obs == 3:
        obs_pic = pygame.image.load("c-6.png")
    elif obs == 4:
        obs_pic = pygame.image.load("c-7.png")
    gd.blit(obs_pic,(obs_startx,obs_starty)) 

def score_system(passed,score):
    font = pygame.font.Font("freesansbold.ttf",20)
    text = font.render("CAR PASSED :"+str(passed),True,black)
    score = font.render("SCORE :"+str(score),True,red)
    gd.blit(text,(0,60))
    gd.blit(score,(0,30))

def car(x,y):
    gd.blit(carimg,(x,y))

def bg():
    gd.blit(llane,(0,0))
    gd.blit(llane,(0,200))
    gd.blit(llane,(0,400))
    gd.blit(rlane,(700,0))
    gd.blit(rlane,(700,200))
    gd.blit(rlane,(700,400))
    
    # gd.blit(bgimg,(0,0))

def text_objects(text,font):
    textsurface = font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def msg_display(text):
    lt = pygame.font.Font("freesansbold.ttf",50)
    textsurf,textrect = text_objects(text,lt)
    textrect.center = ((window_width/2),(window_height/2))
    gd.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    gameLoop()

def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    msg_display("CAR CRASHED") 

def horn():
    # pygame.mixer.Sound.stop(car_sound)
    pygame.mixer.Sound.play(horn_sound)
    pygame.mixer.Sound.stop(horn_sound)
    # pygame.mixer.Sound.play(car_sound)

def gameLoop():
    global pause
    x = (window_width*0.45)
    y = (window_height*0.8)
    x_change = 0
    obs_speed = 9
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200,(window_width-200))
    obs_starty = -750
    obs_width = 56
    obs_height = 125
    passed = 0
    level = 1
    score = 0
    y2 = 900
    
    bumped = False
    while not bumped:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_a:
                    obs_speed += 2
                if event.key == pygame.K_b:
                    obs_speed -= 2
                if event.key == pygame.K_h:
                    horn()
                    


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gd.fill(gray)
        
        rel_y = y2 % bgimg.get_rect().width
        gd.blit(bgimg,(0,rel_y-bgimg.get_rect().width))
        if rel_y < 600:
            gd.blit(bgimg,(0,rel_y))
            gd.blit(bgimg,(0,rel_y+800))
            gd.blit(bgd,(0,y+600))
            gd.blit(wstrip,(240,rel_y-190))
            gd.blit(wstrip,(500,rel_y-190))
            gd.blit(y1,(335,rel_y-190))
            gd.blit(yy2,(135,rel_y-190))
            gd.blit(y3,(600,rel_y-190))
            # gd.blit(bgimg,(0,rel_y-600))
            # gd.blit(bgimg,(0,rel_y-500))
            # gd.blit(bgimg,(0,rel_y-400))
            # gd.blit(bgimg,(0,rel_y-300))
            # gd.blit(bgimg,(0,rel_y-200))
            # gd.blit(bgimg,(0,rel_y-100))
            # gd.blit(bgimg,(0,rel_y-50))
            # gd.blit(bgimg,(0,rel_y-25))
            # gd.blit(bgimg,(0,rel_y-12))
            # gd.blit(bgd,(140,rel_y))
            # gd.blit(bgd,(140,rel_y+100))
            # gd.blit(bgd,(140,rel_y+200))
            # gd.blit(bgd,(140,rel_y+300))
            # gd.blit(bgd,(140,rel_y+400))
    
        y2 += obs_speed

        bg()
        obs_starty -=(obs_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty += obs_speed
        car(x,y)
        score_system(passed,score)
        font = pygame.font.Font("freesansbold.ttf",20)
        l = font.render("LEVEL :"+str(level),True,red)
        gd.blit(l,(0,90))
        button("Back",30,500,100,50,blue,bright_blue,"home")
        pygame.mixer.Sound.play(car_sound)
        
        if x > 680-car_width or x < 140:
            pygame.mixer.Sound.stop(car_sound)
            crash()
        if x > window_width-(car_width+110) or x < 110:
            pygame.mixer.Sound.stop(car_sound)
            crash()
        if obs_starty > window_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(170,(window_width-170))
            obs = random.randrange(0,5)
            passed += 1
            score = passed*10
            if passed%10 == 0:
                level += 1
                obs_speed += 2
                lt = pygame.font.Font("freesansbold.ttf",50)
                textsurf,textrect = text_objects("LEVEL "+str(level),lt)
                textrect.center = ((window_width/2),(window_height/2))
                gd.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(3)
    
        if y < obs_starty + obs_height:
            if x > obs_startx  and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                pygame.mixer.Sound.stop(car_sound)
                crash()
        
        button("Pause",675,0,100,50,green,bright_green,"pause")
        pygame.display.update()
        clock.tick(60)

intro_loop()
gameLoop()
pygame.quit()
quit()