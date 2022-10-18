import struct
from gl import *

class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        with open(self.path, "rb") as image:
            # Info del archivo
            image.seek(2 + 4 + 2 +2)
            header_size = struct.unpack("=l", image.read(4))[0]
            image.seek(2 + 4 + 2 + 2 + 4 + 4)

            # Tamaño del archivo
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]

            # Pasamos el encabezado
            image.seek(header_size)

            # Obtenemos todos los colores de la imagen
            self.pixels = []
            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))
                    self.pixels[y].append(
                        color(r, g, b)
                    )

    # depreciada
    def get_color(self, tx, ty):
        x = round(tx * self.width)
        y = round(ty * self.height)

        return self.pixels[y][x]

    def color_minmax_r(self, value):
        if (0 <= value <= 255 ):
            return round(value)
        elif (0 > value):
            return 0
        elif (value > 255):
            return 255

    """
    get_color_with_intensity:(int, int, int)

    Permite obtener los colores que se deben utilizar para cada punto y 
    dada una intensidad de iluminación oscurese el color

    Parámetros:
    tx:float
    ty:float 
    """
    def get_color_with_intensity(self, tx, ty, intensidad = 1):

        if ty >= 1:
            ty -= 1

        x = round(tx * self.width)
        y = round(ty * self.height)

        p_color = color(0, 0, 0)
        
        if (y < len(self.pixels)):
            if (x < len(self.pixels[y])):
                b = round(self.pixels[y][x][0] * intensidad)
                g = round(self.pixels[y][x][1] * intensidad)
                r = round(self.pixels[y][x][2] * intensidad)

                p_color = color(r, g, b)

        return p_color

    def get_color_pastel(self, tx, ty, intensidad = 0, c = None):
        
        if ty >= 1:
            ty -= 1

        x = round(tx * self.width)
        y = round(ty * self.height)

        p_color = color(0, 0, 0)

        if (intensidad < 0.35):
        
            if (y < len(self.pixels)):
                if (x < len(self.pixels[y])):
                    r = round(self.pixels[y][x][2])
                    g = round(self.pixels[y][x][1])
                    b = round(self.pixels[y][x][0])

                    r_2 = 200
                    g_2 = 230
                    b_2 = 200

                    r_n = self.color_minmax_r(((b * g_2) - (g * b_2)))
                    g_n = self.color_minmax_r(((r * b_2) - (b * r_2)))
                    b_n = self.color_minmax_r(((g * r_2) - (r * g_2)))

                    r_n = self.color_minmax_r((r - (r_n / 8)))
                    g_n = self.color_minmax_r((g - (g_n / 8)))
                    b_n = self.color_minmax_r((b - (b_n / 8)))

                    p_color = color(r_n, g_n, b_n)

        else:
            if (y < len(self.pixels)):
                if (x < len(self.pixels[y])):
                    b = round(self.pixels[y][x][0])
                    g = round(self.pixels[y][x][1])
                    r = round(self.pixels[y][x][2])

                    p_color = color(r, g, b)


        return p_color