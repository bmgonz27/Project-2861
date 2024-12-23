import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Capybara GO")

player_pos = [1, 1]
dungeon = [
    "########",
    "#......#",
    "#.####.#",
    "#......#",
    "########"
]

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= 1
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += 1
            elif event.key == pygame.K_UP:
                player_pos[1] -= 1
            elif event.key == pygame.K_DOWN:
                player_pos[1] += 1

    screen.fill((0, 0, 0))

    for y, row in enumerate(dungeon):
        for x, tile in enumerate(row):
                if tile == "#":
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)
                pygame.draw.rect(screen, color, pygame.Rect(x * 50, y * 50, 50, 50))

    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(player_pos[0] * 50, player_pos[1] * 50, 50, 50))

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
    
