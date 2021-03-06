import pygame, sys
from sprite_controlled import SpriteControlled
from sprite import Sprite
from warp import Warp

class Scene:
    
    def __init__(self, background_file, ground_file):
        self.background = Sprite(0, 0, background_file, False)
        self.ground = Sprite(0, 0, ground_file, False)
        screen_w, screen_h = pygame.display.get_surface().get_size()
        ground_height = screen_h - self.ground.surface.get_height()
        self.ground.y = ground_height
        self.player = SpriteControlled(150, ground_height, 'Sprite.png', True, 2)
        self.copain = SpriteControlled(500, ground_height, 'copain.png', True, 0)
        self.cursor = Sprite(0, 0, 'cursor.jpg', False)
        #self.collision_text = font.render("Oops sorry Mamen", False,(0, 0,0))
        self.warp = Warp(700, 0, 'warp.png', False, "level01")
        self.warp.y = ground_height - self.warp.surface.get_height() / 2

    def load(self):
        pass

    def inputs(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                self.player.move_to(mouse_click[0])

    def update(self, change_scene):
        self.cursor.set_position(pygame.mouse.get_pos())
        self.player.update()
        if(self.player.intersects(self.warp)):
            
            change_scene(self.warp.to_scene)

        #if(self.player.intersects(self.copain)):
            #screen.blit(self.collision_text,(self.copain_x, self.copain_y - 100))

            

    def draw(self, screen):
        self.background.draw(screen)
        self.ground.draw(screen)
        self.warp.draw(screen)
        self.player.draw(screen)
        self.cursor.draw(screen)
        self.copain.draw(screen)