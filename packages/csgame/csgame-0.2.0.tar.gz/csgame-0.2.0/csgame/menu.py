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
    from csgame import *

    pygame.init()

    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    bg_colour = csgame.colour.BiColour(
        csgame.colour.Colour(50, 50, 50, 255),  # gray
        csgame.colour.Colour(0, 255, 0, 255)    # green
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
            csgame.colour.Colour(255, 0, 0),
            csgame.colour.Colour(0, 0, 255),
            0.5
        ),          # background colour switches between red and blue on hover
        csgame.colour.Colour(0, 0, 0),   # black border colour
        csgame.colour.Colour(0, 0, 0),   # black text colour
        bg_colour.cycle # when pressed, cycle the background colour
    )


    # -- in main game loop --
    while 1: # (representing main game loop)
        pygame.event.get()
        clock.tick(60)
        window.fill(bg_colour)

        btn.draw(window)

        pygame.display.update()

        if clock.get_fps() == 0: continue
        btn.update(1 / clock.get_fps())
    ```
    # Demo 2
    ```
    import pygame
    from csgame import *

    pygame.init()

    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    bg_colour = csgame.colour.BiColour(
        csgame.colour.Colour(50, 50, 50, 255),  # gray
        csgame.colour.Colour(0, 255, 0, 255)    # green
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
            csgame.colour.Colour(0, 0, 255),
            csgame.colour.Colour(255, 255, 255),
            0.3
        ),          # background colour flashes to white (from blue)
        csgame.colour.Colour(0, 0, 0),   # black border colour
        csgame.colour.Colour(0, 0, 0),   # black text colour
        bg_colour.cycle # when pressed, cycle the background colour
    )


    # -- in main game loop --
    while 1: # (representing main game loop)
        pygame.event.get()
        clock.tick(60)
        window.fill(bg_colour)

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
        self.text = pygame.font.Font(None, text_size).render(text, True, self.text_colour) 
        self.text_rect = self.text.get_rect(center = center_pos) # gets the text's rect to easily move the text

        # holds whether the mouse button has already been pressed (to ignore holding the mouse down)
        self.clicked = True 

        self.action = action # function to be called when the button's pressed
    
    def draw(self, surface: pygame.Surface) -> None:
        """draws the button onto the specified surface"""
        pygame.draw.rect(surface, self.colour, self.rect) # draw main background colour
        pygame.draw.rect(surface, self.border_colour, 
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
                if self.colour == self.colour.other_colour: 
                    self.colour.cycle()

            if self.size.x > self.unhover_size.x:   # shrink button back down to unhover size if it's not already
                self.size -= ((self.hover_size-self.unhover_size) / self.grow_time) * dt
                self.rect = pygame.Rect((0,0), self.size) # makes new rect with adjusted size
                self.rect.center = self.text_rect.center  # places rect in correct place
            
            self.clicked = pygame.mouse.get_pressed()[0]
            return # next code is only for hovering
        
        if isinstance(self.colour, csgame.colour.BiColour) and not isinstance(self.colour, csgame.colour.FlashColour):
            if self.colour == self.colour.start_colour:
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
    from csgame import *

    pygame.init()

    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    bg_colour = csgame.colour.BiColour(
        csgame.colour.Colour(50, 50, 50, 255),  # gray
        csgame.colour.Colour(0, 255, 0, 255)    # green
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
                csgame.colour.Colour(255, 0, 0),
                csgame.colour.Colour(0, 0, 255),
                0.5
            ),          # background colour switches between red and blue on hover
            csgame.colour.Colour(0, 0, 0),   # black border colour
            csgame.colour.Colour(0, 0, 0),   # black text colour
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
            csgame.colour.Colour(0, 0, 255),
            csgame.colour.Colour(255, 255, 255),
            0.3
        ),          # background colour flashes to white (from blue)
        csgame.colour.Colour(0, 0, 0),   # black border colour
        csgame.colour.Colour(0, 0, 0),   # black text colour
        bg_colour.cycle # when pressed, cycle the background colour
    )
    menu = csgame.menu.Menu([btn_smooth, btn_flash])

    # -- in main game loop --
    while 1: # (representing main game loop)
        pygame.event.get()
        clock.tick(60)
        window.fill(bg_colour)

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

class TextBox:
    """
    input text box to enter text
    access the content inputted with the attribute `input_content`


    `*IMPORTANT*` use `pygame.event.get(exclude=pygame.KEYDOWN)` 
    
    when getting pygame eventsin other places of the code

    # Demo
    ```
    import pygame
    from csgame import *

    pygame.init()

    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    input_box = csgame.menu.TextBox(
        "username:",
        (window.get_width()/2, window.get_height()/2),
        600, 120, 50, 30, 10, 5, 10,
        csgame.colour.Colour(0, 0, 0),
        csgame.colour.Colour(0, 0, 0),
        csgame.colour.Colour(255, 255, 255),
        csgame.colour.Colour(168, 52, 235),
        csgame.colour.Colour(0, 255, 0),
        allow_spaces=True,
        hide_input=False
    )

    # -- in main game loop --
    while 1: # (representing main game loop)
        pygame.event.get(exclude=pygame.KEYDOWN) # VERY IMPORTANT
        clock.tick(60)
        window.fill("pink")

        input_box.update()

        pygame.display.update()
    ```
    """
    def __init__(self, prompt: str, center_pos: tuple[float, float], width: float, height: float, 
                 input_font_size: int, prompt_font_size: int, promt_y_offset: float,
                 input_x_offset: float, border_width: float,
                 input_colour: csgame.colour.Colour, prompt_colour: csgame.colour.Colour,
                 box_colour: csgame.colour.Colour, 
                 unfocused_border_colour: csgame.colour.Colour, focused_border_colour: csgame.colour.Colour,
                 allow_spaces: bool = True, hide_input: bool = False):
        self.screen = pygame.display.get_surface() # main screen for easy access

        self.rect = pygame.Rect(0,0,width,height) # main input bar
        self.rect.center = center_pos

        self.input_x_offset = input_x_offset
        self.border_width = border_width

        font = pygame.font.Font(None, prompt_font_size)
        self.prompt_text = font.render(prompt, True, prompt_colour)          # text image
        self.prompt_rect = self.prompt_text.get_rect(bottomleft=self.rect.topleft) # text container
        self.prompt_rect.y -= promt_y_offset

        self.input_colour = input_colour
        self.box_colour = box_colour
        self.unfocused_border_colour = unfocused_border_colour
        self.focused_border_colour = focused_border_colour

        self.active = False # if the user is currently inputting to this box

        self.allow_spaces: bool = allow_spaces
        self.hide_input: bool = hide_input

        self.input_font = pygame.font.Font(None, 50)
        self.input_content = ""  # player input string
    
    def update(self) -> None:
        """draws and updates text box"""
        if not self.active: # change border colour if text box is active or not
            pygame.draw.rect(self.screen, self.unfocused_border_colour, self.rect.inflate(self.border_width,
                                                                                          self.border_width))
        else:
            pygame.draw.rect(self.screen, self.focused_border_colour, self.rect.inflate(self.border_width,
                                                                                        self.border_width))
        pygame.draw.rect(self.screen, self.box_colour, self.rect)    # draw main input box
        self.screen.blit(self.prompt_text, self.prompt_rect) # draw box title

        # draw player input
        if not self.hide_input:
            input_text = self.input_font.render(self.input_content, True, self.input_colour)
        else:
            input_text = self.input_font.render("*"*len(self.input_content), True, self.input_colour)
        input_rect = input_text.get_rect(midleft=self.rect.midleft)
        input_rect.x += self.input_x_offset
        self.screen.blit(input_text, input_rect)

        self._user_input()
    
    def _user_input(self) -> None:
        """user interaction with the text box"""
        if pygame.mouse.get_pressed()[0]: # change activity of box
            self.active = self.rect.collidepoint(pygame.mouse.get_pos())
        if not self.active: 
            return
        
        if not pygame.key.get_focused(): # no keys pressed
            return

        for event in pygame.event.get(eventtype=pygame.KEYDOWN):
            if event.key == pygame.K_BACKSPACE:
                self.input_content = self.input_content[0:len(self.input_content)-1]
                continue
            elif event.key == pygame.K_SPACE and not self.allow_spaces:
                continue # ignore space bar
            
            self.input_content += event.unicode