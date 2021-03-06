import pygame, math
from sprite import Sprite
from sprite_controlled import SpriteControlled
from Scene import Scene
global current_scene

def main():

    # Load
    global current_scene
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.mouse.set_visible(False)
    quit_game = False

    level00 = Scene("background.png", "ground.png")
    level01 = Scene("background.png", "ground1.png")
    scenes = {}
    scenes["level00"] = level00
    scenes["level01"] = level01
    current_scene = level00

    def change_scene(name):
        global current_scene
        current_scene = scenes[name]

    while not quit_game:
        # Inputs
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game = True
        current_scene.inputs(events)

        # Update
        current_scene.update(change_scene)
        
        # Draw
        screen.fill((0, 0, 0))
        current_scene.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()