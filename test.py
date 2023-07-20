import pygame, math  # добавлено
import random as r

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
fps = 30
width = 1500
height = 900


class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = (r.randint(0, width))
        self.rect.y = (r.randint(0, height))


class Animal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = width // 2
        self.rect.y = height // 2
        self.x = width / 2  # добавлено
        self.y = height / 2  # добавлено
        self.speedx = 0.
        self.speedy = 0.  # добавлено

    def go(self):  # добавлено
        self.x += self.speedx  # добавлено
        self.y += self.speedy  # добавлено
        self.rect.x = int(self.x)  # добавлено
        self.rect.y = int(self.y)  # добавлено

    def set_speed(self, x, y, speed):  # добавлено
        xs = x - self.x  # добавлено
        ys = y - self.y  # добавлено
        k = speed / math.sqrt(xs * xs + ys * ys)  # добавлено
        self.speedx = xs * k  # добавлено
        self.speedy = ys * k  # добавлено

    def get_distance(self, x, y):  # добавлено
        xs = x - self.x  # добавлено
        ys = y - self.y  # добавлено
        return math.sqrt(xs * xs + ys * ys)  # добавлено


pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Симуляция естественного отбора")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

entity = Animal()
entity.set_speed(1000, 10, 1.)  # добавлено

foods = pygame.sprite.Group()
all_sprites.add(entity)

for i in range(50):
    f = Food()
    all_sprites.add(f)
    foods.add(f)

all_sprites.add(foods)
inGame = True

while inGame:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False

    screen.fill((black))
    all_sprites.update()
    asd = r.randint(0, 100)

    entity.go()  # добавлено

    for it in range(1):
        if asd > 0 and asd < 50:
            f = Food()
            all_sprites.add(f)
            foods.add(f)

    all_sprites.draw(screen)
    hits = pygame.sprite.spritecollide(entity, foods, True)
    pygame.display.flip()

pygame.quit()
