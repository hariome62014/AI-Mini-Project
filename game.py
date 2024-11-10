import pygame
import random
import math
import time

# Initialize pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fuzzy Logic Chase Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Player settings
player_pos = [width // 2, height // 2]
player_size = 30
player_speed = 5

# Enemy settings
enemy_pos = [random.randint(0, width), random.randint(0, height)]
enemy_size = 30
enemy_speed = 2

# Fuzzy Logic Parameters for Enemy Behavior
def fuzzy_speed(distance):
    # Adjust speed based on distance to player
    if distance < 100:
        return 5  # Aggressive
    elif distance < 200:
        return 3  # Cautious
    else:
        return 1  # Passive

# Start time for survival score
start_time = time.time()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < width - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < height - player_size:
        player_pos[1] += player_speed

    # Calculate distance between enemy and player
    distance = math.sqrt((enemy_pos[0] - player_pos[0]) ** 2 + (enemy_pos[1] - player_pos[1]) ** 2)
    
    # Set enemy speed based on fuzzy logic
    enemy_speed = fuzzy_speed(distance)
    
    # Move enemy towards player
    if enemy_pos[0] < player_pos[0]:
        enemy_pos[0] += enemy_speed
    elif enemy_pos[0] > player_pos[0]:
        enemy_pos[0] -= enemy_speed

    if enemy_pos[1] < player_pos[1]:
        enemy_pos[1] += enemy_speed
    elif enemy_pos[1] > player_pos[1]:
        enemy_pos[1] -= enemy_speed

    # Draw player and enemy
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    # Display player and enemy names
    font = pygame.font.Font(None, 36)
    nirjay_text = font.render("Nirjay", True, BLACK)
    attacker_text = font.render("Attacker", True, BLACK)
    screen.blit(nirjay_text, (player_pos[0], player_pos[1] - 30))
    screen.blit(attacker_text, (enemy_pos[0], enemy_pos[1] - 30))

    # Calculate and display survival time as score
    survival_time = int(time.time() - start_time)
    score_text = font.render(f"Score: {survival_time} seconds", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Check for collision
    if distance < (player_size + enemy_size) / 2:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over!", True, BLACK)
        screen.blit(text, (width // 2 - 150, height // 2 - 50))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    # Update the screen
    pygame.display.flip()
    clock.tick(30)

pygame.quit()



