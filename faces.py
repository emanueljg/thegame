from math import pi
from collections.abc import Iterable

from enums import Pos


class Pane:
    DEFAULT_CORNER_SIZE = 570

    def __init__(self,
                 scene,
                 layer,
                 corner_scale,
                 pos,
                 dims,
                 bg_color=(1, 1, 1, 1),
                 corner_color=(1, 1, 1, 1),
                 text_infos=None,
                 corner_image='frame4',
                 ):
        self.scene = scene
        self.layer = layer
        self.corner_scale = corner_scale
        self.pos = self._resolve_pos(scene, dims, pos)
        self.dims = dims
        self.bg_color = bg_color
        self.corner_color = corner_color
        self.text_infos = text_infos or []
        self.corner_image = corner_image

        for ti in self.text_infos:
            ti.ref_pos = self.pos

        self.primitives = None
        self.rect, self.corners, self.labels = None, None, None

    @staticmethod
    def _resolve_pos(scene, dims, pos):
        w, h = dims

        #newpos = []
        #if type(pos) is tuple:
        #    for n in range(2):
        #        dim = dims[n]
        #        pos_axis = pos[n]
        #        if isinstance(pos_axis, Pane):
        #            pos_axis.dims[n] + po
        if pos == Pos.CENTER:
            return scene.width/2, scene.height/2
        elif pos == Pos.UPPER_LEFT:
            return w/2, h/2
        elif pos == Pos.UPPER_RIGHT:
            return scene.width - w/2, h/2
        elif pos == Pos.LOWER_RIGHT:
            return scene.width - w/2, scene.height - h/2
        elif pos == Pos.LOWER_LEFT:
            return w/2, scene.height - h/2
        else:
            return pos

    def _rect_maker(self):
        w, h = self.dims
        return self.scene.layers[self.layer].add_rect(width=w, height=h, pos=self.pos, color=self.bg_color)

    def _corner_maker(self):
        w, h = self.dims
        x, y = self.pos
        side = self.DEFAULT_CORNER_SIZE * self.corner_scale

        if side > max(self.dims):
            raise AttributeError("Corner side can't be larger than rect size.")

        moves = (((-w + side), (-h - 1 + side)),
                 ((w - side), (-h - 1 + side)),
                 ((w - side), (h + 1 - side)),
                 ((-w + side), (h + 1 - side)))

        corners = []
        for c, move in enumerate(moves):
            movex, movey = move
            final_pos = (x + movex / 2, y + movey / 2)  # 1/2 factored out from move tuple
            corners.append(self.scene.layers[self.layer + 1].add_sprite(
                image=self.corner_image,
                pos=final_pos,
                angle=(c * pi / 2),
                color=self.corner_color,
                scale=self.corner_scale
            ))

        return corners

    def _label_maker(self):
        return [self.scene.layers[self.layer + 1].add_label(**text_info.labelize()) for text_info in self.text_infos]

    def activate(self):
        r = self._rect_maker()
        c = self._corner_maker()
        l = self._label_maker()

        self.primitives = [r, c, l]
        self.rect, self.corners, self.labels = r, c, l

        return self

    def delete(self):
        for i in self.primitives:
            if isinstance(i, Iterable):
                for k in i:
                    k.delete()
            else:
                i.delete()


class Button(Pane):
    def __init__(self, click_info, outline_color=(0, 0, 0, 1), *args, **kwargs):
        super().__init__(corner_scale=0, corner_color=None, corner_image='', *args, **kwargs, )
        self.click_info = click_info
        self.outline_color = outline_color
        self.outline = None
        self.click = None

    def _outline_maker(self):
        w, h = self.dims
        return self.scene.layers[self.layer + 1].add_rect(width=w, height=h, pos=self.pos, color=self.outline_color, fill=False)

    def _click_maker(self):
        self.click_info.rect = self.outline
        self.click_info.register()
        return self.click_info

    def activate(self):
        self.rect = self._rect_maker()
        self.labels = self._label_maker()
        self.outline = self._outline_maker()
        self.click = self._click_maker()

        self.primitives = [self.rect, self.labels, self.outline]

        return self
