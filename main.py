from pygame import *

class GameSprite():
    def __init__ (self, img, x, y, speed):
        self.img = transform.scale(image.load(img), (65,65))
        self.rect = self.img.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        self.direction = "right"

    def reset(self):
        window.blit(self.img,  (self.rect.x, self.rect.y))


class Hero (GameSprite):
    def move(self):
        keys = key.get_pressed()

        if keys[K_d]:
            if self.rect.x < 640:
                self.rect.x += self.speed

        if keys[K_a]:
            if self.rect.x > 10:
                self.rect.x -= self.speed

        if keys[K_w]:
            if self.rect.y > 10:
                self.rect.y -= self.speed

        if keys [K_s]:
            if self.rect.y < 440:
                self.rect.y += self.speed


class Enemy(GameSprite):
    def move(self, start, end):
        if self.direction == "right":
            self.rect.x += 5
        if self.direction == "left":
            self.rect.x -= 5
        if self.rect.x == end:
            self.direction = "left"
        if self.rect.x == start:
            self.direction = "right"


class Wall():
    def __init__(self, x, y, width, height):
        self.img = Surface((width, height))
        self.img.fill((255, 0, 255))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

clock = time.Clock()
FPS = 60

window = display.set_mode((700, 500))
display.set_caption("Доганялки")
background = transform.scale(image.load("background.png"), (700, 500))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

kick = mixer.Sound("kick.ogg")

hero = Hero('sprite1.png', 50, 50, 10 )

enemy = Enemy("sprite2.png", 10, 50, 50)
   


walls = [
        Wall(20, 40, 100, 10),
        Wall(120, 40, 10, 200),
        Wall(120, 240, 200, 10),
        Wall(320, 200, 10, 50),

        ]

map
game = True


while game:
    window.blit(background, (0, 0))
    enemy.reset()
    hero.reset()
    hero.move()
    enemy.move(0, 600)

    for wall in walls:
        wall.draw()

    keys_preesed = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            game = False
      

    display.update()
    clock.tick(FPS)
