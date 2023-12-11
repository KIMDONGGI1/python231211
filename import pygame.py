import pygame
import sys
import random

# 초기화
pygame.init()

# 게임 창 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("블록깨기 게임")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# 패들 설정
paddle_width, paddle_height = 100, 10
paddle_x = width // 2 - paddle_width // 2
paddle_y = height - 20

# 공 설정
ball_radius = 10
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 5 * random.choice([-1, 1])
ball_speed_y = 5

# 블록 설정
block_width, block_height = 50, 20
blocks = []
for row in range(5):
    for col in range(width // block_width):
        block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
        blocks.append(block)

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    paddle_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    paddle_x = max(0, min(width - paddle_width, paddle_x))

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과 충돌 처리
    if ball_x <= 0 or ball_x >= width:
        ball_speed_x *= -1

    if ball_y <= 0:
        ball_speed_y *= -1

    # 패들과 충돌 처리
    if (
        paddle_x <= ball_x <= paddle_x + paddle_width
        and paddle_y <= ball_y <= paddle_y + paddle_height
    ):
        ball_speed_y *= -1

    # 블록과 충돌 처리
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
            blocks.remove(block)
            ball_speed_y *= -1

    # 그리기
    screen.fill(white)
    pygame.draw.rect(screen, blue, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, red, (int(ball_x), int(ball_y)), ball_radius)

    for block in blocks:
        pygame.draw.rect(screen, black, block)

    pygame.display.flip()
    clock.tick(60)
