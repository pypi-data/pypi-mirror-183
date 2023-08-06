"""
classes to provide player movement
"""
from __future__ import annotations
import pygame

class Player(pygame.sprite.Sprite):
    """base player class that can't do anything"""
    def __init__(self, start_pos: tuple[float, float], image: pygame.Surface, 
                 player_size: tuple(float, float), speed: float,
                 groups: pygame.sprite.Group, collide_group: pygame.sprite.Group):
        """
        `groups`: sprite groups the player is in
        `collide_group`: sprite group that the player can collide with
        """
        super().__init__(groups)
        self.image = pygame.transform.scale(image, player_size)
        self.rect = self.image.get_rect(center = start_pos)

        self.pos: pygame.math.Vector2 = pygame.math.Vector2(start_pos)
        self.speed: float = speed

        self.collide_group: pygame.sprite.Group = collide_group
    
    def update(self, dt: float) -> None:
        """called once per frame to update the player"""
        pass

    def _collide(self) -> bool:
        """returns whether a collision happened or not"""
        for collide_sprite in self.collide_group:
            if self.rect.colliderect(collide_sprite.rect):
                return True
        return False


class TopDownPlayerControls(dict):
    """
    specifies the keys that need to be pressed 
    for the top down player's actions

    # Example
    ```
    import pygame
    import csgame

    controls = csgame.player.TopDownPlayerControls(
        [pygame.K_w, pygame.K_UP],
        [pygame.K_s, pygame.K_DOWN],
        [pygame.K_a, pygame.K_LEFT],
        [pygame.K_d, pygame.K_RIGHT]
    )
    ```
    """
    def __init__(self, up_keys: list[int], down_keys: list[int],
                 left_keys: list[int], right_keys: list[int]):
        """
        the `keys` should be given as a list of integers
        representing pygame keys
        """
        self["up"] = up_keys
        self["down"] = down_keys
        self["left"] = left_keys
        self["right"] = right_keys
    
    def wasd() -> TopDownPlayerControls:
        """return a WASD TopDownPlayerControls"""
        return TopDownPlayerControls(
            [pygame.K_w],
            [pygame.K_s],
            [pygame.K_a],
            [pygame.K_d]
        )
    
    def arrow_keys() -> TopDownPlayerControls:
        """return a typical arrow key TopDownPlayerControls"""
        return TopDownPlayerControls(
            [pygame.K_UP],
            [pygame.K_DOWN],
            [pygame.K_LEFT],
            [pygame.K_RIGHT]
        )
    
    def wasd_arrow_keys() -> TopDownPlayerControls:
        """return a TopDownPlayerControls for both
        WASD and arrow keys"""
        return TopDownPlayerControls(
            [pygame.K_w, pygame.K_UP],
            [pygame.K_s, pygame.K_DOWN],
            [pygame.K_a, pygame.K_LEFT],
            [pygame.K_d, pygame.K_RIGHT]
        )

class TopDownPlayer(Player):
    """
    top-down player controls

    # Demo
    ```
    import pygame
    import csgame.player

    pygame.init()
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    screen_sprites = pygame.sprite.Group() # sprites visible on the screen
    collide_sprites = pygame.sprite.Group() # sprites player can collide with

    player = csgame.player.TopDownPlayer(
        (window.get_width()/2, window.get_height()/2),   # start at middle of screen
        pygame.image.load("player.png").convert_alpha(), # a player image
        (150, 150),                                      # 150x150 size player
        150,                                             # moves 150 pixels per second
        [screen_sprites],                                 
        collide_sprites,
        csgame.player.TopDownPlayerControls.wasd_arrow_keys()
    )

    while 1: # (main game loop)
        [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
        clock.tick(60)

        fps = clock.get_fps()
        if fps == 0: fps = 9999999

        window.fill(pygame.Color(0, 0, 0))

        screen_sprites.draw(window)
        screen_sprites.update(1 / fps)

        pygame.display.update()
    ```
    """
    def __init__(self, start_pos: tuple[float, float], image: pygame.Surface,
                 player_size: tuple[float, float], speed: float,
                 groups: pygame.sprite.Group, collide_group: pygame.sprite.Group,
                 controls: TopDownPlayerControls):
        super().__init__(start_pos, image, player_size, speed, groups, collide_group)

        self.controls: TopDownPlayerControls = controls
    
    def update(self, dt: float) -> None:
        self._move(dt)
    
    def _move(self, dt: float) -> None:
        """player input to move player"""
        direction = pygame.math.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        up = any([keys[key] for key in self.controls["up"]])
        down = any([keys[key] for key in self.controls["down"]])
        left = any([keys[key] for key in self.controls["left"]])
        right = any([keys[key] for key in self.controls["right"]])

        if up == down:
            direction.y = 0
        elif up:
            direction.y = -1
        else:
            direction.y = 1
        
        if left == right:
            direction.x =  0
        elif left:
            direction.x = -1
        else:
            direction.x = 1

        if direction.x != 0 and direction.y != 0:
            direction = direction.normalize()
        
        self._update_position(direction, dt)
    
    def _update_position(self, direction: pygame.math.Vector2, dt: float) -> None:
        """tries to update position in given direction"""
        old_x = self.pos.x
        self.pos.x += direction.x * self.speed * dt 
        self.rect.center = self.pos
        if self._collide():
            self.pos.x = old_x
            self.rect.center = self.pos
        
        old_y = self.pos.y
        self.pos.y += direction.y * self.speed * dt 
        self.rect.center = self.pos
        if self._collide():
            self.pos.y = old_y
            self.rect.center = self.pos

class SideScrollPlayerControls(dict):
    """
    specifies the keys that need to be pressed 
    for the side scroll player's actions

    # Example
    ```
    import pygame
    import csgame

    controls = csgame.player.TopDownPlayerControls(
        [pygame.K_a, pygame.K_LEFT],
        [pygame.K_d, pygame.K_RIGHT],
        [pygame.K_SPACE]
    )
    ```
    """
    def __init__(self, left_keys: list[int], right_keys: list[int], jump_keys: list[int]):
        """
        the `keys` should be given as a list of integers
        representing pygame keys
        """
        self["left"] = left_keys
        self["right"] = right_keys
        self["jump"] = jump_keys
    
    def wasd() -> SideScrollPlayerControls:
        """return WASD SideScrollPlayerControls"""
        return SideScrollPlayerControls(
            [pygame.K_a],
            [pygame.K_d],
            [pygame.K_SPACE]
        )
    
    def arrow_keys() -> SideScrollPlayerControls:
        """return arrow keys SideScrollPlayerControls"""
        return SideScrollPlayerControls(
            [pygame.K_LEFT],
            [pygame.K_RIGHT],
            [pygame.K_SPACE]
        )
    
    def wasd_arrow_keys() -> SideScrollPlayerControls:
        """return a SideScrollPlayerControls for both
        WASD and arrow keys"""
        return SideScrollPlayerControls(
            [pygame.K_a, pygame.K_LEFT],
            [pygame.K_d, pygame.K_RIGHT],
            [pygame.K_SPACE]
        )

class SideScrollerPlayer(Player):
    """
    side scroller player controls

    # Demo
    ```
    import pygame
    import csgame.player

    pygame.init()
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    screen_sprites = pygame.sprite.Group() # sprites visible on the screen
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

        screen_sprites.draw(window)
        screen_sprites.update(1 / fps)

        pygame.display.update()
    ```
    """
    def __init__(self, start_pos: tuple[float, float], image: pygame.Surface, 
                player_size: tuple(float, float), speed: float,
                groups: pygame.sprite.Group, collide_group: pygame.sprite.Group,
                controls: SideScrollPlayerControls, 
                gravity: float, jump_speed: float, terminal_velocity: float):
        """`gravity` to be given as a float for acceleration due to gravity
        (pixels/second**2)

        `jump_speed` is the initial speed of a jump

        `terminal velocity` is the maximum speed the player can fall"""
        super().__init__(start_pos, image, player_size, speed, groups, collide_group)

        self.controls = controls

        self.y_velocity: float = 0
        self.gravity: float = gravity
        self.jump_velocity: float = -jump_speed
        self.terminal_velocity: float = terminal_velocity

        self.grounded: bool = False
    
    def update(self, dt: float) -> None:
        self._apply_gravity()
        self._move(dt)
    
    def _apply_gravity(self) -> None:
        if self.grounded: self.y_velocity = 0
        self.y_velocity += self.gravity
    
    def _move(self, dt) -> None:
        """move the player"""
        x_direction = 0
        keys = pygame.key.get_pressed()
        left = any([keys[key] for key in self.controls["left"]])
        right = any([keys[key] for key in self.controls["right"]])
        if left == right:
            x_direction = 0
        elif left:
            x_direction = -1
        else:
            x_direction = 1
        
        self._update_x(x_direction, dt)

        if self.grounded and any([keys[key] for key in self.controls["jump"]]):
            self.y_velocity = self.jump_velocity
            self.grounded = False
        
        self._update_y(dt)
        
    def _update_x(self, x_direction: int, dt: float) -> None:
        """update x position"""
        old_x = self.pos.x
        self.pos.x += x_direction * self.speed * dt
        self.rect.center = self.pos
        if self._collide():
            self.pos.x = old_x
            self.rect.center = self.pos
    
    def _update_y(self, dt: float) -> None:
        """update y position"""
        old_y = self.pos.y
        self.pos.y += self.y_velocity * dt
        self.rect.center = self.pos
        if self._collide():
            self.pos.y = old_y
            self.rect.center = self.pos
            if self.y_velocity > 0 and not self.grounded: # was falling when collided
                self.grounded = True
        else:
            self.grounded = False # no collisions - can't be on the floor