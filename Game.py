import pygame
import os
import subprocess

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pirate robbery')
clock = pygame.time.Clock()

background = pygame.image.load('Фон.png').convert()
background = pygame.transform.smoothscale(background, gameDisplay.get_size())

surf = pygame.Surface((800, 600))
gameDisplay.blit(surf, (0, 0))

run = True

crashed = False

Sound_on = True


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


class ButonPlay(pygame.sprite.Sprite):
    image = load_image('Button_Play.png', color_key=-1)

    def __init__(self, group):
        super().__init__(group)
        self.image = ButonPlay.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, 150)

    def get_event(self, event):
        global run
        if self.rect.collidepoint(event.pos):
            run = False
            subprocess.call("Land.py", shell=True)


class ButonSet(pygame.sprite.Sprite):
    image = load_image('Button_Settings.png', color_key=-1)

    def __init__(self, group):
        super().__init__(group)
        self.image = ButonSet.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, 250)

    def get_event(self, event):
        global run, X, Sett, Sound
        if self.rect.collidepoint(event.pos):
            X = ButonX(start_sprites)
            Sett = Sett_wind(start_sprites)
            Sound = SoundButton(start_sprites)


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


class SoundButton(pygame.sprite.Sprite):
    image = load_image('S_ON.png', color_key=-1)
    image2 = load_image('S_OFF.png', color_key=-1)
    image3 = load_image('S_ON.png', color_key=-1)

    def __init__(self, group):
        super().__init__(group)
        if Sound_on == True:
            self.image = SoundButton.image
        else:
            self.image = self.image2
        self.rect = self.image.get_rect()
        self.rect.topleft = (525, 400)

    def get_event(self, event):
        global run, Sound_on
        if self.rect.collidepoint(event.pos):
            if pygame.mixer.music.get_volume() > 0:
                pygame.mixer.music.set_volume(0)
                self.image = self.image2
                Sound_on = False

            else:
                pygame.mixer.music.set_volume(10)
                self.image = self.image3
                Sound_on = True


class ButonX(pygame.sprite.Sprite):
    image = load_image('Bt_X.png', color_key=-1)

    def __init__(self, group):
        super().__init__(group)
        self.image = ButonX.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (620, 65)

    def get_event(self, event):
        global run, Sett_open
        if self.rect.collidepoint(event.pos):
            X.kill()
            Sett.kill()
            Sound.kill()


class Sett_wind(pygame.sprite.Sprite):
    image = load_image('Sett_wind.png', color_key=-1)

    def __init__(self, group):
        super().__init__(group)
        self.image = Sett_wind.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (110, 100)

    def get_event(self, event):
        global run
        if self.rect.collidepoint(event.pos):
            pass


start_sprites = pygame.sprite.Group()

ButonPlay(start_sprites)
ButonExit(start_sprites)
ButonSet(start_sprites)

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
    pygame.display.flip()
