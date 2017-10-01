import json
from src.resources.gameobjects import GameObject

display = (1280, 720)  # TODO: Move this out of Director file and into some sort of config file


class Director(GameObject):
    def __init__(self, resource_manager):
        self.manager = resource_manager
        self.characters = {}
        self.music = {}
        self.sfx = {}
        self.backgrounds = {}

    def load_resources(self, resource_script):
        resource_script = open(resource_script, "r")
        resources = json.load(resource_script)
        self.characters = resources["Characters"]
        self.music = resources["Music"]
        self.backgrounds = resources["Backgrounds"]

    def direct_script(self, string):
        # 'Test (Image) = 1'
        base, expression, position = string.split(' ')
        expression = expression.strip('()')
        path = '../resources/images/' + base + expression + '.png'
        img = self.manager.load_image(path)
        position = int(position) - 1
        self.find_position_of_image(img, display, position)
        list_of_gameobjects = [img]
        return list_of_gameobjects

    def find_position_of_image(self, img, page, position):
        page_width_in_pixels = page[0]
        image_width_in_pixels = img.img.get_width()
        left_edge_of_image = (position / 4) * (page_width_in_pixels - image_width_in_pixels)
        img.pos = (left_edge_of_image, 0)
