from gl import *
from obj import *

r = Render(1440,1440,'hatsune.bmp')

r.glClearColor(BLACK)
r.glClear()

o = Obj('miku.obj')

scale_factor = (50, 50)
trans = (720, 100)

for face in o.faces:
    
    if (len(face) == 3):
        f1 = face[0][0] -1
        f2 = face[1][0] -1
        f3 = face[2][0] -1

        v1 = transform_vertex(o.vertices[f1], trans, scale_factor)
        v2 = transform_vertex(o.vertices[f2], trans, scale_factor)
        v3 = transform_vertex(o.vertices[f3], trans, scale_factor)

        # generar la línea
        r.line((v1[0], v1[1]), (v2[0], v2[1]))
        r.line((v2[0], v2[1]), (v3[0], v3[1]))
        r.line((v3[0], v3[1]), (v1[0], v1[1]))

    if (len(face) == 4):
        f1 = face[0][0] -1
        f2 = face[1][0] -1
        f3 = face[2][0] -1
        f4 = face[3][0] -1

        v1 = transform_vertex(o.vertices[f1], trans, scale_factor)
        v2 = transform_vertex(o.vertices[f2], trans, scale_factor)
        v3 = transform_vertex(o.vertices[f3], trans, scale_factor)
        v4 = transform_vertex(o.vertices[f4], trans, scale_factor)

        # generar la línea
        r.line((v1[0], v1[1]), (v2[0], v2[1]))
        r.line((v2[0], v2[1]), (v3[0], v3[1]))
        r.line((v3[0], v3[1]), (v4[0], v4[1]))
        r.line((v4[0], v4[1]), (v1[0], v1[1]))

r.glFinish()
