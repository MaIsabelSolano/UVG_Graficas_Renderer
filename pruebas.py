from gl import *
from vector import *
from obj import *

r = Render(1440,1440,'hatsune.bmp')

# Para probar se puede utilizar cualquier VP
#r.glViewPort(800, 800, 50, 100)
#r.glViewPort(100, 100)
#r.glViewPort(1400, 200)
r.glViewPort(1440, 1440)
r.glClearColor(BLACK)
r.glClear()

#"""
Hatsune = Obj('miku_lp.obj')
scale_factor = (800, 800, 800)
trans = (720, 100, 0)
#"""
"""
Hatsune = Obj('miku.obj')
scale_factor = (50, 50, 50)
trans = (720, 100, 0)
#"""

r.load_model_color(Hatsune, scale_factor, trans)

