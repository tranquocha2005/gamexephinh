# import pygame

# pygame.init()
# WIDTH = 300
# HEIGHT = 600
# GRID_SIZE = 30
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GRAY = (128, 128, 128)
# RED = (255, 0, 0)
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("TETRIS")
# clock = pygame.time.Clock()


# # // vẽ lưới
# def draw_grid():
#     for x in range(0, WIDTH, GRID_SIZE):
#         pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
#     for y in range(0, HEIGHT, GRID_SIZE):
#         pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))


# def draw_khoi(x, y):
#     pygame.draw.rect(screen, RED, (x, y, GRID_SIZE, GRID_SIZE))
#     pygame.draw.rect(screen, RED, (x + GRID_SIZE, y, GRID_SIZE, GRID_SIZE))
#     pygame.draw.rect(screen, WHITE, (x, y + GRID_SIZE, GRID_SIZE, GRID_SIZE))
#     pygame.draw.rect(screen, RED, (x + GRID_SIZE, y + GRID_SIZE, GRID_SIZE, GRID_SIZE))


# khoi_x = 120
# khoi_y = 0
# fall_speed = 5


# running = True
# while running:
#     screen.fill(BLACK)
#     draw_grid()
#     khoi_y += fall_speed
#     if khoi_y + 2 * GRID_SIZE > HEIGHT:
#         khoi_y = HEIGHT - 2 * GRID_SIZE

#     draw_khoi(khoi_x, khoi_y)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT and khoi_x - GRID_SIZE >=0:
#                 khoi_x-=GRID_SIZE
#             elif event.key == pygame.K_RIGHT and khoi_x +  2*GRID_SIZE < WIDTH:
#                 khoi_x+=GRID_SIZE    
#     pygame.display.flip()
#     clock.tick(20)
# pygame.quit()



import pygame

pygame.init()
WIDTH = 300
HEIGHT = 600
GRID_SIZE = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TETRIS")
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def draw_khoi(x, y):
    pygame.draw.rect(screen, RED, (x, y, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (x + GRID_SIZE, y, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, WHITE, (x, y + GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (x + GRID_SIZE, y + GRID_SIZE, GRID_SIZE, GRID_SIZE))

khoi_x = 120
khoi_y = 0
fall_speed = 5
da_cham_dat = False  # Biến kiểm tra khối đã chạm đáy chưa

running = True
while running:
    screen.fill(BLACK)
    draw_grid()
    # Chỉ cho khối rơi nếu chưa chạm đáy
    if not da_cham_dat:
        khoi_y += fall_speed
    # Kiểm tra nếu khối chạm đáy
    if khoi_y + 2 * GRID_SIZE >= HEIGHT:
        khoi_y = HEIGHT - 2 * GRID_SIZE
        da_cham_dat = True  # Đánh dấu khối đã chạm đáy

    draw_khoi(khoi_x, khoi_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and khoi_x - GRID_SIZE >= 0:  
                khoi_x -= GRID_SIZE
            elif event.key == pygame.K_RIGHT and khoi_x + 2 * GRID_SIZE < WIDTH:  
                khoi_x += GRID_SIZE

    pygame.display.flip()
    clock.tick(20)

pygame.quit()