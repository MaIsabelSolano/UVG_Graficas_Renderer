from gl import *
from vector import *
from obj import *
from textures import *

r = Render(2000, 2000,'Paimon.bmp')

# r.glViewPort(1440, 1440)
# r.glClearColor(BLACK)
# r.glClear()

Paimon = Obj('Paimon.obj')

# Texturas a utilizar
t1 = Texture('Paimon_1.bmp')
t2 = Texture('Paimon_6.bmp')
t3 = Texture('Paimon_6.bmp')
t4 = Texture('Paimon_2.bmp')
t5 = Texture('Paimon_3.bmp')
t6 = Texture('Paimon_4.bmp')
t7 = Texture('Paimon_5.bmp')

texturas = [t1, t2, t3, t4, t5, t6]

scale_factor = (180, 180, 180)
trans = (1000, 10, 00)

r.load_model_color(Paimon, scale_factor, trans, t1)


