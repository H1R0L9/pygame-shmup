from settings import *

import player
import enemy

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pygame Shmup")

        self.all_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.player = player.Player(self.all_sprites, self.player_bullets)
        self.all_sprites.add(self.player)

        self.enemy = enemy.Enemy(self.all_sprites, self.enemy_bullets)
        self.all_sprites.add(self.enemy)
        self.enemy_sprites.add(self.enemy)

    def check_collisions(self):
        bullet_hit_enemy = pygame.sprite.groupcollide(self.player_bullets, self.enemy_sprites, True, False)

        for bullet in bullet_hit_enemy:
            for enemy_hit in bullet_hit_enemy[bullet]:
                enemy_hit.take_damage()

        bullet_hit_player = pygame.sprite.spritecollide(self.player, self.enemy_bullets, True)
        if bullet_hit_player:
            self.player.take_damage()

    def check_input(self):
        key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()
        self.player.controls(key)

    def update(self):
        self.check_collisions()
        self.all_sprites.update()
        self.screen.fill(color=BG_COLOR)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)

    def draw(self):
        pygame.display.flip()

    def mainloop(self):
        while True:
            self.check_input()
            self.update()
            self.player.update()
            self.draw()

if __name__ == "__main__":
    app = App()
    app.mainloop()