from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, sprite_group, enemy_bullet_group):
        pygame.sprite.Sprite.__init__(self)
        self.all_sprites = sprite_group
        self.enemy_bullet_group = enemy_bullet_group

        self.boss_image = pygame.image.load("assets/ships/ship_0014.png").convert_alpha()
        self.image = pygame.transform.scale(self.boss_image, (200, 200))
        self.image = pygame.transform.flip(self.image, 0, 1)

        self.x = WIDTH/2 - 25
        self.y = 300

        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.bottom = self.y

        self.health = BOSS_HEALTH

        self.isKilled = False

        self.shoot_delay = 500
        self.last_shot_time = 0

        self.clock = pygame.time.Clock()

    def death_anim(self):
        pass

    def shoot(self):
        if pygame.time.get_ticks() - self.last_shot_time > self.shoot_delay:
            bulletx = random.randrange(self.rect.left, self.rect.right)
            bullet_speed = random.randrange(1, 8)
            bullet = Bullet(bulletx, self.y, bullet_speed)
            self.all_sprites.add(bullet)
            self.enemy_bullet_group.add(bullet)
            self.last_shot_time = pygame.time.get_ticks()

    def take_damage(self):
        self.health -= PLAYER_DAMAGE

    def check_dead(self):
        if self.health <= 0:
            self.isKilled = True
            self.kill()

    def update(self):
        if not self.isKilled:
            self.shoot()
            self.check_dead()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)

        self.bullet = pygame.image.load("assets/vfx/bullets/tile_0003.png").convert_alpha()
        self.image = pygame.transform.scale(self.bullet, (30, 30))
        self.image = pygame.transform.flip(self.image, 0, 1)

        self.x = x
        self.y = y

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

        self.speed = speed

    def move(self):
        self.rect.y += self.speed
        if self.rect.bottom > HEIGHT + 10:
            self.kill()

    def update(self):
        self.move()