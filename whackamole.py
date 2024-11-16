import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        x = 0
        y = 0
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if  (event.pos[0] >= 32*x and event.pos[0] <= 32*x+32) and (event.pos[1] >= 32*y and event.pos[1] <= 32*y+32):
                        x = random.randrange(0, 20)
                        y = random.randrange(0, 16)
            screen.fill("light blue")
            for i in range(1,20):
                pygame.draw.line(screen, "dark blue", (32*i, 0),(32*i, 512))
            for i in range(1,16):
                pygame.draw.line(screen, "blue", (0, 32*i), (640, 32*i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x*32, y*32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
