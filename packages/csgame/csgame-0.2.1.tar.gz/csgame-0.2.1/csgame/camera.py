"""
simple cameras
"""

import pygame

class CameraGroup(pygame.sprite.Group):
    """
    sprite group which has a camera tracking a target

    # Demo
    ```
    import pygame
    import csgame.player
    import csgame.camera

    pygame.init()
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    screen_sprites = csgame.camera.CameraGroup() # sprites visible on the screen
    collide_sprites = pygame.sprite.Group() # sprites player can collide with

    class Floor(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__([screen_sprites, collide_sprites])
            self.image = pygame.image.load("white.png")
            self.image = pygame.transform.scale(self.image, (window.get_width()/1.5, 50))
            self.rect = self.image.get_rect()
            self.rect.bottomleft = (0, window.get_height())

    Floor()

    player = csgame.player.SideScrollerPlayer(
        (window.get_width()/2, window.get_height()/2),   # start at middle of screen
        pygame.image.load("player.png").convert_alpha(), # a player image
        (150, 150),                                      # 150x150 size player
        150,                                             # moves 150 pixels per second
        [screen_sprites],                                 
        collide_sprites,
        csgame.player.SideScrollPlayerControls.wasd_arrow_keys(),
        5,    # 5 pixels/second**2
        200,  # 200 pixels/second initial jump speed
        1000  # 1000 pixels/second max speed
    )

    while 1: # (main game loop)
        [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
        clock.tick(60)

        fps = clock.get_fps()
        if fps == 0: fps = 9999999

        window.fill(pygame.Color(0, 0, 0))

        screen_sprites.camera_draw(player)
        screen_sprites.update(1 / fps)

        pygame.display.update()
    ```
    """
    def __init__(self):
        super().__init__()

        self.screen = pygame.display.get_surface()
    
    def camera_draw(self, target: pygame.sprite.Sprite):
        """draw the group, with the target in the centre of the screen"""
        offset = pygame.math.Vector2(
            self.screen.get_width()/2 - target.rect.centerx,
            self.screen.get_height()/2 - target.rect.centery
        )

        for sprite in self.sprites():
            self.screen.blit(sprite.image, sprite.rect.topleft + offset)