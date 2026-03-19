import pygame
import random

# start pygame
pygame.init()

# screen size
width = 600
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the Falling Balls")

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

# paddle
paddle_width = 100
paddle_height = 15
paddle_x = width//2 - paddle_width//2
paddle_y = height - 40
paddle_speed = 7

# ball
ball_radius = 10
ball_x = random.randint(20, width-20)
ball_y = 0
ball_speed = 4

# score
score = 0
font = pygame.font.SysFont(None, 36)

# clock
clock = pygame.time.Clock()

running = True

while running:

    clock.tick(60)

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed

    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed

    # keep paddle inside screen
    if paddle_x < 0:
        paddle_x = 0

    if paddle_x > width - paddle_width:
        paddle_x = width - paddle_width

    # ball falling
    ball_y += ball_speed

    # collision detection
    if ball_y + ball_radius >= paddle_y and ball_x >= paddle_x and ball_x <= paddle_x + paddle_width:
        score += 1
        ball_x = random.randint(20, width-20)
        ball_y = 0

    # if ball missed
    if ball_y > height:
        ball_x = random.randint(20, width-20)
        ball_y = 0

    # drawing
    screen.fill(white)

    pygame.draw.rect(screen, blue, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10,10))

    pygame.display.update()

pygame.quit()