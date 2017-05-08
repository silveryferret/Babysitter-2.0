from unittest import TestCase
from src.resources import images, sounds, resourcemanager
import pygame


class TestResourceManager(TestCase):
    def setUp(self):
        self.manager = resourcemanager.ResourceManager()

    @classmethod
    def setUpClass(cls):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        screen = pygame.display.set_mode((800, 600))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def test_noimagepath(self):
        with self.assertRaises(resourcemanager.NoFilePath):
            self.manager.load_image('')

    def test_wrongiamgepath(self):
        with self.assertRaises(resourcemanager.NoFilePath):
            self.manager.load_image('../resources/images/NoImageHere.png')

    def test_load_image(self):
        img = self.manager.load_image('../resources/images/TestImage.png')
        self.assertIsInstance(img, images.Image, "Image loaded is an Image instance")

    def test_nosoundpath(self):
        with self.assertRaises(resourcemanager.NoFilePath):
            self.manager.load_sound('')

    def test_wrongsoundpath(self):
        with self.assertRaises(resourcemanager.NoFilePath):
            self.manager.load_sound('../resources/sounds/NoSoundHere.ogg')

    def test_load_sound(self):
        sound = self.manager.load_sound('../resources/sounds/TestSound.ogg')
        self.assertIsInstance(sound, sounds.Sound)
