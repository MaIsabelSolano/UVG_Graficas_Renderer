from gl import *
from vector import *
from obj import *
from textures import *
from matrices import *
from math import *

r = Render(1000, 1000,'lab2.bmp')

r.glViewPort(1000, 1000)
r.glClearColor(BLACK)
r.glClear()

def shader(**kwargs):
    y = kwargs['y']
    x = kwargs['x']
    w, u, v = kwargs['bar']
    A, B, C = kwargs['coords']
    nA, nB, nC = kwargs['ncoords']
    texture = kwargs['textures']
    
    Light = V3(0, 0, 1).normalize()
    
    Norm = (B - A) * (C - A)
    intensity = Norm.normalize() @ Light

    if intensity < 0:
        intensity = abs(intensity)

    if (y < 0):
        return color(
            0, 
            0, 
            0)
    elif (100 <= y < 240):
        return color(
            round(227 * intensity),
            round(173 * intensity),
            round(113)
        )
    elif (240 <= y < 260):
        return color(
            round(215 * intensity),
            round(179 * intensity),
            round(136)
        )
    elif (260 <= y < 320):
        return color(
            round(204 * intensity),
            round(184 * intensity),
            round(159)
        )
    elif (320 <= y < 360):
        return color(
            round(220 * intensity),
            round(210 * intensity),
            round(200)
        )
    elif (355 <= y < 365):
        return color(
            round(217 * intensity),
            round(170 * intensity),
            round(190)
        )
    elif (360 <= y < 420):
        return color(
            round(215 * intensity),
            round(131 * intensity),
            round(108)
        )
    elif (420 <= y < 450):
        return color(
            round(220 * intensity),
            round(210 * intensity),
            round(200)
        )
    elif (450 <= y < 460):
        return color(
            round(227 * intensity),
            round(173 * intensity),
            round(113)
        )
    elif (460 <= y < 490):
        return color(
            round(220 * intensity),
            round(210 * intensity),
            round(200)
        )
    elif (490 <= y < 550):
        return color(
            round(227 * intensity),
            round(173 * intensity),
            round(113)
        )
    elif (550 <= y < 570):
        return color(
            round(219 * intensity),
            round(152 * intensity),
            round(130)
        )
    elif (570 <= y < 615):
        return color(
            round(251 * intensity),
            round(131 * intensity),
            round(107)
        )
    elif (615 <= y < 620):
        return color(
            round(231 * intensity),
            round(161 * intensity),
            round(144)
        )
    elif (620 <= y < 640):
        return color(
            round(211 * intensity),
            round(190 * intensity),
            round(180)
        )
    elif (640 <= y < 670):
        return color(
            round(171 * intensity), 
            round(145 * intensity), 
            round(122)
        )
    elif (670 <= y < 680):
        return color(
            round(191 * intensity),
            round(168 * intensity),
            round(151)
        )
    elif (680 <= y < 700):
        return color(
            round(211 * intensity),
            round(190 * intensity),
            round(180)
        )
    elif (700 <= y < 710):
        return color(
            round(191 * intensity),
            round(168 * intensity),
            round(151)
        )
    elif (710 <= y < 740):
        return color(
            round(171 * intensity), 
            round(145 * intensity), 
            round(122)
        )
    elif (740 <= y < 760):
        return color(
            round(150 * intensity), 
            round(128 * intensity),
            round(103)
        )
    elif (760 <= y < 800):
        return color(
            round(130 * intensity), 
            round(111 * intensity), 
            round(84)
        )
    else:
        return color(
            round(255 * intensity), 
            round(255 * intensity), 
            round(255)
        )


r.active_shader = shader

r.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))

sphere = Obj('Models/sphere.obj')

t = Texture('Models/white.bmp')

textures = [t]

scale_factor = (300, 300, 100)
trans = (500, 500, 0)
rotation = (0, 0, 0)

r.load_model_color(sphere, scale_factor, trans, rotation, textures)
