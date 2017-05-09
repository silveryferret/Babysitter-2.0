from unittest import TestCase
from src.resources import resourcemanager
import pygame, time


class TestImage(TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()

    def setUp(self):
        self.manager = resourcemanager.ResourceManager()
        pygame.display.set_mode((800, 600))
        self.test_screen = pygame.Surface((800, 600))
        self.test_img = pygame.image.load('../resources/images/TestImage.png').convert_alpha()
        self.test_screen.blit(self.test_img, (20, 20))

    def test_image_is_same(self):
        img = self.manager.load_image('../resources/images/TestImage.png')
        img.position((20, 20))
        screen = pygame.Surface((800, 600))
        img.draw(screen)
        our_buffer = screen.get_buffer().raw
        test_buffer = self.test_screen.get_buffer().raw
        self.assertEqual(test_buffer, our_buffer)
