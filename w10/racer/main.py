import random
import pygame

# инициализация pygame
pygame.init()

# размеры окна
WIDTH = 520
HEIGHT = 780
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Street Racer")

clock = pygame.time.Clock()

# цвета
WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
BLUE = (70, 130, 255)
RED = (230, 70, 70)
PURPLE = (170, 100, 255)
YELLOW = (255, 210, 70)

BG_TOP = (18, 20, 28)
BG_BOTTOM = (28, 32, 44)
ROAD = (42, 42, 50)
ROAD_EDGE = (210, 210, 220)
LANE = (235, 235, 235)

# шрифты
font = pygame.font.SysFont("Arial", 24, bold=True)
small_font = pygame.font.SysFont("Arial", 18)
title_font = pygame.font.SysFont("Arial", 44, bold=True)

# параметры дороги
ROAD_X = 80
ROAD_WIDTH = WIDTH - 160
LANES = 3
LANE_WIDTH = ROAD_WIDTH // LANES

road_offset = 0


# фон градиент
def draw_gradient():
    for y in range(HEIGHT):
        t = y / HEIGHT
        r = int(BG_TOP[0] * (1 - t) + BG_BOTTOM[0] * t)
        g = int(BG_TOP[1] * (1 - t) + BG_BOTTOM[1] * t)
        b = int(BG_TOP[2] * (1 - t) + BG_BOTTOM[2] * t)
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))


# центр полосы
def lane_center(lane):
    return ROAD_X + lane * LANE_WIDTH + LANE_WIDTH // 2


# позиция по полосе
def lane_x(lane, width):
    return lane_center(lane) - width // 2


# ===== МАШИНА =====
class Car:
    def __init__(self, lane, y, color, is_player=False):
        self.width = 56
        self.height = 108
        self.lane = lane
        self.x = lane_x(lane, self.width)
        self.y = y
        self.color = color
        self.is_player = is_player

    # обновить позицию при смене полосы
    def update_lane(self):
        self.x = lane_x(self.lane, self.width)

    # хитбокс
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    # рисование машины
    def draw(self):
        # тень
        shadow = pygame.Surface((self.width + 16, self.height + 16), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow, (0, 0, 0, 70),
                            (0, self.height - 4, self.width + 16, 20))
        screen.blit(shadow, (self.x - 8, self.y))

        # кузов
        body = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, body, border_radius=12)

        # кабина
        cabin = pygame.Rect(self.x + 8, self.y + 15, self.width - 16, 30)
        pygame.draw.rect(screen, (30, 34, 44), cabin, border_radius=8)

        # стекло
        glass = pygame.Rect(self.x + 12, self.y + 20, self.width - 24, 16)
        pygame.draw.rect(screen, (170, 215, 255), glass, border_radius=6)

        # колёса
        pygame.draw.rect(screen, BLACK, (self.x - 4, self.y + 20, 6, 20), border_radius=3)
        pygame.draw.rect(screen, BLACK, (self.x + self.width - 2, self.y + 20, 6, 20), border_radius=3)
        pygame.draw.rect(screen, BLACK, (self.x - 4, self.y + self.height - 40, 6, 20), border_radius=3)
        pygame.draw.rect(screen, BLACK, (self.x + self.width - 2, self.y + self.height - 40, 6, 20), border_radius=3)


# ===== МОНЕТА =====
class Coin:
    def __init__(self):
        self.radius = 12
        self.reset()

    # случайная позиция
    def reset(self):
        self.lane = random.randint(0, LANES - 1)
        self.x = lane_center(self.lane)
        self.y = random.randint(-600, -100)
        self.value = random.choice([1, 1, 2])

    # хитбокс
    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                           self.radius * 2, self.radius * 2)

    # рисование монеты
    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, (255, 235, 160), (self.x - 2, self.y - 2), self.radius - 4)
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius, 2)

        text = small_font.render(str(self.value), True, BLACK)
        screen.blit(text, text.get_rect(center=(self.x, self.y)))


# ===== ДОРОГА =====
def draw_road():
    pygame.draw.rect(screen, ROAD, (ROAD_X, 0, ROAD_WIDTH, HEIGHT))

    pygame.draw.line(screen, ROAD_EDGE, (ROAD_X, 0), (ROAD_X, HEIGHT), 4)
    pygame.draw.line(screen, ROAD_EDGE, (ROAD_X + ROAD_WIDTH, 0),
                     (ROAD_X + ROAD_WIDTH, HEIGHT), 4)

    for lane in range(1, LANES):
        x = ROAD_X + lane * LANE_WIDTH
        for y in range(-80, HEIGHT + 80, 80):
            pygame.draw.rect(screen, LANE, (x - 3, y + road_offset, 6, 40))


# ===== HUD =====
def draw_hud(coins, distance, level, speed):
    screen.blit(font.render(f"Coins: {coins}", True, WHITE), (20, 20))
    screen.blit(font.render(f"Dist: {distance}", True, WHITE), (150, 20))
    screen.blit(font.render(f"Level: {level}", True, WHITE), (280, 20))
    screen.blit(font.render(f"Speed: {speed}", True, WHITE), (400, 20))


# ===== GAME RESET =====
def reset_game():
    global player, enemies, coins_list
    global coins_collected, distance, level
    global enemy_speed, road_speed, game_over

    player = Car(1, HEIGHT - 150, BLUE, True)

    enemies = [
        Car(random.randint(0, LANES - 1), -200, RED),
        Car(random.randint(0, LANES - 1), -500, PURPLE),
    ]

    coins_list = [Coin()]

    coins_collected = 0
    distance = 0
    level = 1
    game_over = False

    enemy_speed = 4
    road_speed = 5


reset_game()

# ===== GAME LOOP =====
running = True
while running:
    clock.tick(60)

    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # управление
        if event.type == pygame.KEYDOWN and not game_over:

            if event.key == pygame.K_LEFT and player.lane > 0:
                player.lane -= 1
                player.update_lane()

            if event.key == pygame.K_RIGHT and player.lane < LANES - 1:
                player.lane += 1
                player.update_lane()

        # рестарт
        if game_over and event.key == pygame.K_r:
            reset_game()

    # фон
    draw_gradient()
    draw_road()

    if not game_over:

        distance += 1

        # уровень и скорость
        level = 1 + distance // 400
        enemy_speed = 4 + level - 1
        road_speed = enemy_speed + 1

        road_offset += road_speed
        if road_offset > 80:
            road_offset = 0

        # движение врагов
        for enemy in enemies:
            enemy.y += enemy_speed
            if enemy.y > HEIGHT:
                enemy.lane = random.randint(0, LANES - 1)
                enemy.update_lane()
                enemy.y = random.randint(-600, -100)

        # движение монет
        for coin in coins_list:
            coin.y += road_speed
            if coin.y > HEIGHT:
                coin.reset()

        # добавление монет
        if len(coins_list) < 2:
            coins_list.append(Coin())

        # столкновения
        player_rect = player.rect()

        for enemy in enemies:
            if player_rect.colliderect(enemy.rect()):
                game_over = True

        for coin in coins_list:
            if player_rect.colliderect(coin.rect()):
                coins_collected += coin.value
                coin.reset()

        # рисование
        player.draw()
        for enemy in enemies:
            enemy.draw()
        for coin in coins_list:
            coin.draw()

        draw_hud(coins_collected, distance, level, enemy_speed)

    else:
        # game over экран
        player.draw()
        for enemy in enemies:
            enemy.draw()

        draw_hud(coins_collected, distance, level, enemy_speed)

        text = title_font.render("GAME OVER", True, RED)
        screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    pygame.display.flip()

pygame.quit()