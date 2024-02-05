import pygame
import pygame.gfxdraw


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    screen.fill(('white'))

    try:
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == "q":
                    break
            pygame.display.flip()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()