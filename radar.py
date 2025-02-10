import pygame
from sys import exit
import math
import pygame.locals
import pygame_widgets
from pygame_widgets.button import Button
pygame.init()

screen = pygame.display.set_mode((857 , 482))
clock = pygame.time.Clock()


BLUE2 = (15, 35, 91)
BLACK = (0, 4, 22)
GREEN = (28, 171, 2)
BLUE = (0, 8, 51)

B_COL = (5,5,5)
BH_COL = (73,73,73)
BC_COl = (140,140,140)
buttonCol = (45,45,45)
targetColor = (242 , 238 ,4)



clicking = False
isDay = True
col = GREEN
inner_color = BLUE
outline = 2
isDay = True
kbCol = (119,117,131)
button_size = (40,20)


centerX = 250
centerY = 241
ppiradius = 232

#RECTANGLES
r1 = pygame.Rect((496 , 3) , (186 , 479))
r2 = pygame.Rect((389 , 3) , (107 , 37))
r3 = pygame.Rect((422 , 40) , (74,  18))
r4 = pygame.Rect((433 , 58) , (63, 18))
r5 = pygame.Rect((2,3) , (78 , 15))
r6 = pygame.Rect((2 , 24) , (78 , 15))
r7 = pygame.Rect((2,44) , (78 , 15))
r8 = pygame.Rect((470 , 117) , (26 , 18))
r9 = pygame.Rect((459 , 372) , (37 ,17))
r10 = pygame.Rect((446 , 389) , (50 , 22))
kb_rect = pygame.Rect((682 , 0) , (175 , 482))

b1 = pygame.Rect((697 ,276) , button_size)
font1 = pygame.font.Font('./Fonts/Digital-7.ttf',size=19)
font2 = pygame.font.Font('Fonts/MerchantCopy.ttf',size=19)
ship = pygame.image.load('ship.png').convert()

def switchCol():
   global isDay , col , inner_color
   if isDay:
       col = BLUE2
       inner_color = BLACK
       isDay = False
   else:
       col = GREEN
       inner_color = BLUE
       isDay = True
def headLine():
    global centerX , centerY , ppiradius , col 
    head = 85
    endX = ppiradius * math.sin(math.radians(head))
    endY = ppiradius * math.cos(math.radians(head))
    pygame.draw.line(screen , 'White' , (centerX , centerY ) , (centerX + endX , centerY - endY) )
def northLine():
    global centerX , centerY , ppiradius
    endX = ppiradius * math.sin(math.radians(0))
    endY = ppiradius * math.cos(math.radians(0))
    pygame.draw.line(screen , (39 ,247 ,247) , (centerX , centerY) , (centerX + endX , centerY - endY))
def distance(x , y , a, b):
    return math.sqrt((int((x - a)**2) + (int((y - b)**2))))

class Target():
    global targetColor 
    def __init__(self , startX , startY , width , height , course , speed):
        self.startX = startX
        self.startY = startY
        self.width = width 
        self.height = height
        self.course = course
        self.speed = speed
    


    def displayTarget(self):
        global ppiradius , centerX , targRect
       #not needed as of now
        # if 90 >= self.course >= 0:
        #     quadCo = self.course
        # elif 180 > self.course > 90:
        #     quadCo = 180 - self.course
        # elif self.course == 180 or self.course == 0 or self.course == 270 or self.course == 90:
        #     quadCo = self.course
        # elif self.course == 360:
        #     quadCo = 0
        # elif 270 > self.course > 180:
        #     quadCo =  self.course - 180
        # elif 360 > self.course > 270:
        #     quadCo = 360 - self.course
        targRect = pygame.Rect(self.startX , self.startY , self.width , self.height)
        pygame.draw.rect(screen , targetColor , targRect )
        if 90 > self.course > 0:
            self.startX += self.speed * math.sin(math.radians(self.course))
            self.startY -= self.speed * math.cos(math.radians(self.course))
        elif 180 > self.course > 90:
            self.startX += self.speed * math.sin(math.radians(self.course))
            self.startY -= self.speed * math.cos(math.radians(self.course))
        elif 270 > self.course > 180:
            self.startX += self.speed * math.sin(math.radians(self.course))
            self.startY -= self.speed * math.cos(math.radians(self.course))
        elif 360 > self.course > 270:
            self.startX += self.speed * math.sin(math.radians(self.course))
            self.startY -= self.speed * math.cos(math.radians(self.course))

        elif self.course == 90:
            self.startX += self.speed
        elif self.course == 180:
            self.startY += self.speed
        elif self.course == 270:
            self.startX -= self.speed
        elif self.course == 0 or self.course == 360:
            self.startY -= self.speed
            # self.startX += self.speed * math.cos(math.radians(self.course))
            # self.startY += self.speed * math.sin(math.radians(self.course))
            # print(math.sin(math.radians(self.course)) , math.cos(math.radians(self.course)))
        targRect.update(self.startX , self.startY , self.width , self.height)
        dist = distance(targRect.x , targRect.y , centerX , centerY)
        if dist-4 >= ppiradius:
            self.startX = 150
            self.startY = 205
            self.course += 5
    
    def Bearing(self):
        global centerX , centerY
        bearing = math.degrees(math.atan2(self.startX - centerX , self.startY - centerY))
        if bearing < 0:
            bearing = 360 + bearing
        # bearing = round(bearing)
        bearing = str(bearing)
        return bearing


north = 0  

t1 = Target(150 , 205 , 4 , 4 , 115 , 1.70)
t2 = Target(190 , 89 , 4, 4 , 140 , 1.25)
t3 = Target(210 , 210 , 5 , 2 , 90 , 0.25)

b1 = Button(
        screen , 697 , 276 , 20 , 20 , False , text='hi' , inactiveColour = B_COL , hoverColour = BH_COL , pressedColour = BC_COl,
        textColour = 'Red' ,
        onClick = lambda: switchCol()
    )

# incHead = Button(
#     screen , 697 , 200 , 20 ,20 , False, text='increaseHeading' ,
#     inactiveColour = B_COL , hoverColour = BH_COL , pressedColour = BC_COl,
#     textColour = 'Red' ,
#     onClick = lambda: print()
# )

while True:
    a, b = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill((0,0,0))
    pygame.draw.circle(screen , inner_color , (centerX , centerY) , ppiradius)
    t1.displayTarget()
    t1bear = t1.Bearing()
    t2.displayTarget()
    t3.displayTarget()
    t1b = font1.render(f"{t1bear}" , False , col)
    screen.blit( t1b , (496 ,  25))
    pygame.draw.circle(screen , col , (centerX , centerY), ppiradius , outline)
    pygame.draw.circle(screen , 'Yellow' , (250 , 241) , 2)
    #crosshair
    pygame.draw.line(screen , 'White' , (centerX , centerY + 5 ) , (centerX, centerY - 5))
    pygame.draw.line(screen , 'White' , (centerX - 5 , centerY ) , (centerX + 5 , centerY))
    #drawing the rectangles
    pygame.draw.rect(screen , col , r1 , outline)
    pygame.draw.rect(screen , col , r2 , outline)
    pygame.draw.rect(screen , col , r3 , outline)
    pygame.draw.rect(screen , col , r4 , outline)
    pygame.draw.rect(screen , col , r5 , outline)
    pygame.draw.rect(screen , col , r6 , outline)
    pygame.draw.rect(screen , col , r7 , outline)
    pygame.draw.rect(screen , col , r8 , outline)
    pygame.draw.rect(screen , col , r9 , outline)
    pygame.draw.rect(screen , col , r10 , outline)
    pygame.draw.rect(screen , kbCol , kb_rect)
    # pygame.draw.rect(screen , buttonCol , b1  , border_radius=10)
    #lines (not sure)
    pygame.draw.line(screen, col , (446 , 400 ) , (495 , 400) , width=3)
    #FONT+TEXT
    f1 = font1.render("HDG. 003.00 deg" , False , col)
    f4 = font2.render("HDG. 003.00 deg" , False , col)
    f2 = font1.render(" 12NM    /2" , False , col)
    f3 = font1.render("HEADUP RM" , False , col)
    b1F = font1.render('d/n' , False , 'White')
    fr1 = f1.get_rect(topleft = (497 , 3))
    fr2 = f2.get_rect(topleft = (3 , 5))
    fr3 = f3.get_rect()
    # b1FR = b1F.get_rect(center=b1.center)
    # screen.blit(b1F , b1FR)
    screen.blit(f1 , fr1)
    screen.blit(f2 , r5)
    screen.blit(f4 , (fr1.x + 60 , fr1.y + 200)) 
    headLine()
    # northLine()

    b1.draw()
    pygame_widgets.update(event)
    pygame.display.update()

    clock.tick(1)