from pyautogui import size
from wasabi2d import Scene

from enums import Pos
from faces import Pane, Button
from infos import TextInfo, ClickInfo

# Strings

inv_body_s = """
"""

# Scene stuff

screen_width, screen_height = size()
scene = Scene(width=round(screen_width * 0.9), height=round(screen_height * 0.9))
w, h = scene.width, screen_height
scene.background = (0.5, 0.5, 0.5, 1)

# TextInfos
inv_title = TextInfo(text='Inventory', fontsize=50, align='center', y_offset=320)
inv_body = TextInfo(text=inv_body_s, fontsize=20, align='left', x_offset=130, y_offset=280)
test_body = TextInfo(text='Sure!', fontsize=20, align='center', y_offset=-10)
reader_style = TextInfo(fontsize=20, align='left', x_offset=450, y_offset=280)
writer_style = TextInfo(fontsize=22, align='left', x_offset=470, y_offset=-9)


# Panes
inv = Pane(scene, layer=1, corner_scale=0.12, pos=Pos.UPPER_LEFT, dims=(300, 800), text_infos=(inv_title, inv_body))
reader = Pane(scene, layer=1, corner_scale=0.21, pos=(w/2 + 100, 650/2), dims=(w - inv.dims[0] * 2 + 100, 650), text_infos=[reader_style])
writer = Pane(scene, layer=1, corner_scale=0.05, pos=(w/2 + 100, 750), dims=(w - inv.dims[0] * 2 + 100, 100), text_infos=[writer_style])


#test = Pane(scene, layer=1, corner_scale=0.035, pos=Pos.CENTER, dims=(100, 50), text_infos=[test_body])



