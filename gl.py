import struct
from vector import *
from matrices import *
from obj import *
from math import *

""" Estructuras necesarias para crear un archivo BMP """

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w): 
    # 2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

""" Funciones necesarias """

# clase color, recibe en rgb y lo retorna en bytes en el orden requerido
def color(r, g, b):
    return bytes([b, g, r])

""" Colores pre-establecidos """

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
RED = color(250, 0, 0)
ORANGE = color( 200, 100, 0)
BLUE = color(0, 0, 255)
GREEN = color(0, 255, 0)



""" Clase Render: Produce la imagen BMP"""
class Render(object):
    def __init__(self, width, height, nombre = 'b.bmp'):
        # puede quedar vacío
        self.glInit(width, height, nombre)

    def glInit(self, w, h, nombre):
        self.fileName = nombre
        self.width = w
        self.height = h
        self.width_vp = w
        self.height_vp = h
        self.ModelM = None
        self.View = None

        self.current_color = WHITE
        self.clear_color = BLACK
        self.active_shader = None

        self.glClear()
        self.glFinish()

        # Viewport
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0


    """
    glClear: Vuelve todos los pixeles de un mismo color:
    """
    def glClear(self):
        self.framebuffer = [
            [self.clear_color for x in range(self.width)]
            for y in range(self.height)
        ]
        self.zBuffer = [
            [-9999999999 for x in range(self.width)]
            for y in range(self.height)
        ]
        

    """
    glClearColor: Determina el color con el que se realizará el Clear

    Parámetros:
    c:(int, int, int) Color con el que se pintará en formato rgb
    """
    def glClearColor(self, c):
        self.clear_color = c

    """
    glColor: Void
    
    Cambia el color actual que se está utilizando

    Parámetros: 
    c:(int, int, int) Color con el que se pintará en formato rgb
    """
    def glColor(self, c):
        self.current_color = c

    """
    glViewPort: 
    
    Genera una ventana en la que se podrá
    únicamente escribir allí

    Parámetros: 
    w:int Ancho de la ventana
    h:int Alto de la ventana
    x:int Traslasión en x, centrado si no se indica un valor
    y:int Traslasión en y, centrado si no se indica un valor
    
    """
    def glViewPort(self, w, h, x = 0, y = 0):
        # Redefinimos los valores
        self.width_vp = w
        self.height_vp = h

        # Buscamos el centro del vp
        w_vp_c = round(w/2)
        h_vp_c = round(h/2)

        # Buscamos el centro del bmp
        w_bmp_c = round(self.width/2)
        h_bmp_c = round(self.height/2)

        # Esquinas
        self.x_min = w_bmp_c - w_vp_c + round(x)
        self.x_max = w_bmp_c + w_vp_c + round(x)
        self.y_min = h_bmp_c - h_vp_c + round(y)
        self.y_max = h_bmp_c + h_vp_c + round(y)

        # Frame buffer terporal
        FB_temp = [
            [BLACK for x in range(self.width)]
            for y in range(self.height)
        ]

        # Llenar el FB_temp
        for x in range(len(FB_temp)):
            for y in range(len(FB_temp[x])):
                if (self.x_min <= x and x <= self.x_max) and (self.y_max >= y >= self.y_min):
                    FB_temp[y][x] = WHITE

        # Reemplazar FB
        self.framebuffer = FB_temp

    """
    glFinish:Void
        
    Escribe todo lo necesario para generar un archivo bmp y convierte cada
    uno de los colores del FrameBuffer a un pixel en el archivo

    Parámetros:
    filename:String Nombre del archivo a generar. 
    """
    def glFinish(self):
        f = open(self.fileName, 'bw')

        # pixel header

        f.write(char('B'))
        f.write(char('M'))
        # tamaño del archivo (14 bytes del info header + 40 + ancho*alto*3)
        f.write(dword(14 + 40 + self.width * self.height * 3))
        # 2 bytse (??)
        f.write(word(0))
        f.write(word(0))
        # donde inicia la bitmap data, offset de un puntero saltando todo el info header y 40 extras ()
        f.write(dword(14 + 40))

        # info header

        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        # colores:
        f.write(word(24))
        # compresión:
        f.write(dword(0))
        # tamaño de la imagen sin el header
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data (la imágen en sí)

        for x in range(self.height):
            for y in range(self.width): 
                f.write(self.framebuffer[x][y])

        f.close()

    """
    Point:Void
    
    Cambia un color del Framebuffer al color actual, solamente si este está dentro de los límites
    del archivo

    Parámetros:
    x:int Posición en x del punto
    y:int Posición en y del punto
    """
    def point(self, x, y):
        # pinta un color utilizando un puntero
        if (0 <= x < self.width and 0 <= y < self.height ):
            self.framebuffer[y][x] = self.current_color

    """
    Vertex:Void
    
    Genera un punto en la posición establecida en el ViewPort

    Parámetros:
    m:float[-1.0, 1.0] Posición en x del punto en el ViewPort
    y:float[-1.0, 1.0] Posición en y del punto en el ViewPort
    """
    def Vertex(self, m, n):
      posx = self.x_min + round((1/2)*self.width_vp + m*(1/2)*self.width_vp)
      posy = self.y_min + round((1/2)*self.height_vp + n*(0.5)*self.height_vp)

      # pinta un color utilizando un puntero
      self.framebuffer[posy][posx] = self.current_color

    """
    loadModelMatrix:Void

    Con los valores brindados, generera la matriz de transforamciones

    translante:(int, int, int) Modificación de posiciones en x, y , z
    scale:(int, int, int) Modificación de escala en x, y, z
    rotation:(rad, rad, rad) Modificiación de rotación en x, y, z

    """
    def loadModelMatrix(self, translante = (0, 0, 0), scale = (1, 1, 1), rotate = (0, 0, 0)):

        translante = V3(*translante)
        scale = V3(*scale)
        rotate = V3(*rotate)

        # Traslación
        translationMatrix = M4([
            [1, 0, 0, translante.x],
            [0, 1, 0, translante.y],
            [0, 0, 1, translante.z],
            [0, 0, 0, 1]
        ])

        # Escala
        scaleMatrix = M4([
            [scale.x, 0, 0, 0],
            [0, scale.y, 0, 0],
            [0, 0, scale.z, 0],
            [      0, 0, 0, 1]
        ])

        # rotación
        a = rotate.x
        rotation_x = M4([
            [1,      0,       0, 0],
            [0, cos(a), -sin(a), 0],
            [0, sin(a),  cos(a), 0],
            [0,      0,       0, 1]
        ])

        b = rotate.y
        rotation_y = M4([
            [ cos(b), 0, sin(b), 0],
            [      0, 1,      0, 0],
            [-sin(b), 0, cos(b), 0],
            [      0, 0,      0, 1]
        ])

        c = rotate.z
        rotation_z = M4([
            [cos(c), -sin(c), 0, 0],
            [sin(c),  cos(c), 0, 0],
            [     0,       0, 1, 0],
            [     0,       0, 0, 1]
        ])

        rotationMatrix = rotation_x * rotation_y * rotation_z

        # Generación de matriz de transformaciones
        self.ModelM = translationMatrix * rotationMatrix * scaleMatrix

    """
    transform_vertex: (float, float, float)

    Utilizando la matriz de transformación, aplica las transformaciones al vértice brindado

    v:V3

    """
    def transform_vertex(self, v):

        # V3 -> V4 // Para poder ser multiplicado con matrices de 4x4
        aumented_vertex = V4(v.x, v.y, v.z)

        # Multiplicación de matrices con el Vector en el orden correspondiente
        if (self.View and self.Projection and self.Viewport):
            temp = self.ModelM     * aumented_vertex
            temp = self.View       * temp
            temp = self.Projection * temp
            # temp = self.Viewport   * temp (no en uso temporalmente)

        # Si no se utliza la función lookAt, se hace una transformación
        # Simple de los vértices
        else:
            temp = self.ModelM * aumented_vertex

        # V4 -> V3
        # return (
        #     temp.x / temp.w, 
        #     temp.y / temp.w, 
        #     temp.z / temp.w
        #     )

        # V4 -> V3
        return (
            temp.x, 
            temp.y, 
            temp.z
            )

    """
    line:Void
    
    Genera una línea del color actual dado 2 puntos

    i:(int, int) Punto inicial
    f:(int, int) Punto final

    """
    def line (self, i, f):

        
        # puntos inicial y final
        x1, y1 = i
        x2, y2 = f

        # precaución
        x1 = round(x1)
        y1 = round(y1)
        x2 = round(x2)
        y2 = round(y2)
        
        # razones de cambio
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        pen = dy > dx

        # Revisamos si en necesario invertir valores (para facilitar la impresión)

        # Invertir los valores si 
        if (pen):
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        # Si el punto inicial , invertir los valores
        if ( x1 > x2):
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        # Recalculamos las razones de cambio si ocurrieron cambios
        dy = abs(y2 - y1)
        dx = abs(x2 - x1)

        offset = 0
        threshold = dx

        y = y1 # empezamos la línea en y1
        for x in range(x1, x2 + 1):
            if (pen):
                self.point(y, x)
            else:
                self.point(x, y)

            # Modificamos el offset (en lugar de redondear)
            offset += dy * 2
            if (offset >= threshold):
                y += 1 if (y1 < y2) else -1
                threshold += dx * 2

    """
    line:Void
    
    Genera una línea del color actual dado 2 puntos

    Parámetros:
    i:(int, int) Vector Punto inicial
    f:(int, int) Vector Punto final

    """
    def line_vector (self, i, f):

        # precaución
        x1 = round(i.x)
        y1 = round(i.y)
        x2 = round(f.x)
        y2 = round(f.y)
        
        # razones de cambio
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        pen = dy > dx

        # Revisamos si en necesario invertir valores (para facilitar la impresión)

        # Invertir los valores si 
        if (pen):
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        # Si el punto inicial , invertir los valores
        if ( x1 > x2):
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        # Recalculamos las razones de cambio si ocurrieron cambios
        dy = abs(y2 - y1)
        dx = abs(x2 - x1)

        offset = 0
        threshold = dx

        y = y1 # empezamos la línea en y1
        for x in range(x1, x2 + 1):
            if (pen):
                self.point(y, x)
            else:
                self.point(x, y)

            # Modificamos el offset (en lugar de redondear)
            offset += dy * 2
            if (offset >= threshold):
                y += 1 if (y1 < y2) else -1
                threshold += dx * 2

    """
    line_vertex:Void
    
    Genera una línea con el color actual dado 2 puntos que luego
    transforma dentro del viewport 

    Parámetros:
    i:(int, int) Punto inicial
    f:(int, int) Punto final

    """
    def line_vertex(self, i, f):
        # puntos inicial y final
        x1, y1 = i
        x2, y2 = f

        # transformamos a puntos en el ViewPort
        x1 = self.x_min + round((1/2)*self.width_vp + x1*(1/2)*self.width_vp)
        y1 = self.y_min + round((1/2)*self.height_vp + y1*(0.5)*self.height_vp)

        x2 = self.x_min + round((1/2)*self.width_vp + x2*(1/2)*self.width_vp)
        y2 = self.y_min + round((1/2)*self.height_vp + y2*(0.5)*self.height_vp)
        
        # razones de cambio
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        pen = dy > dx

        # Revisamos si en necesario invertir valores (para facilitar la impresión)

        # Invertir los valores si 
        if (pen):
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        # Si el punto inicial , invertir los valores
        if ( x1 > x2):
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        # Recalculamos las razones de cambio si ocurrieron cambios
        dy = abs(y2 - y1)
        dx = abs(x2 - x1)

        offset = 0
        threshold = dx

        y = y1 # empezamos la línea en y1
        for x in range(x1, x2 + 1):
            if (pen):
                self.point(y, x)
            else:
                self.point(x, y)

            # Modificamos el offset (en lugar de redondear)
            offset += dy * 2
            if (offset >= threshold):
                y += 1 if (y1 < y2) else -1
                threshold += dx * 2

    """
    triangle_vector:Void
    
    Genera un triángulo coloreado dado 3 vectores.

    Parámetros:
    A:V3
    B:V3
    C:V3

    """
    def triangle_vector_gray(self, A, B, C):  

        Light = V3(0, 0.5, 1)
        Norm = (B - A) * (C - A)
        intensity = Norm.normalize() @ Light.normalize() 

        if (intensity < 0):
            # return
            intensity = abs(intensity)

        gris = round(255 * intensity)

        self.current_color = color(gris, gris, gris)


        box_min, box_max = self.bounding_box(A, B, C)
        for x in range(round(box_min.x), round(box_max.x) + 1):
            for y in range(round(box_min.y), round(box_max.y) + 1):
                w, v, u = self.barycentric(A, B, C, V3(x, y))

                if (w < 0 or v < 0 or u < 0):
                    """"""
                    continue

                z = A.z * w + B.z * u + C.z * v

                if (self.zBuffer[x][y] < z  ):
                    self.zBuffer[x][y] = z
                    self.point(x, y)

    """
    triangle_vector_color:Void

    Genera triángulos coloreados a partir de una textura brindada y 3 vectores

    Parámetros:
    A:V3
    B:V3
    C:V3
    texture:Texture
    tcoords:(int, int, int)

    """
    def triangle_vector_color(self, 
        A, B, C, 
        texture, 
        tcoords,
        ncoords
        ):

        # Light = V3(0, 0.5, 1)
        # Norm = (B - A) * (C - A)
        # intensity = Norm.normalize() @ Light.normalize() 

        # if (intensity < 0):
        #     # return
        #     intensity = abs(intensity)

        box_min, box_max = self.bounding_box(A, B, C)
        for x in range(round(box_min.x), round(box_max.x) + 1):
            for y in range(round(box_min.y), round(box_max.y) + 1):
                w, v, u = self.barycentric(A, B, C, V3(x, y))

                color = (0, 0, 0)

                if (w < 0 or v < 0 or u < 0):
                    """"""
                    continue

                z = A.z * w + B.z * u + C.z * v

                if (0 < x < len(self.zBuffer) and 0 < y < len(self.zBuffer[0])):
                    if (self.zBuffer[x][y] < z):
                        self.zBuffer[x][y] = z 

                        
                        self.current_color = self.active_shader(
                            y = y,
                            x = x,
                            bar = (w, u, v),
                            coords = (A, B, C),
                            ncoords = ncoords,
                            tcoords = tcoords, 
                            textures = texture,
                            model = self
                            )
  
                        # else: 
                        #     if texture:
                        #         vt1, vt2, vt3 = tcoords

                        #         tx = vt1.x * w + vt2.x * u + vt3.x * v
                        #         ty = vt1.y * w + vt2.y * u + vt3.y * v

                        #         self.current_color = texture.get_color_with_intensity(tx, ty, intensity)

                        self.point(x, y)


    """
    bounding_box:(V3, V3)

    Dados 3 vectores, determina los límites del triángulo que generan

    Parámetros: 
    v1:V3
    v2:V3
    v3:V3

    """
    def bounding_box(self, v1, v2, v3):
        cordenadas = [(v1.x, v1.y), (v2.x, v2.y), (v3.x, v3.y)]

        x_min = 999999
        x_max = -999999
        y_min = 999999
        y_max = -999999

        for (x, y) in cordenadas:
            if x < x_min:
                x_min = x
            if x > x_max:
                x_max = x
            if y < y_min:
                y_min = y
            if y > y_max:
                y_max = y

        return (V3(x_min, y_min), V3(x_max, y_max))

    """
    barycentric:(float, float, float)
    
    Retorna las coordenadas varicéntricas

    Parámetros:
    A:V3
    B:V3
    C:V3
    P:V3

    """
    def barycentric(self, A, B, C, P):

        cordenada = V3(B.x - A.x, C.x - A.x, A.x - P.x) * V3(B.y - A.y, C.y - A.y, A.y - P.y)

        c_x = cordenada.x
        c_y = cordenada.y
        c_z = cordenada.z

        u= 0
        v = 0
        w = 0

        if (c_z != 0):
            u = c_x / c_z
            v = c_y / c_z
            w = 1 - (u + v)

        return (w, v, u)
        

    """
    fillTriange: Función que genera líneas desde un punto centro hacia
    cada uno de los puntos que se generan al pintar una línea con un punto
    inicial y un punto final

    Parámetros:
    p1:(int, int) Punto inicial de la línea
    p2:(int, int) Punto final de la línea
    c:(int, int) Punto desde donde se generan líneas hacia la línea que se genera
      entre p1 y p2
    
    """
    def fillTriangle_center(self, p1, p2, c):
        # puntos inicial y final
        x1, y1 = p1
        x2, y2 = p2

        # razones de cambio
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        pen = dy > dx

        # Revisamos si en necesario invertir valores (para facilitar la impresión)

        # Invertir los valores si 
        if (pen):
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        # Si el punto inicial , invertir los valores
        if ( x1 > x2):
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        # Recalculamos las razones de cambio si ocurrieron cambios
        dy = abs(y2 - y1)
        dx = abs(x2 - x1)

        offset = 0
        threshold = dx

        y = y1 # empezamos la línea en y1
        for x in range(x1, x2 + 1):
            if (pen):
                # self.point(y, x)
                orilla = (y, x)
                self.line(c, orilla)
            else:
                #self.point(x, y)
                orilla = (x, y)
                self.line(c, orilla)

            # Modificamos el offset (en lugar de redondear)
            offset += dy * 2
            if (offset >= threshold):
                y += 1 if (y1 < y2) else - 1
                threshold += dx * 2

    """
    load_model_wire:Void
    
    Genera las arístas entre los vértices dado un modelo 3D por medio de líneas no vectoriales

    Parámetros:
    modelo_objeto:Obj Modelo 3D que se desea generar
    scale_factor:(int, int) Escala en x y y para agrandar y achiquitar el objeto
    transformation:int Pixeles en x y y de cuánto se desea mover el objeto en la pantalla

    """
    def load_model_wire(self, modelo_objeto, scale_factor, transformation):
        o = modelo_objeto

        for face in o.faces:
    
            if (len(face) == 3):
                f1 = face[0][0] -1
                f2 = face[1][0] -1
                f3 = face[2][0] -1

                v1 = self.transform_vertex(V3(*o.vertices[f1]))
                v2 = self.transform_vertex(V3(*o.vertices[f2]))
                v3 = self.transform_vertex(V3(*o.vertices[f3]))

                # generar triángulo
                self.line_vector(V3(v1[0], v1[1]), V3(v2[0], v2[1]))
                self.line_vector(V3(v2[0], v2[1]), V3(v3[0], v3[1]))
                self.line_vector(V3(v3[0], v3[1]), V3(v1[0], v1[1]))

            if (len(face) == 4):
                f1 = face[0][0] -1
                f2 = face[1][0] -1
                f3 = face[2][0] -1
                f4 = face[3][0] -1

                v1 = self.transform_vertex(V3(*o.vertices[f1]))
                v2 = self.transform_vertex(V3(*o.vertices[f2]))
                v3 = self.transform_vertex(V3(*o.vertices[f3]))
                v4 = self.transform_vertex(V3(*o.vertices[f4]))

                # generar las líneas
                self.line_vector(V3(v1[0], v1[1]), V3(v2[0], v2[1]))
                self.line_vector(V3(v2[0], v2[1]), V3(v3[0], v3[1]))
                self.line_vector(V3(v3[0], v3[1]), V3(v4[0], v4[1]))
                self.line_vector(V3(v4[0], v4[1]), V3(v1[0], v1[1]))


        self.glFinish()

    """
    load_model_color:Void

    Colorea un modelo 3D con tonalidades de gris dependiendo de la iluminación

    Parámetros:
    modelo_objeto:Obj Modelo 3D que se desea generar
    scale_factor:(int, int) Escala en x y y para agrandar y achiquitar el objeto
    transformation:int Pixeles en x y y de cuánto se desea mover el objeto en la pantalla
    
    """
    def load_model_color(
        self, modelo_objeto, 
        scale_factor = (1, 1, 1), 
        transformation =(0, 0, 0), 
        rotation = (0,0,0), 
        texture = None
        ):

        # Generación de matrices de transformación
        self.loadModelMatrix(transformation, scale_factor, rotation)

        o = modelo_objeto

        for face in o.faces:

            if (len(face) == 3):
                f1 = face[0][0] -1
                f2 = face[1][0] -1
                f3 = face[2][0] -1

                v1 = self.transform_vertex(V3(*o.vertices[f1]))
                v2 = self.transform_vertex(V3(*o.vertices[f2]))
                v3 = self.transform_vertex(V3(*o.vertices[f3]))

                if not texture:
                    # generar triángulo
                    self.triangle_vector_gray(V3(v1[0], v1[1], v1[2]), V3(v2[0], v2[1], v2[2]), V3(v3[0], v3[1], v3[2]))

                else:
                    # texturas (face texture)
                    ft1 = face[0][1] -1
                    ft2 = face[1][1] -1
                    ft3 = face[2][1] -1

                    vt1 = V3(o.tvertices[ft1][0], o.tvertices[ft1][1])
                    vt2 = V3(o.tvertices[ft2][0], o.tvertices[ft2][1])
                    vt3 = V3(o.tvertices[ft3][0], o.tvertices[ft3][1])

                    # normales (face normal)
                    fn1 = face[0][2] -1
                    fn2 = face[1][2] -1
                    fn3 = face[2][2] -1

                    vn1 = V3(*o.tvertices[fn1])
                    vn2 = V3(*o.tvertices[fn2])
                    vn3 = V3(*o.tvertices[fn3])

                    # Obtiene el número de la textura a utilizar
                    num_texture = o.tvertices[ft1][2]

                    # Generar triángulo con textura
                    self.triangle_vector_color(
                        V3(*v1), 
                        V3(*v2), 
                        V3(*v3), 
                        texture[num_texture], 
                        (vt1, vt2, vt3),
                        (vn1, vn2, vn3)
                    )


            if (len(face) == 4):
                f1 = face[0][0] -1
                f2 = face[1][0] -1
                f3 = face[2][0] -1
                f4 = face[3][0] -1

                v1 = self.transform_vertex(V3(*o.vertices[f1]))
                v2 = self.transform_vertex(V3(*o.vertices[f2]))
                v3 = self.transform_vertex(V3(*o.vertices[f3]))
                v4 = self.transform_vertex(V3(*o.vertices[f4]))


                if not texture:
                    # Generar triángulos grises
                    self.triangle_vector_gray(V3(v1[0], v1[1], v1[2]), V3(v2[0], v2[1], v2[2]), V3(v3[0], v3[1], v3[2]))
                    self.triangle_vector_gray(V3(v1[0], v1[1], v1[2]), V3(v3[0], v3[1], v3[2]), V3(v4[0], v4[1], v4[2]))

                else:
                    # Generar triánglos con textura
                    ft1 = face[0][1] -1
                    ft2 = face[1][1] -1
                    ft3 = face[2][1] -1
                    ft4 = face[3][1] -1

                    vt1 = V3(o.tvertices[ft1][0], o.tvertices[ft1][1])
                    vt2 = V3(o.tvertices[ft2][0], o.tvertices[ft2][1])
                    vt3 = V3(o.tvertices[ft3][0], o.tvertices[ft3][1])
                    vt4 = V3(o.tvertices[ft4][0], o.tvertices[ft4][1])

                    # normales (face normal)
                    fn1 = face[0][2] -1
                    fn2 = face[1][2] -1
                    fn3 = face[2][2] -1
                    fn4 = face[3][2] -1

                    vn1 = V3(*o.tvertices[fn1])
                    vn2 = V3(*o.tvertices[fn2])
                    vn3 = V3(*o.tvertices[fn3])
                    vn4 = V3(*o.tvertices[fn4])

                    # Obtiene el número de la textura a utilizar
                    num_texture = o.tvertices[ft1][2]

                    # Generar triángulo con textura
                    self.triangle_vector_color(
                        V3(*v1), 
                        V3(*v2), 
                        V3(*v3), 
                        texture[num_texture], 
                        (vt1, vt2, vt3), 
                        (vn1, vn2, vn3)
                        )

                    self.triangle_vector_color(
                        V3(*v1), 
                        V3(*v3), 
                        V3(*v4), 
                        texture[num_texture], 
                        (vt1, vt3, vt4),
                        (vn1, vn3, vn4)
                        )

        # Renderizar modelo terminado
        self.glFinish()

    """
    loadViewMatrix:Void

    Genera la matriz de vista para deformar los vértices
    
    x:V3
    y:V3
    z:V3
    center:V3

    """
    def loadViewMatrix(self, x, y, z, center):
        Mi = M4([
            [x.x, x.y, x.z, 0],
            [y.x, y.y, y.z, 0],
            [z.x, z.y, z.z, 0],
            [  0,   0,   0, 1]
        ])

        Op = M4([
            [1, 0, 0, -center.x],
            [0, 1, 0, -center.y],
            [0, 0, 1, -center.z],
            [0, 0, 0,         1]
        ])

        self.View = Mi * Op

    """
    loadProjectionMatrix:Void

    Genera la matriz de proyección de perspectiva

    coeff:float Coeficiente con el que se genera la perspectiva el
     cuál depende de la cámara y dónde se encuentran los objetos
    
    """
    def loadProjectionMatrix(self, coeff):
        self.Projection = M4([
            [1, 0, 0, 0], 
            [0, 1, 0, 0], 
            [0, 0, 1, 0], 
            [0, 0, coeff, 1] 
        ])

    """
    loadViewPortMatrix:Void

    Genera la matriz para que los objetos queden dentro del viewport
    """
    def loadViewportMatrix(self, x = 0, y = 0):
        x = 0
        y = 0
        w = self.width/2
        h = self.height/2

        self.Viewport = M4([
            [w, 0,   0, x + w], 
            [0, h,   0, y + h], 
            [0, 0, 128,   128], 
            [0, 0,   0,     1] 
        ])

    """
    lookAt:Void

    Llama a las funciones para generar las matrices de proyección
    y del viewport

    eye:V3
    center:V3
    up:V3

    """
    def lookAt(self, eye, center, up):
        # Cálculo de variables
        z = (eye - center).normalize()
        x = (up * z).normalize()
        y = (z * x).normalize()

        # Generación de las otras matrices
        self.loadViewMatrix(x, y, z, center)
        self.loadProjectionMatrix((-1 / (eye - center).length()))
        self.loadViewportMatrix()
