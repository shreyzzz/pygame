
import pygame
WIDTH=700
HEIGHT=700
BORDER=20
RADIUS=30
counter = 0
pygame.font.init()
font= pygame.font.SysFont('timesnewroman', 32)
text1=font.render('PLAYER 1 TO MOVE', True, "white", "black")
text2=font.render('PLAYER 2 TO MOVE', True, "white", "black")
text3=font.render('PLAYER 1 WON', True, "white", "black")
text4=font.render('PLAYER 2 WON', True, "white", "black")
text1rect= text1.get_rect()
text1rect.center=(350, 100)
fgColor = pygame.Color("Black")
bgColor = pygame.Color("white")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.draw.line(screen, "white", (300,200), (300, 500), 12)
pygame.draw.line(screen, "white", (400,200), (400, 500), 12)
pygame.draw.line(screen, "white", (200,300), (500, 300), 12)
pygame.draw.line(screen, "white", (200,400), (500, 400), 12)
FRAMERATE = 400

l=[["","","",""],["","",""],["","",""]]

class Cross:
    def __init__(self):
        pass
    def showCross(self, x, y):
        pygame.draw.rect(screen, "white", pygame.Rect((x-30, y-30), (60,60)))
class Circle:
    global screen,RADIUS
    def __init__(self):
        pass
    def showCirc(self ,x , y):
        pygame.draw.circle(screen, "white", (x, y), RADIUS)

class Cells(Cross, Circle):
    def __init__(self):
        pass
    def state(self):
        global counter, l
        pos = pygame.mouse.get_pos()
        e=pygame.event.poll()
        if counter%2==0:
            screen.blit(text1, text1rect)
        else:
            screen.blit(text2, text1rect)
        if e.type==pygame.MOUSEBUTTONUP and pos[0]>200 and pos[1]>200 and pos[0]<500 and pos[1]<500:

            cordx=(pos[0]//100)-2
            cordy=pos[1]//100-2

            if counter%2==0:
                Cross.showCross(self, (pos[0]//100)*100+50, (pos[1]//100)*100+50)
                counter+=1
                l[cordx][cordy]=0
            else:
                Circle.showCirc(self, (pos[0]//100)*100+50, (pos[1]//100)*100+50)
                counter+=1
                l[cordx][cordy]=1
def win():
      for m in range(0,3):
            for n in range(0,3):
                  if (l[m][0]==l[m][1] and l[m][1]==l[m][2] and l[m][1]==0)or(l[0][n]==l[1][n] and l[1][n]==l[2][n] and l[0][n]==0)or(l[0][0]==l[1][1] and l[1][1]==l[2][2] and l[2][2]==0)or(l[0][2]==l[1][1] and l[2][0]==l[1][1] and l[0][2]==0):
                        return('player1')
                  elif(l[m][0]==l[m][1] and l[m][1]==l[m][2] and l[m][1]==1)or(l[0][n]==l[1][n] and l[1][n]==l[2][n] and l[0][n]==1)or(l[0][0]==l[1][1] and l[1][1]==l[2][2] and l[2][2]==1)or(l[0][2]==l[1][1] and l[2][0]==l[1][1] and l[0][2]==1):
                        return('player2')

p=Cells()

clock = pygame.time.Clock()
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    if counter%2==0:
        if win()=='player1':
            screen.blit(text3, text1rect)
        elif win()=='player2':
            screen.blit(text4, text1rect)
        else:
            screen.blit(text1, text1rect)
    else:
        if win()=='player1':
            screen.blit(text3, text1rect)
        elif win()=='player2':
            screen.blit(text4, text1rect)
        else:
            screen.blit(text2, text1rect)
    
    clock.tick(FRAMERATE)
    pygame.display.update()
    p.state()
pygame.quit()