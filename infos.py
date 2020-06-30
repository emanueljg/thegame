from typing import Mapping, List, Tuple
from dataclasses import dataclass, asdict, field
from functools import partial
from typing import Callable, Any

clicks = []


@dataclass
class TextInfo:
    # Appearance
    text: str = ''  # label-attribute
    align: str = 'center'  # label-attribute
    fontsize: int = 20  # label-attribute
    font: str = None  # label-attribute
    color: tuple = (0, 0, 0, 1)  # label-attribute

    # Positioning/other
    ref_pos: tuple = (0, 0)
    x_offset: int = 0
    y_offset: int = 0
    pos: tuple = field(init=False)  # label-attribute

    @property
    def pos(self):
        x, y = self.ref_pos
        return x - self.x_offset, y - self.y_offset

    @pos.setter  # For some reason this is needed... God knows why.
    def pos(self, val):
        pass

    def labelize(self):
        return {k: v for k, v in asdict(self).items() if k in ('text', 'align', 'fontsize', 'font', 'color', 'pos')}


@dataclass(init=False)
class ClickInfo:
    callback: Callable
    args: Tuple[Any]
    kwargs: Mapping[Any, Any]

    rect: Any = None

    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs
        self.partial = partial(self.callback, *self.args, **self.kwargs)

    def register(self):
        clicks.append(self)











