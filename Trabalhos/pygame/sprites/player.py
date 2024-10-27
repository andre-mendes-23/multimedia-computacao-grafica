# Nome do ficheiro: sprites/player.py
# Descrição: Este ficheiro define a classe Player, que representa um jogador do jogo.~

# Importa a biblioteca pygame
import pygame

# Importa constantes de configuração do módulo settings.py
from settings import WIDTH, HEIGHT, GREEN

# Define a classe Player como uma subclasse pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):

    def __init__(self, speed):

        """
        Método construtor que inicia a classe Player.

        Argumentos:
            speed: Velocidade do jogador.
        """

        # Chama o construtor da classe pai (Sprite)
        super().__init__()

        # Cria uma superfície para o jogador com uma transparência
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)

        # Desenha um triângulo verde para representar o jogador
        pygame.draw.polygon(self.image, GREEN, [(0, 50), (25, 0), (50, 50)])

        # Obtém o retângulo delimitador da superfície do jogador
        self.rect = self.image.get_rect()

        # Define a posição inicial do jogador no centro da largura e 50 pixels acima da borda inferior da tela
        self.rect.center = (WIDTH // 2, HEIGHT - 50)

        # Define a velocidade do jogador
        self.speed = speed

    def update(self):
        
        """
        Método para atualizar a posição do jogador a partir da tecla pressionada.
        
        """

        # Captura o estado das teclas pressionadas
        keys = pygame.key.get_pressed()

        # Verifica se a tecla esquerda foi pressionada
        if keys[pygame.K_LEFT]:

            # Move o jogador para a esquerda pela velocidade definida
            self.rect.x -= self.speed
        # Verifica se a tecla direita foi pressionada
        if keys[pygame.K_RIGHT]:

            # Move o jogador para a direita pela velocidade definida
            self.rect.x += self.speed