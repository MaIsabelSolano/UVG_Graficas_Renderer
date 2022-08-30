from gl import *
from vector import *
from obj import *

r = Render(1440,1440,'hatsune.bmp')

r.glViewPort(1440, 1440)
r.glClearColor(BLACK)
r.glClear()

"""
Hatsune = Obj('miku_lp.obj')
scale_factor = (800, 800, 800)
trans = (720, 100, 0)
#"""
#"""
Hatsune = Obj('miku.obj')
scale_factor = (50, 50, 50)
trans = (720, 100, 00)
#"""

r.load_model_color(Hatsune, scale_factor, trans)

