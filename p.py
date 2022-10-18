from gl import *
from vector import *
from obj import *
from textures import *
from matrices import *
from math import *

r = Render(1000, 1000,'p.bmp')

r.glViewPort(1000, 1000)
r.glClearColor(BLACK)
r.glClear()

# Shaders _______________________________________
def shader(**kwargs):
    y = kwargs['y']
    x = kwargs['x']
    w, u, v = kwargs['bar']
    A, B, C = kwargs['coords']
    nA, nB, nC = kwargs['ncoords']
    texture = kwargs['textures']

    Light = V3(0, 1, 1).normalize()
    Norm = (B - A) * (C - A)
    intensity = Norm.normalize() @ Light

    if intensity < 0:
        # Para evitar problemas con números negativos
        intensity = 0

    if texture:
        
        vt1, vt2, vt3 = kwargs['tcoords']

        tx = vt1.x * w + vt2.x * u + vt3.x * v
        ty = vt1.y * w + vt2.y * u + vt3.y * v

        return texture.get_color_pastel(tx, ty, intensity)

r.active_shader = shader

# Cámara _______________________________________
r.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))

# Objetos _______________________________________
# Amber
print('paimon')
Paimon = Obj('Models/Paimon.obj')

# Texturas a utilizar
t1 = Texture('Models/Paimon_1.bmp') # cara
t2 = Texture('Models/Paimon_2.bmp') # Pelo
t3 = Texture('Models/Paimon_3.bmp') # Ropa
t4 = Texture('Models/Paimon_4.bmp') # Capa
t5 = Texture('Models/Paimon_5.bmp') # Otros

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

scale_factor = (100, 100, 100)
trans = (500, 0, 0)
rotation = (0, 0, 0)

r.load_model_color(Paimon, scale_factor, trans, rotation, texturas)
