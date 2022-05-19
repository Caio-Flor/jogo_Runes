import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/player.png") #16x16
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = pygame.Rect(250,250,100,100)

    def update(self, *args):
        # Lógica do jogo
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rect.x += 1
        elif keys[pygame.K_a]:
            self.rect.x -= 1
        elif keys[pygame.K_w]:
            self.rect.y -= 1
        elif keys[pygame.K_s]:
            self.rect.y += 1