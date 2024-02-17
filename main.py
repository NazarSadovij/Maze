from pygame import *

class GameSprite():
    def __init__ (self, img, x, y, speed):
        self.img = transform.scale(image.load(img), (65,65))
        self.rect = self.img.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y

        self.move_left = False

    def reset(self):

        if self.move_left == True:
            self.rect.x += self.speed

        window.blit(self.img,  (self.rect.x, self.rect.y))


clock = time.Clock()
FPS = 60

window = display.set_mode((700, 500))
display.set_caption("Доганялки")
background = transform.scale(image.load("background.png"), (700, 500))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

kick = mixer.Sound("kick.ogg")

hero = GameSprite('sprite1.png', 50, 50, 10 )

sprite2 = transform.scale(
    image.load("sprite2.png"),(100, 100))

game = True


while game:
    window.blit(background, (0, 0))
    window.blit(sprite2, (200, 200))
    hero.reset()
    keys_preesed = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_d:
                kick.play()
            if e.key == K_d:
                hero.move_left = True

        if e.type == KEYUP:
            if e.key == K_d:
                hero.move_left = False


    display.update()
    clock.tick(FPS)
