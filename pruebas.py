from gl import *
from vector import *
from obj import *
from textures import *
from matrices import *
from math import *

r = Render(500, 500,'Paimon_da.bmp')
# r = Render(500, 500, 'Cajita.bmp')

r.glViewPort(500, 500)
r.glClearColor(BLACK)
r.glClear()

Paimon = Obj('Paimon.obj')

# Texturas a utilizar
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

"""
Transformaciones

Modo de uso: Descomentar cada grupo de código para poder 
obtener las transformaciones subidas a canvas

Tip: Utilizar comandos "ctr + k + c" y "ctr + k + u" para
comentar y descomentar respectivamente

"""
# # __________________________________________________________________
# # Transformación: High angle: front 
# # Nombre de archivo: Paimon_ha_f.bmp

# scale_factor = (50, 50, 50)
# trans = (250, 0, -50)
# rotation = (0, 0, 0)
# r.lookAt(V3(0, 15, 10), V3(0, 1, 0), V3(0, 1, 0))
# r.load_model_color(Paimon, scale_factor, trans, rotation, texturas)
# # __________________________________________________________________

# # __________________________________________________________________
# # Transformación: High angle: back ()
# # Nombre de archivo: Paimon_ha_b.bmp

# scale_factor = (50, 50, 50)
# trans = (250, 0, -50)
# rotation = (0, pi, 0)
# r.lookAt(V3(0, 15, 10), V3(0, 1, 0), V3(0, 1, 0))
# r.load_model_color(Paimon, scale_factor, trans, rotation, texturas)
# # __________________________________________________________________

# # __________________________________________________________________
# # Transformación: Low angle: front ()
# # Nombre de archivo: Paimon_la_b.bmp

# scale_factor = (50, 50, 50)
# trans = (250, 0, 0)
# rotation = (0, 0, 0)
# r.lookAt(V3(0, 0, 25), V3(0, -1, 0), V3(0, 1, 0))
# r.load_model_color(Paimon, scale_factor, trans, rotation, texturas)
# # __________________________________________________________________

# # __________________________________________________________________
# # Transformación: Low angle: back ()
# # Nombre de archivo: Paimon_la_b.bmp

# scale_factor = (50, 50, 50)
# trans = (250, 0, 0)
# rotation = (0, pi, 0)
# r.lookAt(V3(0, 0, 25), V3(0, -1, 0), V3(0, 1, 0))
# r.load_model_color(Paimon, scale_factor, trans, rotation, texturas)
# # __________________________________________________________________


# # __________________________________________________________________
# # Transformación: Medium shot ()
# # Nombre de archivo: Paimon_ms.bmp

# scale_factor = (90, 90, 90)
# trans = (250, -400, 0)
# rotation = (0, 0, 0)
# r.lookAt(V3(0, 0, 100), V3(0, 0, 0), V3(0, 1, 0))
# r.load_model_color(Paimon, scale_factor, trans, rotation, texturas)
# # __________________________________________________________________

# __________________________________________________________________
# Transformación: Dutch angle ()
# Nombre de archivo: Paimon_da.bmp

scale_factor = (60, 60, 60)
trans = (350, -350, 0)
rotation = (0, pi/6, 0)
r.lookAt(V3(0, -10, 100), V3(0, -0.25, 0), V3(1, 1, 0))
r.load_model_color(Paimon, scale_factor, trans, rotation, texturas)
# __________________________________________________________________
