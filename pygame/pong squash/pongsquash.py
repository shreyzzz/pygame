import pygame
WIDTH=1200
HEIGHT=600
BORDER=20
PWIDTH=30
PHEIGHT=300
fgColor = pygame.Color("white")
bgColor = pygame.Color("black")
RADIUS=15
velocity=-1
FRAMERATE=400

class Ball:
    global RADIUS

    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y=y
        self.vx=vx
        self.vy=vy
    def show(self, color):
        global screen,WIDTH,PWIDTH,BORDER,HEIGHT,PHEIGHT,bgColor, fgColor
        pygame.draw.circle(screen, color, (self.x, self.y), RADIUS)
    def update(self):
        global bgColor, fgColor
        self.show(bgColor)
        newx=self.x+self.vx
        newy=self.y+self.vy
        if newx<BORDER+RADIUS:
            self.vx=-self.vx
        elif newy>HEIGHT-BORDER-RADIUS or newy<BORDER+RADIUS:
            self.vy=-self.vy
            self.y=self.y+self.vy
        elif newx>WIDTH-PWIDTH-RADIUS and newy in range(pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[1]+PHEIGHT):
            self.vx=-self.vx
        else:
            self.show(bgColor)
            self.x=self.x+self.vx
            self.y=self.y+self.vy
            self.show(fgColor)


class Paddle:
    global HEIGHT, WIDTH, BORDER,PWIDTH, PHEIGHT
    def __init__(self, py):
        self.py=py
    def show(self, color):
        global screen
        pygame.draw.rect(screen, color, pygame.Rect((WIDTH-PWIDTH,self.py),(BORDER, PHEIGHT)))
    def update(self):
        if pygame.mouse.get_pos()[1]>BORDER and pygame.mouse.get_pos()[1]<HEIGHT-BORDER-PHEIGHT:
            self.show(pygame.Color("black"))
            self.py=pygame.mouse.get_pos()[1]
            self.show(pygame.Color("white"))

ballplay= Ball(WIDTH-RADIUS, HEIGHT//2,velocity, velocity)
paddleplay=Paddle(HEIGHT//2)

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
ballplay.show(fgColor)
pygame.draw.rect(screen, fgColor, pygame.Rect((0,0), (WIDTH,BORDER)))
pygame.draw.rect(screen, fgColor, pygame.Rect((0,0), (BORDER,HEIGHT)))
pygame.draw.rect(screen, fgColor, pygame.Rect((0,HEIGHT-BORDER), (WIDTH,BORDER)))
clock=pygame.time.Clock()
while True:

    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    clock.tick(FRAMERATE)
    pygame.display.flip()
    ballplay.update()
    paddleplay.update()
pygame.quit()
