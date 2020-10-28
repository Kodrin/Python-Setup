import pyglet
from pyglet import image
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse

# window parameters
WIN_WIDTH = 1200
WIN_HEIGHT = 780


IMAGE_PATH = "media/images/2.JPG"

window = pyglet.window.Window(width= WIN_WIDTH, height=WIN_HEIGHT)
# window.width = 1200
# window.height = 800

image = pyglet.resource.image(IMAGE_PATH)
label = pyglet.text.Label('[Logger]',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')


@window.event
def on_draw():
    window.clear()
    # image.blit(0, 0)
    label.draw()
    circle = shapes.Circle(x=100, y=150, radius=100, color=(50, 225, 30))


pyglet.app.run()