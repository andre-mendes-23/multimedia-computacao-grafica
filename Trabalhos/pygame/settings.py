# Nome do ficheiro: settings.py
# Descrição: Este ficheiro contém as configurações globais do jogo "Space Shooter 2D"~

# Importar a biblioteca pygame
import pygame

# Nome do jogo
GAME_NAME = "Space Shooter 2D"

# Dimensões da tela
SCREEN_WIDTH = 800  # Largura da janela do jogo em pixels.
SCREEN_HEIGHT = 600  # Altura da janela do jogo em pixels.

# Cores
WHITE = (255, 255, 255)  # Cor branca em formato RGB.
BLACK = (0, 0, 0)  # Cor preta em formato RGB.
RED = (255, 0, 0)  # Cor vermelha em formato RGB.
GREEN = (0, 255, 0)  # Cor verde em formato RGB.
BLUE = (0, 0, 255)  # Cor azul em formato RGB.
YELLOW = (255, 255, 0)  # Cor amarela em formato RGB.
PURPLE = (128, 0, 128)  # Cor roxa em formato RGB.

# FPS
FPS = 60  # Taxa de quadros por segundo para o jogo.

# Clock
CLOCK = pygame.time.Clock()

# Fonte do jogo
FONT_NAME = "Arial"  # Fonte a ser utilizada no texto do jogo.

# Configurações do jogador
PLAYER_SPEED = 5  # Velocidade do jogador em pixels por frame.
BULLET_SPEED = 10  # Velocidade das balas em pixels por frame.
ENEMY_SPEED = 2  # Velocidade dos inimigos em pixels por frame.
ENEMY_SPAWN_RATE = 30  # Número de frames para o surgimento de um novo inimigo.
INITIAL_LIVES = 3  # Número inicial de vidas do jogador.

# Dificuldades
DIFFICULTY_SETTINGS = {  # Dicionário contendo as configurações para diferentes níveis de dificuldade.
    "Easy": {"enemy_speed": 1, "points_needed": 1000, "wave_size": 5, "max_waves": 10},  # Configurações para dificuldade fácil.
    "Medium": {"enemy_speed": 1.5, "points_needed": 3000, "wave_size": 7, "max_waves": 12},  # Configurações para dificuldade média.
    "Hard": {"enemy_speed": 2, "points_needed": 5000, "wave_size": 10, "max_waves": 15},  # Configurações para dificuldade difícil.
}