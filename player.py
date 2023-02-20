from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_group, bullet_group):
        pygame.sprite.Sprite.__init__(self)

        self.all_sprites = sprite_group
        self.bullets = bullet_group

        self.player = pygame.image.load("assets/ships/ship_0000.png").convert_alpha()
        self.image = pygame.transform.scale(self.player, (100, 100))

        self.x = WIDTH/2 - 25
        self.y = HEIGHT - 10

        self.rect = self.image.get_rect()
        self.rect.bottom = self.y
        self.rect.centerx = self.x

        self.health = PLAYER_HEALTH

    def take_damage(self):
        self.health -= BOSS_DAMAGE

    def check_dead(self):
        if self.health <= 0:
            pygame.quit()
            sys.exit()

    def update(self):
        self.check_dead()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top + 10, BULLET_SPEED)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

    def controls(self, pressed_key):
        x, y = 0, 0
        if pressed_key[pygame.K_UP]:
            y -= PLAYER_SPEED
        elif pressed_key[pygame.K_DOWN]:
            y += PLAYER_SPEED
        elif pressed_key[pygame.K_LEFT]:
            x -= PLAYER_SPEED
        elif pressed_key[pygame.K_RIGHT]:
            x += PLAYER_SPEED

        if x != 0 and y != 0:
            x = x*(math.sqrt(2)/2)
            y = y*(math.sqrt(2)/2)

        self.rect.y += y
        self.rect.x += x


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)

        self.bullet = pygame.image.load("assets/vfx/bullets/tile_0000.png").convert_alpha()
        self.image = pygame.transform.scale(self.bullet, (30, 30))

        self.x = x
        self.y = y

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

        self.speed = speed

    def move(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

    def update(self):
        self.move()