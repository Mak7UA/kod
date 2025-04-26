import pygame 
pygame.init()
window=pygame.display.set_mode((500,500))

window.fill((158,213,0))
clock=pygame.time.Clock()
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.fill_color = color
        self.rect = pygame.Rect(x, y, width, height)
       
    def set_color(self, new_color):
        self.fill_color = new_color
   
def fill(self):
    if self.fill_color is not None:  # Перевірка, чи колір задано
        pygame.draw.rect(window, self.fill_color, self.rect)

def outline(self, frame_color, thickness):
    if frame_color is not None and thickness > 0:  # Перевірка, чи колір і товщина задані
        pygame.draw.rect(window, frame_color, self.rect, thickness)
        
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
class Picture(Area):
    def __init__(self,filename, x=0, y=0, width=10,height=10):
        Area.__init__(self,x=x,y=y,width=width,height=height,color=None)
        self.image=pygame.image.load(filename)
    def draw(self):
        window.blit(self.image,(self.x,self.y))
platform_x=200
platform_y=300
ball=Picture("ball.png",x=160,y=200,width=50,height=50)
platform=Picture("platform.png",platform_x,platform_y,100,30)
start_x=5
start_y=5
count=4
monsters=[]
for i in range(10):
    y=start_y+(25*i)
    x=start_x+(25*i)
    for j in range(count):
        enemy=Picture("enemy.png",x,y,width=50,height=50)
        monsters.append(enemy)
        x=x+50
speed_x=3
speed_y=3
game=True
while game:
    ball.fill()
    platform.fill()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                platform.rect_x+=3

            if event.key==pygame.K_LEFT:
                platform.rect_x-=3


            if event.key==pygame.K_UP:
                platform.y=platform.y-5
            if event.key==pygame.K_DOWN:
                platform.y=platform.y+5
    for m in monsters:
        m.draw()
    platform.draw()
    ball.draw()
    ball.rect.x+=speed_x
    ball.rect.y+=speed_y
    if ball.rect.y<0:
        speed_y*=-1
    if ball.rect.x<0 or ball.rect.x>500:
        speed_x*=-1
    if ball.rect.colliderect(platform.rect):
        speed_y*=-1
        speed_x*=-1
    clock.tick(40)
    pygame.display.update()
pygame.quit()
