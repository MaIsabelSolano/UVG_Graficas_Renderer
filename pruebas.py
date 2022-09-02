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
#"""
t1 = Texture('Paimon_1.bmp') # cara
t2 = Texture('Paimon_2.bmp') # Pelo
t3 = Texture('Paimon_3.bmp') # Ropa
t4 = Texture('Paimon_4.bmp') # Capa
t5 = Texture('Paimon_5.bmp') # Otros

"""
orden
1. Ojos y Pestañas (blanco) t1
2. Ojos (pupilas) t2
3. Cara t1
4. Piel t1
5. Ropa t3
6. Pelo t2
7. Capa t4
8. ??
""" 
texturas = [t1, t2, t1, t1, t3, t2, t4, t1]

scale_factor = (180, 180, 180)
trans = (1000, 10, 00)

r.load_model_color(Paimon, scale_factor, trans, texturas)


