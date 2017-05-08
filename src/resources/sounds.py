import pygame
from src.resources.gameobjects import GameObject


class Sound(GameObject):
    def __init__(self, filepath):
        pygame.mixer.Sound(filepath)
