# Nome do ficheiro: settings.py
# Descrição: Este ficheiro contém as definições para um jogo desenvolvido em Pygame.

# Importa a biblioteca pygame
import pygame

# Define uma constante para o nome do jogo
GAME_TITLE = "Aventura Espacial"

# Define uma constante para a largura da janela do jogo
WIDTH = 800

# Define uma constante para a altura da janela do jogo
HEIGHT = 600

# Define uma constante para a velocidade do jogo
FPS = 60

# Define uma constante que cria um relogio para o jogo
CLOCK = pygame.time.Clock()

# Define uma constante para o nome da fonte utilizada no jogo
FONT_NAME = 'arial'

# Define uma constante para o tamanho da fonte utilizada no jogo
FONT_SIZE = 30

# Define uma constante para o tamanho da fonte do texto dos botões do jogo
BUTTON_FONT_SIZE = 25

# Define uma constante para a cor do fundo do jogo como preto no formato RGB
BACKGROUND_COLOR = (0, 0, 0)

# Define uma constante para a cor dos textos do jogo como branco no formato RGB
TEXT_COLOR = (255, 255, 255)

# Define uma constante para a cor dos botões do jogo como azul no formato RGB
BUTTON_COLOR = (50, 150, 50)

# Define uma constante para a cor dos textos dos botões do jogo como branco no formato RGB
BUTTON_TEXT_COLOR = (255, 255, 255)

# Define uma constante com um dicionário para os textos do menu principal do jogo
MAIN_MENU_TEXTS = {
    "title": "Bem-vindo ao jogo 'Aventura Espacial' ",
    "play": "Jogar",
    "settings": "Definições",
    "highscores": "Melhores Pontuações",
    "instructions": "Instruções",
    "quit": "Sair",
}

# Define uma constante com um dicionário para os textos do menu de definições do jogo
SETTINGS_MENU_TEXTS = {
    "title": "Definições do Jogo",
    "difficulty": "Dificuldade",
    "back": "Voltar",
}

# Define uma constante com um dicionário para os textos da janela de instruções do jogo
INSTRUCTIONS_MENU_TEXTS = {
    "title": "Instruções do Jogo",
    "text": "Utilize as setas para movimentar o personagem e a barra de espaco para atirar.",
    "back": "Voltar",
}

# Define uma constante com um dicionário para os textos da janela de melhores pontuações do jogo
HIGHSCORES_MENU_TEXTS = {
    "title": "Melhores Pontuações",
    "back": "Voltar",
}

# Define uma constante com um dicionário para os textos da janela de fim de jogo
GAME_OVER_MENU_TEXTS = {
    "title": "Perdeste o Jogo!",
    "score": "Pontos",
    "back": "Voltar",
}

# Define uma constante com um dicionário para os textos da janela de vitória do jogo
VICTORY_MENU_TEXTS = {
    "title": "Venceste o Jogo!",
    "score": "Pontos",
    "back": "Voltar",
}

# Define uma constante para apresentar o texto das vidas do jogador no jogo
PLAYER_LIVES_TEXT = "Vidas: "

# Define uma constante para apresentar o texto da pontuação do jogador no jogo
PLAYER_SCORE_TEXT = "Pontuação: "

# Define uma constante com uma dicionário com as definições de cada nível de dificuldade do jogo
DIFFICULTY_SETTINGS = {
    "easy": {"meteors": 5, "lives": 11, "points_to_level": 5000, "points_per_meteor": 1000, "ship_speed": 5, "meteor_speed": 2, "bullet_speed": 10},
    "medium": {"meteors": 15, "lives": 8, "points_to_level": 15000, "points_per_meteor": 1000, "ship_speed": 6, "meteor_speed": 3, "bullet_speed": 12},
    "hard": {"meteors": 30, "lives": 5, "points_to_level": 30000, "points_per_meteor": 1000, "ship_speed": 7, "meteor_speed": 4, "bullet_speed": 14},
}

# Define uma constante com um nome do ficheiro das pontuações do jogo
SCORES_FILE = "scores.csv"

# Define uma constante com o caminho do ficheiro da imagem da nave espacial
SPACESHIP_IMAGE = "spaceship.png"

# Define uma constante com o caminho do ficheiro da imagem do meteoro
METEOR_IMAGE = "meteor.png"