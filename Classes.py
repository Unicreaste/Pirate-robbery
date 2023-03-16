import pygame
import os

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pirate robbery')
clock = pygame.time.Clock()

background = pygame.image.load('Фон.png').convert()
background = pygame.transform.smoothscale(background, gameDisplay.get_size())

run = True

crashed = False


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class ButonSet(pygame.sprite.Sprite):
    image = load_image('Button_Settings.png', color_key=-1)

    def __init__(self, group):
        super().__init__(group)
        self.image = ButonSet.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, 250)

    def get_event(self, event):
        global run
        if self.rect.collidepoint(event.pos):
            pass


class Dark_Layer(pygame.sprite.Sprite):
    image = load_image('dark_layer.png', color_key=-1)

    def __init__(self, group):
        super().__init__(group)
        self.image = ButonSet.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

    def get_event(self, event):
        global run
        if self.rect.collidepoint(event.pos):
            pass


class ButonExit(pygame.sprite.Sprite):
    image = load_image('Button_Exit.png', color_key=-1)

    def __init__(self, group):
        super().__init__(group)
        self.image = ButonExit.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, 350)

    def get_event(self, event):
        global run
        if self.rect.collidepoint(event.pos):
            run = False


start_sprites = pygame.sprite.Group()
sett_sprites = pygame.sprite.Group()

ButonSet(start_sprites)
b_e = ButonExit(start_sprites)

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for bt in start_sprites:
                bt.get_event(event)

    # draw the background
    gameDisplay.blit(background, (0, 0))
    start_sprites.draw(gameDisplay)
    sett_sprites.draw(gameDisplay)
    pygame.display.flip()
