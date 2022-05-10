import pygame

#Inicializando o Pygame
pygame.init()

width = 600
height = 600

#Criando janela
display = pygame.display.set_mode([width, height])
pygame.display.set_caption("Meu jogo 01")

gameloop = True 

#Agrupa todos os Spritesheets
drawGroup = pygame.sprite.Group()

#Inserindo spritesheets

#Player
guy = pygame.sprite.Sprite(drawGroup)
guy.image = pygame.image.load("data/player.png") #16x16
guy.image = pygame.transform.scale(guy.image, [100,100])
guy.rect = pygame.Rect(250,250,100,100)

#Inimigo
enemy = pygame.sprite.Sprite(drawGroup)
enemy.image = pygame.image.load("data/enemy.png") 
enemy.image = pygame.transform.scale(enemy.image, [100,100])
enemy.rect = pygame.Rect(0,0,100,100)

#Looping do game
while gameloop:
    #Lista de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        
    #Outra lista de eventos, mas que pode ser usada várias vezes
    #Retorna True ou False para a tecla apertada
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        guy.rect.x += 2
    elif keys[pygame.K_a]:
        guy.rect.x -= 2
    elif keys[pygame.K_w]:
        guy.rect.y -= 2
    elif keys[pygame.K_s]:
        guy.rect.y += 2

    #Desenha na tela "draw"
    display.fill([139,69,19])

    #Imprime na tela os spritesheets
    drawGroup.draw(display)

    pygame.display.update()

