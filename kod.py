import pygame
pygame.init()
window = pygame.display.set_mode((750, 700))
window.fill((158, 213, 0))
clock = pygame.time.Clock()

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
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        super().__init__(x=x, y=y, width=width, height=height)
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))
        
    def draw(self):
        window.blit(self.image, (self.x, self.y))


class Label(Area):
    def set_text(self,text,fsize=12,text_color=(0,0,0)):
        self.image=pygame.font.SysFont("vernada", 20).render("Game over", True,(255,0,0))
    def draw(self,shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.x+shift_x, self.y+shift_y))



platform_x = 200
platform_y = 300

# ВАЖЛИВО: ці зображення мають бути в одній папці з .py файлом
ball = Picture("ball.png", 160, 200, 50, 50)
platform = Picture("platform.png", platform_x, platform_y, 100, 30)

# створення ворогів
start_x = 5
start_y = 5
monsters = []
for i in range(4):
    y = start_y + (55 * i)
    x = start_x + (25 * i)
    for j in range(4):
        enemy = Picture("enemy.png", x, y, 50, 50)
        monsters.append(enemy)
        x += 55
#початкова швидкість м'яча
speed_x=3
speed_y=3
game = True
font1=pygame.font.Font(None, 70)
font2=pygame.font.Font(None, 30)
  
while game:
    window.fill((158, 213, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                platform.x+=10
            if event.key==pygame.K_LEFT:
                platform.x=-10
    for m in monsters:
        m.draw()
        if m.rect.colliderect(ball.rect):
            monsters.remove(m)
            m.fill()    
            speed_y*=-1

    platform.draw()
    ball.draw()
    ball.x+=speed_x
    ball.y+=speed_y
    if ball.y<0:
        speed_y*=-1
    if ball.x<0 or ball.x>750:
        speed_x*=-1
    if ball.rect.collidepoint(platform_y,platform_y):
        speed_x*=-1
        speed_y*=-1
    if ball.y>700:
        time_text=Label(150,150,50,50,(158,213,0))
        time_text.set_text("Ти програв",30,(255,200,0))
        time_text.draw(10,10)
       
    if len(monsters)==0:
        time_text=Label(150,150,50,50,(158,213,0))
        time_text.set_text("Ти виграв",30,(255,200,0))
        time_text.draw(10,10)
        
    clock.tick(40)
    pygame.display.update()

pygame.quit()
