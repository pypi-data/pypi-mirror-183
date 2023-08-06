OpenGame is a Python3 module that can help you build a game faster.  
Document is writing, this is the dev version. 

Version: 0.2.1beta

# Theory
OpenGame built on pygame2. Many features of pygame are retained.   
Therefore, it has good compatibility with pygame.

# Why do you use OpenGame?
Let's see an example, we'll show a label "Hello World" on the screen. And let it follow the mouse.

If we use `opengame`, we should:
```python
import opengame as og
win = og.Window('Demo', (800, 600))
text = og.Label('Hello World')
text.pack()
@win.when_draw
def draw():
    text.pos = win.mouse.pos
win.show()
```

If we use `pygame`, we should:
```python
import sys
import pygame as pg
pg.init()
pg.font.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Demo')
font = pg.font.Font(None, 26)
while True:
    screen.fill((255, 255, 255))
    text = font.render('Hello World', True, (0, 0, 0))
    screen.blit(text, 400 - text.get_rect().width // 2, 300 - text.get_rect().height // 2)
    for event in pg.event.get():
        if event == pg.QUIT:
            pg.quit()
            sys.exit()
```

Really easy?

Although using `pyglet` and `opengame` is similar, yet `opengame` has other reason why you use it.  
> Note: In large projects, you should still use other packages because OpenGame designed for small projects.

## The Advantages
1. Simple API, callback system;
2. A perfect resource library;
3. Great encapsulation, more functions;
4. Lots of humanity design.

## The Inferiority
1. Instability(Only passed the test on Windows 10);
2. Not applicable to large projects.

# Install
Use `pip` install it:
```shell
pip install -U opengame
```
