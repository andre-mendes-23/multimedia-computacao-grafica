# Nome do ficheiro: sprites/bullet.py
# Descrição: Este ficheiro define a classe Bullet que representa uma bala do jogador.

# Importa a biblioteca pygame
import pygame

# Importa constantes de configuração do módulo settings.py
from settings import RED

# Define a classe Bullet como uma subclasse pygame.sprite.Sprite
class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, speed):
        
        """
        Método construtor que inicia a classe Bullet.

        Argumentos:
            x: Posição X da bala.
            y: Posição Y da bala.
            speed: Velocidade da bala.
        """

        # Chama o construtor da classe pai (Sprite)
        super().__init__()

        # Cria uma superfície para a bala com uma transparência
        self.image = pygame.Surface((5, 10), pygame.SRCALPHA)

        # Desenha um retângulo vermelho para representar a bala
        pygame.draw.rect(self.image, RED, (0, 0, 5, 10))

        # Obtém o retângulo delimitador da superfície da bala
        self.rect = self.image.get_rect()

        # Obtém o retângulo da imagem da bala e centra-o na posição
        self.rect = self.image.get_rect(center=(x, y))

        # Define a velocidade da bala
        self.speed = speed

    def update(self):
        
        """
        Método para atualizar a posição da bala a partir da tecla pressionada.
        """

        # Move a bala para cima pela velocidade definida
        self.rect.y -= self.speed

        # Remove a bala se ela sair da tela
        if self.rect.bottom < 0:
            self.kill()