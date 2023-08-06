# csgame
useful tools for pygame development

## instructions
1. Install:
```
pip install csgame
```
2. Initialise in project:
``` python
from csgame import *
```

## features
### csgame.colour
dynamic colours with special features
> BiColour - colour that can swap between 2 colours

> BiColourSmooth - BiColour that has a smooth transition when swapping

> FlashColour - colour that can momentarily flash to another colour

### csgame.menu
useful tools for menus
> Button - interactible button which can be pressed to perform an action

> Menu - holds a collection of buttons and is responsible for updating them

### csgame.player
provides basic player movement
> TopDownPlayer - simple top-down style player movement

> SideScrollPlayer - simple side scroll player movement with gravity

### csgame.camera
manipulates how sprites are drawn as if a camera is looking at them
> CameraSpriteGroup - sprite group which has a camera tracking a target