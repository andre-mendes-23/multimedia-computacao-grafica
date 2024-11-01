# Nome do ficheiro: settings.py
# Descrição do ficheiro: Este ficheiro contém as configurações globais de um jogo com Pygame

# Importa as biblioteca pygame
import pygame

# Define uma constante para guardar o título do jogo
GAME_TITLE = "Jogo de Tiro Avançado"

# Define duas constantes para guardar a largura e a altura da janela do jogo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define uma constante para guardar a taxa de frames por segundo (FPS)
FPS = 60

# Define uma constanste para controlar a taxa de frames do jogo através do objeto do Pygame, Clock
CLOCK = pygame.time.Clock()

# Define constantes para guardar a configuração de cada cor do jogo no formato RGB
WHITE = (255, 255, 255) # Cor branca
BLACK = (0, 0, 0) # Cor preta
RED = (255, 0, 0) # Cor vermelha
GREEN = (0, 255, 0) # Cor verde
BLUE = (0, 0, 255) # Cor azul
YELLOW = (255, 255, 0) # Cor amarela

# Define um dicionário para armazenar as configurações de cada dificuldade do jogo
DIFFICULTY_SETTINGS = {
    "Easy": { # Configurações da dificuldade "Easy"
        "lives": 10, # Número de vidas iniciais do jogador na dificuldade
        "bullets": 40, # Número de balas disponíveis para o jogador disparar
        "bullet_speed": 5, # Velocidade das balas disparadas pelo jogador
        "player_speed": 4, # Velocidade do jogador
        "enemy_speed": 2, # Velocidade dos inimigos
        "enemy_count": 15, # Número de inimigos da dificuldade
        "points_per_enemy": 333, # Pontos ganhos pelo jogador por matar um inimigo
        "points_to_win": 5000 # Número de pontos necessários para vencer o jogo
    },
    "Medium": { # Configurações da dificuldade "Medium"
        "lives": 6, # Número de vidas iniciais do jogador na dificuldade
        "bullets": 35, # Número de balas disponíveis para o jogador disparar
        "bullet_speed": 6, # Velocidade das balas disparadas pelo jogador
        "player_speed": 5, # Velocidade do jogador
        "enemy_speed": 3, # Velocidade dos inimigos
        "enemy_count": 20, # Número de inimigos da dificuldade
        "points_per_enemy": 375, # Pontos ganhos pelo jogador por matar um inimigo
        "points_to_win": 7500 # Número de pontos necessários para vencer o jogo
    },
    "Hard": { # Configurações da dificuldade "Hard"
        "lives": 4, # Número de vidas iniciais do jogador na dificuldade
        "bullets": 30, # Número de balas disponíveis para o jogador disparar
        "bullet_speed": 7, # Velocidade das balas disparadas pelo jogador   
        "player_speed": 6, # Velocidade do jogador    
        "enemy_speed": 4, # Velocidade dos inimigos
        "enemy_count": 25, # Número de inimigos da dificuldade
        "points_per_enemy": 400, # Pontos ganhos pelo jogador por matar um inimigo
        "points_to_win": 10000 # Número de pontos necessários para vencer o jogo
    },
}

# Define uma constante para guardar o nome do ficheiro onde os pontos do jogador serão guardados
SCORES_FILE = "scores.csv"