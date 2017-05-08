import pygame


def main():
    # TODO: Main Game Loop
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()


if __name__ == '__main__':
    main()
