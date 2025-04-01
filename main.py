import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spring Scene")

clock = pygame.time.Clock()
running = True

ticker = 0
ticker1 = 0

class bee:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.swdir = False
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 215, 0), (self.x, self.y, 30, 20))
        pygame.draw.line(screen, (0, 0, 0), (self.x+10, self.y), (self.x+10, self.y + 20), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y), (self.x + 20, self.y + 20), 2)
        pygame.draw.ellipse(screen, (255, 255, 255), (self.x+5, self.y-5, 10, 15))
        pygame.draw.ellipse(screen, (255, 255, 255), (self.x+15,self.y-5, 10, 15))

    def move(self, ticker):
        if self.swdir == False:
            if ticker > 10:
                ticker = 0
                self.x += 10
                if self.x > 700:
                    self.swdir = True
        if self.swdir == True:
            if ticker > 10:
                ticker = 0
                self.x -= 10
                if self.x < 100:
                    self.swdir = False


class rainbow:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen):
        pygame.draw.arc(screen, (255, 0, 0), (self.x, self.y, 400, 400), 0, math.pi, 10)
        pygame.draw.arc(screen, (255, 127, 0), (self.x + 10, self.y + 10, 380, 380), 0, math.pi, 10)
        pygame.draw.arc(screen, (255, 255, 0), (self.x + 20, self.y + 20, 360, 360), 0, math.pi, 10)
        pygame.draw.arc(screen, (0, 200, 0), (self.x + 30, self.y + 30, 340, 340), 0, math.pi, 10)
        pygame.draw.arc(screen, (0, 0, 200), (self.x + 40, self.y + 40, 320, 320), 0, math.pi, 10)
        pygame.draw.arc(screen, (75, 0, 130), (self.x + 50, self.y + 50, 300, 300), 0, math.pi, 10)
        pygame.draw.arc(screen, (127, 0, 255), (self.x + 60, self.y + 60, 280, 280), 0, math.pi, 10)

class flower:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 105, 180), (self.x - 10, self.y - 10), 10)
        pygame.draw.circle(screen, (255, 105, 180), (self.x + 10, self.y - 10), 10)
        pygame.draw.circle(screen, (255, 105, 180), (self.x, self.y - 20), 10)
        pygame.draw.circle(screen, (255, 105, 180), (self.x, self.y), 10)
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y - 10), 8)
        pygame.draw.line(screen, (0, 100, 0), (self.x, self.y), (self.x, self.y + 40), 3)

class sun:
    def __init__(self):
        self.x = 700
        self.y = 100
        self.rotate = False

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 223, 0), (self.x, self.y), 50)
        pygame.draw.line(screen, (255, 223, 0), (self.x, self.y - 80), (self.x, self.y + 80), 8)
        pygame.draw.line(screen, (255, 223, 0), (self.x - 80, self.y), (self.x + 80, self.y), 8)
        pygame.draw.line(screen, (255, 223, 0), (self.x- 60, self.y - 60), (self.x+60, self.y + 60), 12)
        pygame.draw.line(screen, (255, 223, 0), (self.x+ 60, self.y - 60), (self.x-60, self.y + 60), 12)

    def move(self, ticker1):
        if ticker1 > 100:
            ticker1 = 0
            self.x *= -1
            self.y *= -1


            
    

beeBag = [bee(200, 150), bee(100, 200)]
r = rainbow(200, 200)
flowerBag = [flower(100,460), flower(500,400)]
s = sun()
while running:
    clock.tick(60)
    ticker += 1
    ticker1 += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in beeBag:
        i.move(ticker)

        s.move(ticker)
    # Sky
    screen.fill((135, 206, 235))

    # Grass
    pygame.draw.rect(screen, (60, 179, 113), (0, 400, 800, 200))

    # Sun
    s.draw(screen)
    # Rainbow 
    r.draw(screen)
    
    



    # Flower 1
    for i in flowerBag:
        i.draw(screen)

    # Bee 1
    for i in beeBag:
        i.draw(screen)

    pygame.display.flip()



pygame.quit()
