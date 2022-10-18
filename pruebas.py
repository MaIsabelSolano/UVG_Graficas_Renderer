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
def Pastel_Shader(**kwargs):
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


r.active_shader = Pastel_Shader

# Fondo_______________________________________
fondo = Texture('Models/fondo2_m.bmp')
r.framebuffer = fondo.pixels

# Cámara _______________________________________
r.lookAt(V3(0, 1, 5), V3(0, 0.3, 0), V3(0, 1, 0))

# Objetos _______________________________________
# Paimon ..................................
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

scale_factor = (40, 40, 40)
trans = (1800, 600, -100)
rotation = (0, -pi/4, 0)

r.load_model_color(Paimon, scale_factor, trans, rotation, texturas)

# Traveler ..................................
print('Aether')
Aether = Obj('Models/Aether.obj')

# Texturas
t1 = Texture('Models/Aether_1.bmp') # Ropa
t2 = Texture('Models/Aether_2.bmp') # Otros
t3 = Texture('Models/Aether_3.bmp') # Cara
t4 = Texture('Models/Aether_4.bmp') # Pelo

"""
Orden
1.  t3 Cara
2.  ??
3.  ??
4.  t4 Ojos
5.  ??
6.  t3 Cejas
7.  ??
8.  ??
9.  t3 Ojos (blanco)
10. t4 Pelo
11. t1 Gancho de melo
12. t1 Bufanda
13. t1 Ropa
14. t1 Capa
15. t1 Guante der
16. t1 Arete
17. t1 Piel
18. t1 Guante iz
19. ??
20. ??
21. ??
22. ??
23. ??
24. 

"""
texturas = [t3, t2, t2, t4, t2, 
            t3, t2, t2, t3, t4,
            t1, t1, t1, t1, t1,
            t1, t1, t1, t1, t1,
            t1, t1, t1, t1,
]

scale_factor = (45, 45, 45)
trans = (1500, 100, 0)
rotation = (0, pi/8, 0)

r.load_model_color(Aether, scale_factor, trans, rotation, texturas)

# Jean ..................................
print('Jean')
Jean = Obj('Models/Jean.obj')

# Texturas
t1 = Texture('Models/Jean_1.bmp') # Cara
t2 = Texture('Models/Jean_2.bmp') # Ropa
t3 = Texture('Models/Jean_3.bmp') # Pelo
t4 = Texture('Models/Jean_4.bmp') # Otros

"""
Orden
1.  t1 Pestañas
2.  t1 Cara
3.  t2 Piel
4.  t3 Ojos
5.  t3 Pelo
resto: ropa
"""
texturas = [t1, t1, t2, t3, t3,
            t2, t2, t2, t2, t2,
            t2, t2, t2, t2, t2
]

# scale_factor = (50, 50, 50)
scale_factor = (40, 40, 40)
trans = (1000, 130, -500)
rotation = (0, 8*pi/7, 0)

r.load_model_color(Jean, scale_factor, trans, rotation, texturas)

# Kaeya ..................................
print('Kaeya')
Kaeya = Obj('Models/Kaeya.obj')

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

# scale_factor = (55, 55, 55)
scale_factor = (45, 45, 45)
trans = (600, 100, -500)
rotation = (0, 7*pi/6, 0)

r.load_model_color(Kaeya, scale_factor, trans, rotation, texturas)

# Amber ..................................
print('Amber')
Amber = Obj('Models/Amber.obj')

# Texturas
t1 = Texture('Models/Amber_1.bmp') # Cara
t2 = Texture('Models/Amber_2.bmp') # Pelo
t3 = Texture('Models/Amber_3.bmp') # Ropa
t4 = Texture('Models/Amber_4.bmp') # Otros

"""
Orden
1.  t1 Pestañas
2.  t1 Cara
3.  t2 Ojos
4.  t3 Ojos
5.  t3 Ropa
6.  t2 Pelo
resto: ropa
"""
texturas = [t1, t1, t2, t3, t3, t2, t3, t3]

scale_factor = (48, 48, 48)
trans = (300, 100, 100)
rotation = (0, 11*pi/8, 0)

r.load_model_color(Amber, scale_factor, trans, rotation, texturas)
