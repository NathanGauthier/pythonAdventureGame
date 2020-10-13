class Level00(Scene):


    def __init__(self, background_file, ground_file):
        Scene.__init__(self, background_file, ground_file)
        screen_h = pygame.display.get_surface().get_size()
        ground_height = screen_h - self.ground.surface.get_height()
        self.ground.y = ground_height
        self.player = SpriteControlled(10,ground_height, 'Sprite.png', True, 2)
        self.cursor = Sprite(0, 0, 'cursor.jpg', False)
        self.warp = Warp(700, 0, 'warp.png', False, "level01")
        self.warp.y = ground_height - self.warp.surface.get_height() / 2      
