import pygame
from random import randrange

#Config do Jogo
pygame.init()
pygame.display.set_caption("Jogo da cobrinha")
largura = 1200
altura = 700
tela = pygame.display.set_mode((largura, altura))
tempo = pygame.time.Clock()

#Cores / RGB
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
branco = (255, 255, 255)
azul = (135, 206, 235)

#Cobrinha
tamanho_quadrado = 25
velocidade_atualizacao = 12

#Gerar comida
def gerar_comida():
    comida_x = round(randrange(0, largura - tamanho_quadrado) / 25.0) * 25.0
    comida_y = round(randrange(0, altura - tamanho_quadrado) / 25.0) * 25.0
    return comida_x, comida_y

#Desenhar comida
def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.circle(tela, vermelho, [comida_x + 10, comida_y + 10], 10)

#Desenhar pontuação
def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Impact", 25)
    texto = fonte.render(f"Pontos: {pontuacao}", True, branco)
    tela.blit(texto, [15, 10])

#Desenhar cobra
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, azul, [pixel[0], pixel[1], tamanho, tamanho,])

#Controles
def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0

    return velocidade_x, velocidade_y 

#funçaõ rodar jogo
def rodar_jogo():
    fim_jogo = False

    x = altura / 2
    y = largura /2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()
        
    while not fim_jogo:

        #Fundo
        tela.fill(preto)
        fundo = pygame.image.load("grade.png")
        novo_fundo = pygame.transform.scale(fundo, (1400, 700))
        tela.blit(novo_fundo, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_jogo = True
            elif event.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(event.key)

        #desenhar comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        #Atualizar a posição da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        x += velocidade_x
        y += velocidade_y

        #desenhar cobra
        pixels.append([x, y])
        if len (pixels) > tamanho_cobra:
            del pixels[0]
            
        #Se a cobra bater nela mesma    
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        desenhar_cobra(tamanho_quadrado, pixels) 

        desenhar_pontuacao(tamanho_cobra - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
        tempo.tick(velocidade_atualizacao)          
rodar_jogo()

