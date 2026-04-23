import pygame

# Инициализация библиотеки pygame
pygame.init()

# Размер окна программы
WIDTH, HEIGHT = 900, 700

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Таймер для ограничения FPS
clock = pygame.time.Clock()

# Основные цвета
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GRAY = (200, 200, 200)
DARK = (40, 40, 40)

# Палитра цветов для выбора
COLORS = [
    (0, 0, 0),      # черный
    (255, 0, 0),    # красный
    (0, 200, 0),    # зеленый
    (0, 0, 255),    # синий
    (255, 255, 0),  # желтый
    (255, 0, 255),  # фиолетовый
    (0, 255, 255),  # голубой
]

# Создаем поверхность для рисования (canvas)
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)  # заполняем белым цветом

# Текущий выбранный цвет
current_color = BLACK

# Размер кисти
brush_size = 5

# Режим рисования
# brush - кисть
# rect - прямоугольник
# circle - круг
# eraser - ластик
mode = "brush"

# Флаг рисования
drawing = False

# Начальная точка фигуры
start_pos = None

# Шрифт для текста интерфейса
font = pygame.font.SysFont("Arial", 20)


# Функция для отрисовки панели инструментов
def draw_ui():
    # верхняя панель
    pygame.draw.rect(screen, DARK, (0, 0, WIDTH, 50))

    # отображение доступных цветов
    for i, c in enumerate(COLORS):
        pygame.draw.rect(screen, c, (10 + i * 40, 10, 30, 30))

    # текст с подсказками управления
    text = font.render(
        "B:Brush R:Rect C:Circle E:Eraser +/- Size X:Clear",
        True,
        (255, 255, 255)
    )
    screen.blit(text, (350, 15))


# Основной игровой цикл программы
running = True
while running:

    # отображаем холст
    screen.blit(canvas, (0, 0))

    # рисуем интерфейс
    draw_ui()

    # обработка событий
    for event in pygame.event.get():

        # закрытие окна
        if event.type == pygame.QUIT:
            running = False

        # нажатие кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos  # запоминаем начальную точку

            # проверка выбора цвета
            for i, c in enumerate(COLORS):
                rect = pygame.Rect(10 + i * 40, 10, 30, 30)
                if rect.collidepoint(event.pos):
                    current_color = c

        # отпускание кнопки мыши
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            # рисование прямоугольника
            if mode == "rect" and start_pos:
                pygame.draw.rect(
                    canvas,
                    current_color,
                    (
                        start_pos[0],
                        start_pos[1],
                        event.pos[0] - start_pos[0],
                        event.pos[1] - start_pos[1]
                    ),
                    2
                )

            # рисование круга
            if mode == "circle" and start_pos:
                radius = int(
                    (
                        (event.pos[0] - start_pos[0]) ** 2 +
                        (event.pos[1] - start_pos[1]) ** 2
                    ) ** 0.5
                )

                pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

        # обработка нажатий клавиатуры
        if event.type == pygame.KEYDOWN:

            # режим кисти
            if event.key == pygame.K_b:
                mode = "brush"

            # режим прямоугольника
            elif event.key == pygame.K_r:
                mode = "rect"

            # режим круга
            elif event.key == pygame.K_c:
                mode = "circle"

            # режим ластика
            elif event.key == pygame.K_e:
                mode = "eraser"

            # увеличение размера кисти
            elif event.key == pygame.K_EQUALS:
                brush_size += 2

            # уменьшение размера кисти
            elif event.key == pygame.K_MINUS:
                brush_size = max(2, brush_size - 2)

            # очистка холста
            elif event.key == pygame.K_x:
                canvas.fill(WHITE)

    # рисование кистью
    if drawing and mode == "brush":
        pygame.draw.circle(canvas, current_color, pygame.mouse.get_pos(), brush_size)

    # работа ластика (рисует белым цветом)
    if drawing and mode == "eraser":
        pygame.draw.circle(canvas, WHITE, pygame.mouse.get_pos(), brush_size)

    # обновление экрана
    pygame.display.flip()

    # ограничение до 60 FPS
    clock.tick(60)

# завершение работы pygame
pygame.quit()