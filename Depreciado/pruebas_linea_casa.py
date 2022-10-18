from gl_line import *

r = Render(1440,1440,'SR2_line.bmp')

# Para probar se puede utilizar cualquier VP
#r.glViewPort(800, 800, 50, 100)
#r.glViewPort(100, 100)
#r.glViewPort(1400, 200)
r.glViewPort(1440, 1440)

# Casa simple escrita directamente en el archivo
r.glColor(RED)
r.line((10,10), (10,100))
r.line((10,10), (100,10))
r.line((100,10), (100,100))
r.line((10,100), (100,100))
r.line((10,100), (55,150))
r.line((55,150), (100,100))
r.line((100,100), (120,100))
r.line((100,10), (120,10))
r.line((120,10), (120,100))
r.line((55,150), (75,150))
r.line((75,150), (120,100))
r.line((20,10), (20, 70))
r.line((20,70), (50,70))
r.line((50,70), (50,10))
r.line((65,40), (85,40))
r.line((65,70), (85,70))
r.line((65,40), (65,70))
r.line((85,40), (85,70))

# Casa hecha en el ViewPort

# pared izquierda
r.line_vertex((-0.7,-0.3), (-0.7,0.1))
r.line_vertex((-0.3,-0.6), (-0.3,-0.2))
r.line_vertex((-0.7,-0.3), (-0.3,-0.6))
r.line_vertex((-0.7,0.10), (-0.3,-0.2))

# techo izquierdo
r.line_vertex((-0.7,0.1), (-0.3,0.6))
r.line_vertex((-0.3,-0.2), (0.1,0.3))
r.line_vertex((-0.3,0.6), (0.1,0.3))

# Parte de enfrente
r.line_vertex((-0.3,-0.6), (0.0,-0.45))
r.line_vertex((0.0,-0.45), (0.0,-0.2))
r.line_vertex((0.0,-0.2), (0.1, -0.14))
r.line_vertex((0.1,-0.4), (0.1,-0.14))
r.line_vertex((0.1,-0.4), (0.4,-0.25))
r.line_vertex((0.4,-0.25), (0.4,0.05))
r.line_vertex((0.4,0.05), (0.1,0.3))

r.glFinish() 

