import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
RAIN_WIDTH = 10
RAIN_HEIGHT = 20

PLAYER_VELOCITY = 10
RAIN_VELOCITY = 3

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, rain_drops):
    WIN.blit(BG,(0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10,10))

    pygame.draw.rect(WIN, "red", player)

    for rain in rain_drops:
        pygame.draw.rect(WIN, "white", rain)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    rain_add_increment = 2000
    rain_count = 0

    rain_drops = []
    hit = False


    while run:
        rain_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if rain_count > rain_add_increment:
            for _ in range(3):
                rain_x = random.randint(0, WIDTH - RAIN_WIDTH)
                rain = pygame.Rect(rain_x, -RAIN_HEIGHT, RAIN_WIDTH, RAIN_HEIGHT)
                rain_drops.append(rain)

            rain_add_increment = max(200, rain_add_increment -50)
            rain_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY

        for rain in rain_drops[:]:
            rain.y += RAIN_VELOCITY
            if rain.y > HEIGHT:
                rain_drops.remove(rain)
            elif rain.y + rain.height >= player.y and rain.colliderect(player):
                rain_drops.remove(rain)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, rain_drops)

    pygame.quit()

if __name__ == "__main__":
    main()