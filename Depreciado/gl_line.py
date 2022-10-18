import struct 

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
        self.current_color = WHITE
        self.clear_color = WHITE
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

    """
    glClearColor: Determina el color con el que se realizará el Clear

    Parámetros:
    c:(r,g,b) Color con el que se pintará
    """
    def glClearColor(self, c):
        self.clear_color = c

    """
    glViewPort: Genera una ventana en la que se podrá
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
    glFinish: Escribe todo lo necesario para generar un archivo bmp y convierte cada
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
    Point: Cambia un color del Framebuffer al color actual

    Parámetros:
    x:int Posición en x del punto
    y:int Posición en y del punto
    """
    def point(self, x, y):
        # pinta un color utilizando un puntero
        self.framebuffer[y][x] = self.current_color

    """
    Vertex: Genera un punto en la posición establecida en el ViewPort

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
    line: Genera una línea del color actual dado 2 puntos

    i:(int, int) Punto inicial
    f:(int, int) Punto final
    """
    def line (self, i, f):
        
        # puntos inicial y final
        x1, y1 = i
        x2, y2 = f

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
    fillTriange: Función que genera líneas desde un punto centro hacia
    cada uno de los puntos que se generan al pintar una línea con un punto
    inicial y un punto final

    Parámetros:
    p1:(int, int) Punto inicial de la línea
    p2:(int, int) Punto final de la línea
    c:(int, int) Punto desde donde se generan líneas hacia la línea que se genera
      entre p1 y p2
    """
    def fillTriangle(self, p1, p2, c):
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
                y += 1 if (y1 < y2) else -1
                threshold += dx * 2

    """
    glColor: Cambia el color actual que se está utilizando
    """
    def glColor(self, c):
        self.current_color = c
