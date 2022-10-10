from gl import *
from vector import *
from obj import *
from textures import *
from matrices import *
from math import *

r = Render(2000, 2000,'Scene.bmp')

r.glViewPort(2000, 2000)
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

# Cámara _______________________________________
r.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))

# Objetos _______________________________________
# Traveler
print('Aether')
Aether = Obj('Models/Kaeya.obj')

# Texturas
t1 = Texture('Models/Kaeya_1.bmp') # Pelo
t2 = Texture('Models/Kaeya_2.bmp') # Ropa
t3 = Texture('Models/Kaeya_3.bmp') # Cara
t4 = Texture('Models/Kaeya_4.bmp') # Otros

"""
Orden
1.  ??
2.  t2 Piel
3.  t3 Pestañas
4.  t3 Cara
5.  t1 Pelo
resto: t2 Ropa
"""
texturas = [t1, t2, t3, t3, t1,
            t2, t2, t2, t2, t2,
            t2, t2, t2, t2, t2,
            t2
]

scale_factor = (50, 50, 50)
trans = (500, 100, 50)
rotation = (0, pi, 0)

r.load_model_color(Aether, scale_factor, trans, rotation, texturas)

scale_factor = (50, 50, 50)
trans = (1500, 100, 50)
rotation = (0, 0, 0)

r.load_model_color(Aether, scale_factor, trans, rotation, texturas)
