"""
Nome do ficheiro: menu.py
Descrição: Este ficheiro que contém as funcionalidades do menu do jogo

Criado em: 13/10/2024
Autor: André Mendes
"""

# Importação da biblioteca Pygame
import pygame

# Importação da biblioteca pandas
import pandas as pd

# Importação das configurações necessárias
from settings import BLACK, GREEN, WHITE, WINDOW_WIDTH, FONT

# Criação da classe Menu
class Menu:
    def __init__(self):
        """
        Construtor da classe Menu que define as opções do menu.
        """
        # Inicializa a lista que armazena as opções disponíveis no menu
        self.options = ["Start Game", "High Scores", "Quit"]

        # Inicialização da variável que armazenará a opção selecionada
        self.selected_option = 0

    def draw_menu(self, screen):
        """
        Define o método que exibe o menu no ecrã.
        """

        # Preenche a tela com uma cor preta
        screen.fill(BLACK)

        # Cria um objeto Fonte para o título do jogo no menu
        title_font = pygame.font.SysFont(FONT, 60)

        # Cria um objeto Fonte para as opções do menu
        option_font = pygame.font.SysFont(FONT, 40)
