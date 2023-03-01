import pygame

from classes import *
# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

# Create the paddles and ball objects
player_paddle = Paddle(50, 250)
ai_paddle     = Paddle(screen_width - 70, 250)
ball          = Ball(screen_width,screen_height)

# Set up the clock and scoring variables
clock = pygame.time.Clock()
player_score = 0
ai_score = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_paddle.move_up()
    if keys[pygame.K_DOWN]:
        player_paddle.move_down()

    # Update the game state
    ball.update(player_paddle, ai_paddle)
    ai_paddle.update(ball)
    
    # Check for scoring
    if ball.rect.left < 0:
        ai_score += 1
        ball.reset()
    if ball.rect.right > screen_width:
        player_score += 1
        ball.reset()

    # Check for game over
    if player_score == 5 or ai_score == 5:
        running = False

    # Inside the game loop:
    if player_score == 5:
        print("Player wins!")
        running = False
    if ai_score == 5:
        print("AI wins!")
        running = False



    # Draw the game board and objects
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (screen_width / 2, 0), (screen_width / 2, screen_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), player_paddle)
    pygame.draw.rect(screen, (255, 255, 255), ai_paddle)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# End the game
pygame.quit()


