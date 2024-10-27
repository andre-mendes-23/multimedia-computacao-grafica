# Nome do ficheiro: settings.py
# Descrição: Este ficheiro contém as variáveis de configuração do jogo "Jogo de Tiro".

# Importa a biblioteca pygame
import pygame

# Define o título da janela do jogo
GAME_TITLE = "Jogo de Tiro"

# Define a largura e altura da janela em pixels
WIDTH = 800
HEIGHT = 600

# Define a taxe de frames por segundo
FPS = 60

# Define um objeto Clock para controlar o tempo de jogo
CLOCK = pygame.time.Clock()

# Define a paleta de cores do jogo no formato RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define um dicionário que guarda as configurações de cada nível de dificuldade do jogo
DIFFICULTY_SETTINGS = {
    "Easy": { # Configurações para o nível de dificuldade Easy
        "lives": 10, # Quantidade de vidas iniciais
        "points_to_win": 5000, # Pontos necessários para vencer o jogo e passar para o próximo nível
        "bullets": 40, # Quantidade de balas do jogador disponíveis
        "enemies": 15, # Número de inimigos no nível
        "enemy_speed": 2, # Velocidade dos inimigos
        "bullet_speed": 5, # Velocidade das balas disparadas pelo jogador
        "player_speed": 4, # Velocidade do jogador
        "points_por_enemy": 333 # Pontos por inimigo
    },
    "Medium": { # Configurações para o nível de dificuldade Medium
        "lives": 6, # Quantidade de vidas iniciais
        "points_to_win": 7500, # Pontos necessários para vencer o jogo e passar para o próximo nível
        "bullets": 35, # Quantidade de balas do jogador disponíveis
        "enemies": 20, # Número de inimigos no nível
        "enemy_speed": 3, # Velocidade dos inimigos
        "bullet_speed": 6, # Velocidade das balas disparadas pelo jogador
        "player_speed": 5, # Velocidade do jogador
        "points_por_enemy": 375 # Pontos por inimigo
    },
    "Hard": { # Configurações para o nível de dificuldade Hard
        "lives": 4, # Quantidade de vidas iniciais
        "points_to_win": 10000, # Pontos necessários para vencer o jogo e passar para o próximo nível
        "bullets": 30, # Quantidade de balas do jogador disponíveis
        "enemies": 25, # Número de inimigos no nível
        "enemy_speed": 4, # Velocidade dos inimigos
        "bullet_speed": 7, # Velocidade das balas disparadas pelo jogador
        "player_speed": 6, # Velocidade do jogador
        "points_por_enemy": 400 # Pontos por inimigo
    }
}

# Define o nome do ficheiro onde as pontuacões do jogo ficam guardadas
SCORE_FILE = "scores.csv"