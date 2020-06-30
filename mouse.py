from pygame import mouse
from props import scene

mouse.set_visible(False)
mp = mouse.get_pos()

mouse_rect = scene.layers[10].add_rect(10, 10, color=(0, 0, 0, 1), pos=mp, fill=False)


def to_black():
    mouse_rect.color = 'black'


def to_green():
    mouse_rect.color = 'green'

