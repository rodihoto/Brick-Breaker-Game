import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brick Breaker")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)  # Define red color
gray = (50, 50, 50)  # Background color for the score and screens

# Paddle
paddle_width, paddle_height = 100, 20
paddle = pygame.Rect(width // 2 - paddle_width // 2, height - 50, paddle_width, paddle_height)

# Ball
ball = pygame.Rect(width // 2 - 15, height // 2 - 15, 30, 30)
ball_speed_x, ball_speed_y = 7, -7

# Bricks
brick_list = [pygame.Rect(5 + i * 110, 5 + j * 35, 100, 30) for j in range(5) for i in range(7)]

# Score
score = 0
font = pygame.font.Font(None, 36)

def show_start_screen():
    screen.fill(black)
    text = font.render("Press any key to start", True, white)
    text_rect = text.get_rect(center=(width / 2, height / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def show_game_over_screen():
    screen.fill(black)
    text1 = font.render("Game Over", True, white)
    text1_rect = text1.get_rect(center=(width / 2, height / 2 - 30))
    screen.blit(text1, text1_rect)
    text2 = font.render(f"Final Score: {score}", True, white)
    text2_rect = text2.get_rect(center=(width / 2, height / 2 + 10))
    screen.blit(text2, text2_rect)
    pygame.display.flip()
    pygame.time.delay(3000)

# Start Screen
show_start_screen()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-10, 0)
    if keys[pygame.K_RIGHT] and paddle.right < width:
        paddle.move_ip(10, 0)

    # Move the ball
    ball.move_ip(ball_speed_x, ball_speed_y)

    # Collisions with walls
    if ball.left <= 0 or ball.right >= width:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.bottom >= height:
        running = False  # Ball hit bottom wall

    # Collisions with paddle
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # Collision with bricks
    for brick in brick_list[:]:
        if ball.colliderect(brick):
            ball_speed_y *= -1
            brick_list.remove(brick)
            score += 10  # Increase score by 10 for each brick

    # Drawing
    screen.fill(black)
    pygame.draw.rect(screen, white, paddle)
    pygame.draw.ellipse(screen, red, ball)  # Draw the ball in red
    for brick in brick_list:
        pygame.draw.rect(screen, white, brick)
    # Display score with background
    score_text = font.render(f'Score: {score}', True, white)
    score_rect = score_text.get_rect(center=(width / 2, height - 30))
    pygame.draw.rect(screen, gray, score_rect)  # Draw background for score
    screen.blit(score_text, score_rect)  # Blit the score text on the background

    pygame.display.flip()
    pygame.time.delay(30)

# Game Over Screen
show_game_over_screen()

pygame.quit()
sys.exit()
