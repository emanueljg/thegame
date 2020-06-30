from props import scene, reader, writer
from wasabi2d import keys
from pygame import key
from infos import ClickInfo
from faces import Button

w, h = writer.dims
x, y = writer.pos

key.set_repeat(400, 20)  # Thank god for this!
MAXCHARS = 79  # Can't type longer cmds in the writer than this


activated = False
stored = ''


def on():
    global activated
    activated = True
    writer.labels[0].color = (0, 0, 0, 1)
    writer_button.outline.color = (0, 0, 0, 1)


def off():
    global activated
    activated = False
    writer.labels[0].color = (0, 0, 0, 0.5)
    writer_button.outline.color = (0, 0, 0, 0.5)


def toggle():
    if activated:
        off()
    else:
        on()


writer_button = Button(click_info=ClickInfo(on), scene=scene, layer=2, dims=(w - 50, h - 50), pos=(x, y), outline_color=(0, 0, 0, 0.5)).activate()


def write(key, unicode):
    global activated
    global stored

    if key == keys.RETURN:
        toggle()
    if not activated and key == keys.RETURN and stored != '':
        reader.labels[0].text += f'\n{stored}'
        writer.labels[0].text = ''
        stored = ''
    elif activated and key == keys.BACKSPACE:
        stored = stored[:-1]
        writer.labels[0].text = writer.labels[0].text[:-1]
    elif activated and len(stored) < MAXCHARS:
        stored += unicode
        writer.labels[0].text += unicode
