from BMP_func import *

"""
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

r.glFinish('b.bmp')
"""

#"""
r = Render(1024,1024)
r.glInit(1024,1024)

# funciones a utilizar 
def set_glColor():
    color_loop = True
    while (color_loop):
        print("\nDe qué color desea hacer el punto?")
        print("1) Negro")
        print("2) Blanco")
        print("3) Rojo")
        print("4) Anaranjado")
        print("5) Azul")
        print("6) Verde")

        op_color = input()
        
        if (op_color == '1'):
            r.glColor(BLACK)
            color_loop = False
        
        elif (op_color == '2'):
            r.glColor(WHITE)
            color_loop = False

        elif (op_color == '3'):
            r.glColor(RED)
            color_loop = False

        elif (op_color == '4'):
            r.glColor(ORANGE)
            color_loop = False

        elif (op_color == '5'):
            r.glColor(BLUE)
            color_loop = False
        
        elif (op_color == '6'):
            r.glColor(GREEN)
            color_loop = False

        else:
            print("Error: Elija un color válido")

def check_pos(max, simb):
    valor = 0
    position_loop = True
    while (position_loop):
        try:
            print("Indique el valor de ", simb, " entre 0 y ", max )
            pos = int(input())

            if (pos < 0 or pos > max):
                print("Número inválido")

            else:
                valor = pos
                position_loop = False

        except ValueError:
            print("Input inválido")
    return valor

def genOutline(puntos):
    for i in range(len(puntos)):
        f = i+1
        if (i >= len(puntos) -1):
            f = 0
            r.line(puntos[i], puntos[f])
        else:
            r.line(puntos[i], puntos[f])

def fillShape_center(puntos):
    x_sum = 0
    for x in puntos:
        val1, val2 = x
        x_sum += val1
    x_med = int(x_sum/len(puntos))

    y_sum = 0
    for y in puntos:
        val1, val2 = y
        y_sum += val2
    y_med = int(y_sum/len(puntos))

    centro = (x_med, y_med)

    for i in range(len(puntos)):
        f = i+1
        if (i >= len(puntos) -1):
            f = 0
            r.fillTriangle(puntos[i], puntos[f], centro)
            r.fillTriangle(puntos[f], centro, puntos[i])
        else:
            r.fillTriangle(puntos[i], puntos[f], centro)
            r.fillTriangle(puntos[f], centro, puntos[i])




menu = True
while (menu):
    print("\nQué desea realizar")
    print("1) Crear un punto")
    print("2) Crear un cuadro")
    print("3) Crear una línea")
    print("4) Cambiar tamaño")
    print("5) Clear")
    print("6) Cambiar color del clear")
    print("7) Renderizar")
    print("8) Salir")

    op = input('op: ')

    # Opción: Crear un punto
    if (op == '1'):

        # Definir color 
        set_glColor()

        # Posicion del punto
        pos_x = check_pos(r.width, 'x')
        pos_y = check_pos(r.height, 'y')

        r.point(pos_x, pos_y)

        r.glFinish('b.bmp')
    
    # Opción: Crear un cuadrado
    elif (op == '2'):
        
        # Definir color del cuadro
        set_glColor()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

    # Opción: Crear una línea
    elif (op == '3'):
        
        # Definir color de la línea
        set_glColor()

        # Definir punto inicial y final de la línea
        pos_x1 = check_pos(r.width, 'x1')
        pos_y1 = check_pos(r.height, 'y1')

        pos_x2 = check_pos(r.width, 'x2')
        pos_y2 = check_pos(r.height, 'y2')

        r.line((pos_x1, pos_y1), (pos_x2, pos_y2))

        r.glFinish('b.bmp')


    # Opción: Cambiar de tamaño
    elif (op == '4'):
        """"""

    # Opción: Clear
    elif (op == '5'):
        r.glClear()
        r.glFinish('b.bmp')

    # Opción: Cambiar color del clear
    elif (op == '6'):
        color_loop = True
        while (color_loop):
            print("\nQué color?")
            print("1) Negro")
            print("2) Blanco")
            print("3) AAA")
            print("4) Anaranjado")
            print("5) Otro")

            op_color = input()
            
            if (op_color == '1'):
                r.glClearColor(BLACK)
                color_loop = False
            
            elif (op_color == '2'):
                r.glClearColor(WHITE)
                color_loop = False

            elif (op_color == '3'):
                r.glClearColor(RED)
                color_loop = False

            elif (op_color == '4'):
                r.glClearColor(ORANGE)
                color_loop = False

            else:
                print("Error: Elija un color válido")

    # Opción : Salir
    elif (op == '8'):
        menu = False

    else: 
        print("\n[La opción ingresada no es válida]")
#"""