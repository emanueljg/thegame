from wasabi2d import event
from helpers import is_inside
from mouse import mouse_rect, to_black, to_green
from infos import clicks
import writer


@event
def on_mouse_move(pos):
    mouse_rect.pos = pos
    for click in clicks:
        if is_inside(click.rect, pos):
            to_green()
            break
    else:
        to_black()


@event
def on_mouse_down(pos):
    for click in clicks:
        if is_inside(click.rect, pos):
            click.partial()

    if not is_inside(writer.writer_button.rect, pos):
        writer.off()


@event
def on_key_down(key, unicode):
    writer.write(key, unicode)
