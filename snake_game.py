import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Mouse Controlled")
clock = pygame.time.Clock()
speed = 10
score = 0

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initial snake setup
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (CELL_SIZE, 0)

# Generate initial food location
food = (random.randrange(0, WIDTH, CELL_SIZE),
        random.randrange(0, HEIGHT, CELL_SIZE))

def draw_rect(color, position):
    pygame.draw.rect(screen, color, (*position, CELL_SIZE, CELL_SIZE))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Determine direction based on mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    head_x, head_y = snake[0]
    dx = mouse_x - head_x
    dy = mouse_y - head_y
    if abs(dx) > abs(dy):
        direction = (CELL_SIZE if dx > 0 else -CELL_SIZE, 0)
    else:
        direction = (0, CELL_SIZE if dy > 0 else -CELL_SIZE)

    # Calculate new head position
    new_head = (head_x + direction[0], head_y + direction[1])

    # Check for wall collision
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake):
        running = False
        continue

    # Move snake
    snake.insert(0, new_head)

    # Check for food collision
    if new_head == food:
        score += 1
        speed += 1
        food = (random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE))
    else:
        snake.pop()

    # Draw everything
    screen.fill(BLACK)
    draw_rect(RED, food)
    for pos in snake:
        draw_rect(GREEN, pos)

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
