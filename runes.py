import pygame

# p - parede
# <space> - area em branco

mapa = [
    "pppppppppppppppppppppppppppppppppppppppp",
    "p       p                              p",
    "p       p                              p",
    "p       p                              p",
    "p    pppp               pppppppppppppppp",
    "p                                      p",
    "p                                      p",
    "p     ppppppppppppppp                  p",
    "p                   p                  p",
    "p                   p                  p",
    "p                   p          p       p",
    "p                   p          p       p",
    "p                   p          p       p",
    "p                   p          p       p",
    "p                              p       p",
    "p                              p       p",
    "p     pppppppppppppppppppppppppp       p",
    "p                                      p",
    "p                                      p",                                
    "pppppppppppppppppppppppppppppppppppppppp"
]

TELA_WIDTH = 800
TELA_HEIGHT = 600

BLK_WIDTH = TELA_WIDTH / 40
BLK_HEIGHT = TELA_HEIGHT / 20

pygame.init()
tela = pygame.display.set_mode((TELA_WIDTH, TELA_HEIGHT))

#Função que seleciona a imagem e corrige a escala
def load_image(img_set, x, y):
    img_orig = img_set.subsurface((x, y), (16, 16))
    img_scaled = pygame.transform.scale(img_orig, (BLK_WIDTH, BLK_HEIGHT))
    return img_scaled

tiles = pygame.image.load("./data/basictiles_2.png").convert_alpha()
caracteres = pygame.image.load("./data/characters.png").convert_alpha()
#Carrega imagem da grama
img_grama = load_image(tiles, 16, 128)
#Carrega imagem de parede
img_parede = load_image(tiles, 48, 0)

class Personagem (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.vel_x = 0
        self.vel_y = 0

        #Carrega imagem do personagem
        car_img_1 = load_image(caracteres, 48, 0)
        car_img_2 = load_image(caracteres, 64, 0)
        car_img_3 = load_image(caracteres, 80, 0)
        self.lista_imagens = [car_img_1, car_img_2, car_img_3]
        self.image_idx = 0
        self.image = car_img_1
        self.rect = pygame.Rect((32, 32), (BLK_WIDTH, BLK_HEIGHT))

    def update(self):
        self.image = self.lista_imagens[self.image_idx]
        self.image_idx += 1
        if self.image_idx >= len(self.lista_imagens):
            self.image_idx = 0
        
        intencao_x = self.rect.x + self.vel_x
        intencao_y = self.rect.y + self.vel_y
        colisao = False

        for id_linha, linha in enumerate(mapa):
            for id_coluna, caracter in enumerate(linha):
                if caracter == 'p':
                    x = id_coluna * BLK_WIDTH
                    y = id_linha * BLK_HEIGHT
                    r = pygame.Rect((x, y), (BLK_WIDTH,BLK_HEIGHT))
                    r2 = self.rect.copy()
                    r2.move_ip(self.vel_x, self.vel_y)
                    if r.colliderect(r2):
                        colisao = True

        if not colisao:
            self.rect.move_ip(self.vel_x, self.vel_y)

    def processar_evento(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_d:
                self.vel_x = 1.0
            if e.key == pygame.K_a:
                self.vel_x = - 1.0
            if e.key == pygame.K_w:
                self.vel_y = -1.0
            if e.key == pygame.K_s:
                self.vel_y = 1

        if e.type == pygame.KEYUP:
            if e.key in [pygame.K_a, pygame.K_d]:
                self.vel_x = 0.0
            if e.key in [pygame.K_w, pygame.K_s]:
                self.vel_y = 0.0

heroi = Personagem()
grupo_heroi = pygame.sprite.Group(heroi)

while True:
    for id_linha, linha in enumerate(mapa):
        for id_coluna, caracter in enumerate(linha):
            x = id_coluna * BLK_WIDTH
            y = id_linha * BLK_HEIGHT
            if caracter == 'p':
                tela.blit(img_parede, (x, y))
            else:
                tela.blit(img_grama , (x, y))

    grupo_heroi.draw(tela)
    pygame.display.update()

    grupo_heroi.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

        heroi.processar_evento(e)