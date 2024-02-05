import pygame
import pygame.gfxdraw


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    screen.fill(('white'))
    pygame.font.init()

    font = pygame.font.SysFont("Comic Sans MS", 24)
    text = font.render("Tekst w \"pygame\"", False, [128, 64, 255])
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
        screen.blit(text, [0, 0])
        pygame.quit()


if __name__ == "__main__":
    main()