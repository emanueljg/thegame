from importlib import import_module


def is_inside(rect, pos):
    """Helper function for checking of pos is inside of rect."""
    x, y = rect.pos
    w, h = rect.width, rect.height
    px, py = pos
    xmin, ymin = x - w/2, y - h/2
    xmax, ymax = x + w/2, y + h/2
    return xmin < px < xmax and ymin < py < ymax


def start_room(name):
    import_module(f'room.{name}')

