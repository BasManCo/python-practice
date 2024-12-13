import pygame
pygame.font.init()

WIDTH, HEIGHT = 1000, 800

FONT = pygame.font.SysFont("comicsans", 30)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Selector Screen')

def draw(button):

    select_text = FONT.render("Select Game", 1, "white")
    WIN.blit(select_text, (WIDTH / 2 - select_text.get_width() / 2, HEIGHT / 2 - select_text.get_height() / 2))
    WIN.blit()
    pygame.display.update()

def main():
    run = True

    while run:

        button = pygame.Rect(200, 600, 50, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(button)

    pygame.quit()