import pygame

# p - parede
# <space> - area em branco

mapa = [
    "pppppppppppppppppppppppppppppppppppppppp",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",                                
    "pppppppppppppppppppppppppppppppppppppppp"
]

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
TELA_WIDTH = 800
TELA_HEIGHT = 600

BLK_WIDTH = TELA_WIDTH / 40
BLK_HEIGHT = TELA_HEIGHT / 20

pygame.init()
tela = pygame.display.set_mode((TELA_WIDTH, TELA_HEIGHT))

tiles = pygame.image.load("./data/basictiles_2.png").convert_alpha()
img_grama_orig = tiles.subsurface((16, 128), (16, 16))
img_grama = pygame.transform.scale(img_grama_orig, (BLK_WIDTH, BLK_HEIGHT))
img_parede_orig = tiles.subsurface((48, 0), (16,16))
img_parede = pygame.transform.scale(img_parede_orig, (BLK_WIDTH, BLK_HEIGHT))

for id_linha, linha in enumerate(mapa):
    for id_coluna, caracter in enumerate(linha):
        x = id_coluna * BLK_WIDTH
        y = id_linha * BLK_HEIGHT
        if caracter == 'p':
            tela.blit(img_parede, (x, y))
        else:
            tela.blit(img_grama , (x, y))

pygame.display.update()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()