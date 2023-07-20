import pygame, math

WIDTH = 800
HEIGHT = 600

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

running = True

pygame.init()
pygame.mixer.init()
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load('data/Test_Land.png').convert()
background = pygame.transform.smoothscale(background, gameDisplay.get_size())

surf = pygame.Surface((800, 600))
gameDisplay.blit(surf, (0, 0))
pygame.display.set_caption("")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.x = self.rect.left
        self.y = self.rect.top
        self.speedx = 0

    def coords(self):
        return f"coords: {self.x}, {self.y}"

    def update(self):
        self.speedx = 0
        self.x = self.rect.left
        self.y = self.rect.top
        global running
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -3
        if keystate[pygame.K_d]:
            self.speedx = 3
        self.rect.x += self.speedx

        if keystate[pygame.K_s]:
            self.speedy = 3
            self.rect.y += self.speedy  # +
        if keystate[pygame.K_w]:
            self.speedy = -3
            self.rect.y += self.speedy  # +
        #        self.rect.y += self.speedy

        if self.rect.left < 150:
            self.rect.left = 150
        if self.rect.right > 650:
            self.rect.right = 650

        if self.rect.top < 100:
            self.rect.top = 100
        if self.rect.bottom > 500:
            self.rect.bottom = 500

        if 420 < self.rect.right < 480 and 270 < self.rect.bottom < 350 and keystate[pygame.K_z]:
            running = False


    def get_event(self, event):
        global run
        if self.rect.collidepoint(event.pos):
            pass


class NPS(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = 460
        self.rect.bottom = 300
        self.speedx = 0

    def get_event(self, event):
        global run
        if self.rect.collidepoint(event.pos):
            pass



all_sprites = pygame.sprite.Group()
player = Player()
nps = NPS()
all_sprites.add(player)
all_sprites.add(nps)


while running:
    clock.tick(FPS)
    print(player.coords())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    gameDisplay.blit(background, (0, 0))
    all_sprites.draw(gameDisplay)
    pygame.display.flip()

pygame.quit()
