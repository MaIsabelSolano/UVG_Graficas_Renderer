import struct

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w): 
    # 2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

# clase color, recibe en rgb y lo retorna en bytes en el orden requerido
def color(r, g, b):
    return bytes([b, g, r])

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
AAA = color(250, 0, 0)

class Render(object):
    def __init__(self, width, height):
        # puede quedar vacío
        self.width = width
        self.height = height
        self.current_color = WHITE
        self.clear()

    # inicializa con un color
    def clear(self):
        self.framebuffer = [
            [BLACK for x in range(self.width)]
            for y in range(self.height)
        ]

    def write(self, filename):
        f = open(filename, 'bw')

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

    def point(self, x, y):
        # pinta un color utilizando un puntero
        self.framebuffer[x][y] = self.current_color


#r = Render(1024, 1024)
r = Render(1280, 720)

r.current_color = (color( 200, 100, 0))

for x in range(200, 300):
    for y in range (200, 300):
        r.point(x, y)

r.current_color = (color( 100, 100, 255))

for x in range(300, 400):
    for y in range (300, 400):
        r.point(x, y)

r.write('a.bmp')