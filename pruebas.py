from gl import *
from vector import *
from obj import *
from textures import *
from matrices import *
from math import *

r = Render(2000, 2000,'Paimon.bmp')
# r = Render(500, 500, 'Cajita.bmp')

r.glViewPort(2000, 2000)
r.glClearColor(BLACK)
r.glClear()

# Fondo
fondo = Texture('fondo_m.bmp')
r.framebuffer = fondo.pixels

# Objetos

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

# t1 = Texture('caja_text.bmp')
# texturas = [t1, t1, t1, t1, t1, t1, t1]

scale_factor = (40, 40, 40)
trans = (1000, 400, 50)
rotation = (0, 0, 0)
r.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))

def shader(**kwargs):
    y = kwargs['y']
    x = kwargs['x']
    w, u, v = kwargs['bar']
    A, B, C = kwargs['coords']
    nA, nB, nC = kwargs['ncoords']
    texture = kwargs['textures']
    
    Light = V3(0, 10, 5).normalize()
    
    iA = nA.normalize() @ Light
    iB = nB.normalize() @ Light
    iC = nC.normalize() @ Light

    intensity = iA * w + iB * u + iC * v

    if intensity < 0:
        intensity = abs(intensity)

    if texture:
        
        vt1, vt2, vt3 = kwargs['tcoords']

        tx = vt1.x * w + vt2.x * u + vt3.x * v
        ty = vt1.y * w + vt2.y * u + vt3.y * v

        return texture.get_color_with_intensity(tx, ty)

    # if (y < 100):
    #     return color(255, 0, 0)
    # elif (y < 150):
    #     return color(255, 0, 0)
    # elif ( y < 100):
    #     return color(0, 0, 0)
    # else:
    #     return color(0, 0, 200)

r.active_shader = shader

r.load_model_color(Paimon, scale_factor, trans, rotation, texturas)

