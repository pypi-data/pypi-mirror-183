"""
special colour classes with unique behaviour
"""
from __future__ import annotations
import pygame

class Colour(pygame.Color):
    """base colour class, just represents a colour"""
    def __init__(self, red: int, green: int, blue: int, alpha: int = 255):
        super().__init__(red, green, blue, alpha)
    
    def set_colour(self, colour: Colour):
        self.r = colour.r
        self.g = colour.g
        self.b = colour.b
        self.a = colour.a

    def __add__(self, other: Colour) -> Colour:
        return Colour(
            self.r + other.r,
            self.g + other.g,
            self.b + other.b,
            self.a + other.a
        )

    def update(self, dt: float) -> None:
        """called once per frame\n
        
        `dt`: time between current and last frame
        (typically 1/FPS)"""
        pass

class BiColour(Colour):
    """
    colour which can switch between two colours

    # examples

    ```
    import pygame
    import csgame

    c = csgame.colour.BiColour(
        pygame.Color(255, 0, 0, 255), # red
        pygame.Color(0, 0, 255, 255)  # blue
    )

    # switch the colour from red to blue
    c.cycle()

    # switch the colour from blue to red
    c.cycle()
    ```
    """
    def __init__(self, start_colour: Colour, other_colour: Colour):
        self.start_colour: Colour = start_colour
        self.other_colour: Colour = other_colour

        self.set_colour(start_colour)
    
    def cycle(self):
        """switch between the two colours `once`"""
        if self == self.start_colour:
            self.set_colour(self.other_colour)
        else:
            self.set_colour(self.start_colour)

class BiColourSmooth(BiColour):
    """
    BiColour but with a smooth transition between the two colours

    # example

    ```
    import pygame
    import csgame

    c = csgame.colour.BiColourSmooth(
        csgame.colour.Colour(255, 0, 0, 255), # red
        csgame.colour.Colour(0, 0, 255, 255), # blue
        2 # 2 second transition
    )

    # -- at some point in the program --
    c.cycle()

    # -- in main game loop --
    while 1: # (representing main game loop)
        c.update()
    ```
    # Demo
    ```
    import pygame
    import csgame.colour

    pygame.init()

    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    c = csgame.colour.BiColourSmooth(
        csgame.colour.Colour(255, 0, 0, 255), # red
        csgame.colour.Colour(0, 0, 255, 255), # blue
        2 # 2 second transition
    )

    # -- at some point in the program --
    c.cycle()

    # -- in main game loop --
    while 1: # (representing main game loop)
        pygame.event.get()
        clock.tick(60)
        window.fill(c)
        
        if clock.get_fps() == 0: continue

        c.update(1 / clock.get_fps())

        if pygame.time.get_ticks() % 4000 < 10:
            c.cycle()

        pygame.display.update()
    ```
    """
    def __init__(self, start_colour: Colour, other_colour: Colour,
                 switch_time: float):
        super().__init__(start_colour, other_colour)

        self.switch_time: float = switch_time
        self.switch_timer: float = -1 # -1 => off
        self.switch_direction: int = 0
    
    def cycle(self) -> None:
        """start transition between the two colours"""
        self.switch_timer = 0
        if self == self.start_colour:
            self.switch_direction = 0
        else:
            self.switch_direction = 1
            

    def _lerp(self, a: int, b: int, t: float) -> int:
        return int((1 - t) * a + t * b)
    
    def _interpolate_colours(self):
        # direction = 0 => start to other
        # direction = 1 => other to start
        t = self.switch_timer / self.switch_time
        if self.switch_direction == 1:
            t = 1 - t

        self.set_colour(pygame.Color(
            self._lerp(self.start_colour.r, self.other_colour.r, t),
            self._lerp(self.start_colour.g, self.other_colour.g, t),
            self._lerp(self.start_colour.b, self.other_colour.b, t),
            255
        ))
    
    def update(self, dt: float) -> None:
        if self.switch_timer != -1 and self.switch_timer < self.switch_time:
            self.switch_timer += dt
            self.switch_timer = min(self.switch_timer, self.switch_time)

            self._interpolate_colours()

class FlashColour(BiColourSmooth):
    """
    colour that when called will flash to another colour
    before returning to the base colour

    # Example

    ```
    import pygame
    import csgame

    c = csgame.colour.FlashColour(
        csgame.colour.Colour(255, 0, 0, 255),     # red
        csgame.colour.Colour(255, 255, 255, 255), # white
        0.5 # 0.5 second flash
    )

    # -- at some point in the program --
    c.flash()

    # -- in main game loop --
    while 1: # (representing main game loop)
        c.update()
    ```
    # Demo
    ```
    import pygame
    import csgame.colour

    pygame.init()

    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    c = csgame.colour.FlashColour(
        csgame.colour.Colour(255, 0, 0, 255),     # red
        csgame.colour.Colour(255, 255, 255, 255), # white
        0.5 # 0.5 second flash
    )

    # -- at some point in the program --
    c.flash()

    # -- in main game loop --
    while 1: # (representing main game loop)
        pygame.event.get()
        clock.tick(60)
        window.fill(c)
        
        if clock.get_fps() == 0: continue

        c.update(1 / clock.get_fps())

        if pygame.time.get_ticks() % 2000 < 10:
            c.flash()

        pygame.display.update()
    ```
    """
    def __init__(self, base_colour: pygame.Color, flash_colour: pygame.Color,
                 flash_time: float):
        super().__init__(base_colour, flash_colour, flash_time/2)
    
    # flash doesn't actually have any special implementation
    # it is just given a different name to be more intuitive to use
    def flash(self) -> None: 
        """start the flash"""
        super().cycle()
    
    def update(self, dt: float) -> None:
        if self.switch_timer != -1 and self.switch_timer < self.switch_time:
            self.switch_timer += dt
            self.switch_timer = min(self.switch_timer, self.switch_time)

            self._interpolate_colours()
        
        if self.switch_timer == self.switch_time and self.switch_direction == 0:
            super().cycle()