import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da Tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Aventura Espacial")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
YELLOW = (200, 200, 0)
GRAY = (100, 100, 100)

# Frame Rate
FPS = 60
clock = pygame.time.Clock()

# Fontes
FONT_SMALL = pygame.font.SysFont("Arial", 24)
FONT_LARGE = pygame.font.SysFont("Arial", 48)

# Imagens e Sprites (Desenhados do Zero)
def draw_player(x, y):
    pygame.draw.polygon(SCREEN, BLUE, [(x, y), (x - 20, y + 30), (x + 20, y + 30)])

def draw_enemy(x, y):
    pygame.draw.rect(SCREEN, RED, (x, y, 40, 40))

def draw_asteroid(x, y, size):
    pygame.draw.circle(SCREEN, GRAY, (x, y), size)

def draw_projectile(x, y):
    pygame.draw.rect(SCREEN, YELLOW, (x, y, 5, 10))

def draw_resource(x, y):
    pygame.draw.circle(SCREEN, GREEN, (x, y), 10)

# Classes do Jogo
class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 60
        self.speed = 5
        self.lives = 3
        self.score = 0
        self.projectiles = []

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.x -= self.speed
            if self.x < 20:
                self.x = 20
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.x += self.speed
            if self.x > SCREEN_WIDTH - 20:
                self.x = SCREEN_WIDTH - 20
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            self.y -= self.speed
            if self.y < 20:
                self.y = 20
        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            self.y += self.speed
            if self.y > SCREEN_HEIGHT - 20:
                self.y = SCREEN_HEIGHT - 20

    def shoot(self):
        projectile = Projectile(self.x, self.y)
        self.projectiles.append(projectile)

    def update_projectiles(self):
        for projectile in self.projectiles[:]:
            projectile.move()
            if projectile.y < 0:
                self.projectiles.remove(projectile)

    def draw(self):
        draw_player(self.x, self.y)
        for projectile in self.projectiles:
            projectile.draw()

class Enemy:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - 40)
        self.y = -40
        self.speed = random.randint(2, 5)

    def move(self):
        self.y += self.speed

    def draw(self):
        draw_enemy(self.x, self.y)

class Asteroid:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = -20
        self.size = random.randint(10, 30)
        self.speed = random.randint(1, 3)

    def move(self):
        self.y += self.speed

    def draw(self):
        draw_asteroid(self.x, self.y, self.size)

class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 7

    def move(self):
        self.y -= self.speed

    def draw(self):
        draw_projectile(self.x, self.y)

class Resource:
    def __init__(self):
        self.x = random.randint(20, SCREEN_WIDTH - 20)
        self.y = random.randint(20, SCREEN_HEIGHT - 200)

    def draw(self):
        draw_resource(self.x, self.y)

# Funções Auxiliares
def check_collision(x1, y1, x2, y2, size=20):
    distance = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
    return distance < size

def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    SCREEN.blit(surface, (x, y))

def game_over_screen(player):
    SCREEN.fill(BLACK)
    draw_text("GAME OVER", FONT_LARGE, RED, SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50)
    draw_text(f"Score: {player.score}", FONT_SMALL, WHITE, SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2 + 10)
    draw_text("Press R to Restart or Q to Quit", FONT_SMALL, WHITE, SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2 + 50)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def victory_screen(player):
    SCREEN.fill(BLACK)
    draw_text("VICTORY!", FONT_LARGE, GREEN, SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50)
    draw_text(f"Score: {player.score}", FONT_SMALL, WHITE, SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2 + 10)
    draw_text("Press R to Restart or Q to Quit", FONT_SMALL, WHITE, SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2 + 50)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def main():
    # Inicializar Jogador e Listas de Objetos
    player = Player()
    enemies = []
    asteroids = []
    resources = [Resource()]
    enemy_spawn_event = pygame.USEREVENT + 1
    asteroid_spawn_event = pygame.USEREVENT + 2
    resource_spawn_event = pygame.USEREVENT + 3
    pygame.time.set_timer(enemy_spawn_event, 2000)
    pygame.time.set_timer(asteroid_spawn_event, 3000)
    pygame.time.set_timer(resource_spawn_event, 5000)

    running = True
    while running:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
            if event.type == enemy_spawn_event:
                enemies.append(Enemy())
            if event.type == asteroid_spawn_event:
                asteroids.append(Asteroid())
            if event.type == resource_spawn_event:
                resources.append(Resource())

        # Atualizar Jogador
        player.move(keys_pressed)
        player.update_projectiles()

        # Atualizar Inimigos
        for enemy in enemies[:]:
            enemy.move()
            if enemy.y > SCREEN_HEIGHT:
                enemies.remove(enemy)
            # Checar colisão com jogador
            if check_collision(player.x, player.y, enemy.x + 20, enemy.y + 20):
                player.lives -= 1
                enemies.remove(enemy)
                if player.lives <= 0:
                    game_over_screen(player)

        # Atualizar Asteroides
        for asteroid in asteroids[:]:
            asteroid.move()
            if asteroid.y > SCREEN_HEIGHT:
                asteroids.remove(asteroid)
            # Checar colisão com jogador
            if check_collision(player.x, player.y, asteroid.x, asteroid.y, asteroid.size):
                player.lives -= 1
                asteroids.remove(asteroid)
                if player.lives <= 0:
                    game_over_screen(player)

        # Atualizar Projetos
        for projectile in player.projectiles[:]:
            for enemy in enemies[:]:
                if check_collision(projectile.x, projectile.y, enemy.x + 20, enemy.y + 20):
                    player.score += 100
                    player.projectiles.remove(projectile)
                    enemies.remove(enemy)
                    break

        # Atualizar Recursos
        for resource in resources[:]:
            if check_collision(player.x, player.y, resource.x, resource.y, size=15):
                player.score += 200
                resources.remove(resource)

        # Verificar Condição de Vitória
        if player.score >= 1000:
            victory_screen(player)

        # Desenhar Tudo
        SCREEN.fill(BLACK)
        player.draw()

        for enemy in enemies:
            enemy.draw()
        for asteroid in asteroids:
            asteroid.draw()
        for resource in resources:
            resource.draw()

        # Desenhar UI
        draw_text(f"Score: {player.score}", FONT_SMALL, WHITE, 10, 10)
        draw_text(f"Lives: {player.lives}", FONT_SMALL, WHITE, 10, 40)

        pygame.display.flip()

if __name__ == "__main__":
    main()
