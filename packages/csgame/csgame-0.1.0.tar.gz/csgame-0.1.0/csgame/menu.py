"""
tools that can be used for menus
"""

import pygame
import csgame.colour

class Button:
    """
    Interactible button for menus

    # Demo 1
    ```
    import pygame
    import csgame

    pygame.init()

    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    bg_colour = csgame.colour.BiColour(
        pygame.Color(50, 50, 50, 255),  # gray
        pygame.Color(0, 255, 0, 255)    # green
    )
    btn = csgame.menu.Button(
        "change background",
        (300, 300), # 300x300 pixel button
        1.25,       # grows to 1.25x the scale
        0.5,        # takes 0.5 seconds to grow
        5,          # 5 pixel border width
        30,         # 30 size text
        (window.get_width()/2, window.get_height()/2), # middle of screen
        csgame.colour.BiColourSmooth(
            pygame.Color(255, 0, 0),
            pygame.Color(0, 0, 255),
            0.5
        ),          # background colour switches between red and blue on hover
        csgame.colour.Colour(pygame.Color(0, 0, 0)),   # black border colour
        csgame.colour.Colour(pygame.Color(0, 0, 0)),   # black text colour
        bg_colour.cycle # when pressed, cycle the background colour
    )


    # -- in main game loop --
    while 1: # (representing main game loop)
        pygame.event.get()
        clock.tick(60)
        window.fill(bg_colour.colour)

        btn.draw(window)

        pygame.display.update()

        if clock.get_fps() == 0: continue
        btn.update(1 / clock.get_fps())
    ```
    # Demo 2
    ```
    import pygame
    import csgame

    pygame.init()

    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    bg_colour = csgame.colour.BiColour(
        pygame.Color(50, 50, 50, 255),  # gray
        pygame.Color(0, 255, 0, 255)    # green
    )
    btn = csgame.menu.Button(
        "change background",
        (300, 150), # 300x300 pixel button
        1.1,       # grows to 1.1x the scale
        0.2,        # takes 0.2 seconds to grow
        5,          # 5 pixel border width
        30,         # 30 size text
        (window.get_width()/2, window.get_height()/2), # middle of screen
        csgame.colour.FlashColour(
            pygame.Color(0, 0, 255),
            pygame.Color(255, 255, 255),
            0.3
        ),          # background colour flashes to white (from blue)
        csgame.colour.Colour(pygame.Color(0, 0, 0)),   # black border colour
        csgame.colour.Colour(pygame.Color(0, 0, 0)),   # black text colour
        bg_colour.cycle # when pressed, cycle the background colour
    )


    # -- in main game loop --
    while 1: # (representing main game loop)
        pygame.event.get()
        clock.tick(60)
        window.fill(bg_colour.colour)

        btn.draw(window)

        pygame.display.update()

        if clock.get_fps() == 0: continue
        btn.update(1 / clock.get_fps())
    ```
    
    """
    def __init__(self, text: str, size: tuple[float, float], grow_scale: float, grow_time: float,
                 border_width: float, text_size: int, center_pos: tuple[float, float], 
                 button_colour: csgame.colour.Colour, border_colour: csgame.colour.Colour, text_colour: csgame.colour.Colour, 
                 action):
        """size: (width, height)"""
        self.rect = pygame.Rect(0,0,size[0],size[1])    # main rect for the button
        self.rect.center = center_pos                   # aligns rect to specified centre

        self.size = pygame.math.Vector2(size[0],size[1])            # current size of the button
        self.unhover_size = self.size.copy()                        # size of the button when not hovering over it
        self.hover_size = self.unhover_size * grow_scale  # size of the button when hovering over it
        self.grow_time = grow_time

        self.border_width = border_width

        self.colour = button_colour        # colour of button background
        self.border_colour = border_colour # colour of the border around buttons
        self.text_colour = text_colour

        # image for the text on the button
        self.text = pygame.font.Font(None, text_size).render(text, True, self.text_colour.colour) 
        self.text_rect = self.text.get_rect(center = center_pos) # gets the text's rect to easily move the text

        # holds whether the mouse button has already been pressed (to ignore holding the mouse down)
        self.clicked = True 

        self.action = action # function to be called when the button's pressed
    
    def draw(self, surface: pygame.Surface) -> None:
        """draws the button onto the specified surface"""
        pygame.draw.rect(surface, self.colour.colour, self.rect) # draw main background colour
        pygame.draw.rect(surface, self.border_colour.colour, 
                         self.rect.inflate(self.border_width, self.border_width), 
                         width=self.border_width) # draw border
        surface.blit(self.text, self.text_rect) # draw text
    
    def update(self, dt: float) -> None:
        """called once per frame"""
        self._mouse_interact(dt)

        self.colour.update(dt)
    
    def _mouse_interact(self, dt: float) -> None:
        """mouse interaction with the button"""
        if not self.rect.collidepoint(pygame.mouse.get_pos()): # mouse outside button
            if isinstance(self.colour, csgame.colour.BiColour) and not isinstance(self.colour, csgame.colour.FlashColour):
                if self.colour.colour == self.colour.other_colour: 
                    self.colour.cycle()

            if self.size.x > self.unhover_size.x:   # shrink button back down to unhover size if it's not already
                self.size -= ((self.hover_size-self.unhover_size) / self.grow_time) * dt
                self.rect = pygame.Rect((0,0), self.size) # makes new rect with adjusted size
                self.rect.center = self.text_rect.center  # places rect in correct place
            
            self.clicked = pygame.mouse.get_pressed()[0]
            return # next code is only for hovering
        
        if isinstance(self.colour, csgame.colour.BiColour) and not isinstance(self.colour, csgame.colour.FlashColour):
            if self.colour.colour == self.colour.start_colour:
                self.colour.cycle()

        if self.size.x < self.hover_size.x: # grows button up to hover size if it's not already
            self.size += ((self.hover_size-self.unhover_size) / self.grow_time) * dt
            self.rect = pygame.Rect((0,0), self.size) # makes new rect with adjusted size
            self.rect.center = self.text_rect.center  # places rect in correct place
        
        if pygame.mouse.get_pressed()[0] and not self.clicked: # left mouse button clicked (and hovering over button)
            self.action() # do the button's action
            self.clicked = True

            if isinstance(self.colour, csgame.colour.FlashColour):
                self.colour.flash()

        elif not pygame.mouse.get_pressed()[0]:
            # reason for not pressing the button was that the mouse wasn't clicked
            self.clicked = False

class Menu:
    """
    base menu class

    # Demo
    ```
    import pygame
    import csgame

    pygame.init()

    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    bg_colour = csgame.colour.BiColour(
        pygame.Color(50, 50, 50, 255),  # gray
        pygame.Color(0, 255, 0, 255)    # green
    )
    btn_smooth = csgame.menu.Button(
            "change background",
            (300, 300), # 300x300 pixel button
            1.25,       # grows to 1.25x the scale
            0.5,        # takes 0.5 seconds to grow
            5,          # 5 pixel border width
            30,         # 30 size text
            (200, window.get_height()/2),
            csgame.colour.BiColourSmooth(
                pygame.Color(255, 0, 0),
                pygame.Color(0, 0, 255),
                0.5
            ),          # background colour switches between red and blue on hover
            csgame.colour.Colour(pygame.Color(0, 0, 0)),   # black border colour
            csgame.colour.Colour(pygame.Color(0, 0, 0)),   # black text colour
            bg_colour.cycle # when pressed, cycle the background colour
        )
    btn_flash = csgame.menu.Button(
        "change background",
        (300, 150), # 300x300 pixel button
        1.1,       # grows to 1.1x the scale
        0.2,        # takes 0.2 seconds to grow
        5,          # 5 pixel border width
        30,         # 30 size text
        (window.get_width()-200, window.get_height()/2),
        csgame.colour.FlashColour(
            pygame.Color(0, 0, 255),
            pygame.Color(255, 255, 255),
            0.3
        ),          # background colour flashes to white (from blue)
        csgame.colour.Colour(pygame.Color(0, 0, 0)),   # black border colour
        csgame.colour.Colour(pygame.Color(0, 0, 0)),   # black text colour
        bg_colour.cycle # when pressed, cycle the background colour
    )
    menu = csgame.menu.Menu([btn_smooth, btn_flash])

    # -- in main game loop --
    while 1: # (representing main game loop)
        pygame.event.get()
        clock.tick(60)
        window.fill(bg_colour.colour)

        try:
            menu.update(1 / clock.get_fps())
        except ZeroDivisionError:
            menu.update(1 / 99999)

        pygame.display.update()
    ```
    """
    def __init__(self, buttons: list[Button]):
        self.buttons = buttons

        self.screen = pygame.display.get_surface()
    
    def update(self, dt: float) -> None:
        """called once per frame to draw and update menu"""
        for button in self.buttons:
            button.update(dt)
            button.draw(self.screen)