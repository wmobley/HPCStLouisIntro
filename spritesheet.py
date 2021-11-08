import pygame
import json

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()

        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()




    def get_sprite(self, x, y, w, h, z=4):
        sprite = pygame.Surface((w, h))


        sprite.blit(self.sprite_sheet,(0, 0),(x, y, w, h))
        sprite = pygame.transform.rotozoom(sprite, 0, z)
        sprite.set_colorkey((90, 156, 247))
        return sprite

    def parse_sprite(self, name, z=4):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h, z)
        self.x = self.data['frames'][name]["location"]['x']
        self.y = self.data['frames'][name]["location"]['y']
        return image

