from unittest import TestCase
from src.resources import resourcemanager
import pygame


class TestImage(TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()

    def setUp(self):
        self.manager = resourcemanager.ResourceManager()
        self.screen = pygame.display.set_mode((800, 600))
        self.test_img = pygame.image.load('../resources/images/TestImage.png')
        self.test_surf = self.test_img.blit(self.screen, (20, 20))

    def test_image_is_same(self):
        img = self.manager.load_image('../resources/images/TestImage.png')
        our_surf = img.draw(self.screen, (20, 20))
        our_buffer = our_surf.get_buffer().raw
        test_buffer = self.screen.get_buffer().raw
        self.assertEqual(test_buffer, our_buffer)
