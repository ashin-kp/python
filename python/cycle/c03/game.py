import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 0, 255)
ENEMY_COLOR = (255, 0, 0)
FONT_COLOR = (0, 0, 0)

# Player setup
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# Enemy setup
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = 0
enemy_speed = 5

# Score & lives
score = 0
missed = 0
max_score = 10
max_missed = 3

# Font
font = pygame.font.SysFont("Arial", 30)

# Clock
clock = pygame.time.Clock()

# Game loop control
running = True
game_over = False
win = False

while running:
    clock.tick(30)  # 30 FPS
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Key press
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed

        # Move enemy
        enemy_y += enemy_speed

        # Check collision
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

        if player_rect.colliderect(enemy_rect):
            score += 1
            enemy_x = random.randint(0, WIDTH - enemy_size)
            enemy_y = 0
        elif enemy_y > HEIGHT:
            missed += 1
            enemy_x = random.randint(0, WIDTH - enemy_size)
            enemy_y = 0

        # Win/Lose check
        if score >= max_score:
            game_over = True
            win = True
        elif missed >= max_missed:
            game_over = True

        # Draw player and enemy
        pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
        pygame.draw.rect(screen, ENEMY_COLOR, enemy_rect)

        # Draw score
        score_text = font.render(f"Score: {score}", True, FONT_COLOR)
        missed_text = font.render(f"Missed: {missed}", True, FONT_COLOR)
        screen.blit(score_text, (10, 10))
        screen.blit(missed_text, (10, 40))

    else:
        # Game Over Screen
        if win:
            msg = font.render("🎉 You Win!", True, (0, 150, 0))
        else:
            msg = font.render("💥 You Lose!", True, (200, 0, 0))
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - msg.get_height()//2))
        restart_msg = font.render("Press R to Restart or Q to Quit", True, FONT_COLOR)
        screen.blit(restart_msg, (WIDTH//2 - restart_msg.get_width()//2, HEIGHT//2 + 40))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Reset game
            score = 0
            missed = 0
            enemy_x = random.randint(0, WIDTH - enemy_size)
            enemy_y = 0
            game_over = False
            win = False
        elif keys[pygame.K_q]:
            running = False

    pygame.display.update()

pygame.quit()
