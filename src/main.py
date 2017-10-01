import pygame
import src.config

def main():
    # TODO: Main Game Loop
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()

    config = load_config()

    pygame.display.set_mode(config.display)
    director = src.resources.Director()



def load_config():
    config = src.config.Config()

    return config


if __name__ == '__main__':
    main()
