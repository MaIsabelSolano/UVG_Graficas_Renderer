from BMP_func import *

#"""
r = Render(1440,1440)

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
    print("2) Crear una línea")
    print("3) Clear")
    print("4) Cambiar color del clear")
    print("5) Generar outline de formas")
    print("6) Colorear figuras")
    print("7) Salir")

    op = input('op: ')

    # Opción: Crear un punto
    if (op == '1'):

        # Definir color 
        set_glColor()

        # Posicion del punto
        pos_x = check_pos(r.width, 'x')
        pos_y = check_pos(r.height, 'y')

        r.point(pos_x, pos_y)

        # Escribir al archivo
        r.glFinish('Lab1.bmp')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

    # Opción: Crear una línea
    elif (op == '2'):
        
        # Definir color de la línea
        set_glColor()

        # Definir punto inicial y final de la línea
        pos_x1 = check_pos(r.width, 'x1')
        pos_y1 = check_pos(r.height, 'y1')

        pos_x2 = check_pos(r.width, 'x2')
        pos_y2 = check_pos(r.height, 'y2')

        r.line((pos_x1, pos_y1), (pos_x2, pos_y2))

        # Escribir al archivo
        r.glFinish('Lab1.bmp') 

    # Opción: Clear
    elif (op == '3'):
        r.glClear()
        
        # Escribir al archivo
        r.glFinish('Lab1.bmp') 

    # Opción: Cambiar color del clear
    elif (op == '4'):
        color_loop = True
        while (color_loop):
            print("\nQué color?")
            print("1) Negro")
            print("2) Blanco")
            print("3) Rojo")
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

    # Generar outline de formas
    elif (op == '5'):
        
        # polígonos
        pol1 = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360),
                (250, 380), (220, 385), (205, 410), (193, 383)]
        
        pol2 = [(321, 335), (288, 286), (339, 251), (374, 302)]
        
        pol3 = [(377, 249), (411, 197), (436, 249)]
        
        pol4 = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37),
                (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214),
                (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180)]
        
        pol5 = [(682, 175), (708, 120), (735, 148), (739, 170)]

        # Determinar color
        set_glColor()

        # Generar el outline
        genOutline(pol1)
        genOutline(pol2)
        genOutline(pol3)
        genOutline(pol4)
        genOutline(pol5)

        
        # Escribir al archivo
        r.glFinish('Lab1.bmp') 

    # Colorear formas
    elif (op == '6'):

        # Determinar color
        set_glColor()

        # Sacar el centro de la estrella, cuadrado y tríangulo
        pol1 = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360),
                (250, 380), (220, 385), (205, 410), (193, 383)]

        pol2 = [(321, 335), (288, 286), (339, 251), (374, 302)]
        
        pol3 = [(377, 249), (411, 197), (436, 249)]

        # Llenar las figuras pequeñas
        fillShape_center(pol1)
        fillShape_center(pol2)
        fillShape_center(pol3)

        # Comenzar a llenar la tetera
        r.fillTriangle((502, 88), (466, 180), (448, 159))
        r.fillTriangle((466, 180), (448, 159), (502, 88)) #
        r.fillTriangle((413, 177), (448, 159), (466, 180))
        r.fillTriangle((448, 159), (466, 180), (413, 177)) #
        r.fillTriangle((502, 88), (553, 53), (466, 180))
        r.fillTriangle((553, 53), (466, 180), (502, 88)) #
        r.fillTriangle((553, 53), (517, 144), (466, 180))
        r.fillTriangle((553, 53), (552, 214), (517, 144))
        r.fillTriangle((553, 53), (552, 214), (659, 214))
        r.fillTriangle((552, 214), (659, 214), (553, 53)) #
        r.fillTriangle((632, 230), (580, 230), (597, 215))
        r.fillTriangle((597, 215), (632, 230), (615, 214))
        r.fillTriangle((632, 230), (615, 214), (597, 215)) #
        r.fillTriangle((553, 53), (660, 52), (659, 214))
        r.fillTriangle((660, 52), (659, 214), (553, 53)) #
        r.fillTriangle((553, 53), (535, 36), (676, 37))
        r.fillTriangle((535, 36), (676, 37), (553, 53)) #
        r.fillTriangle((553, 53), (676, 37), (660, 52))
        r.fillTriangle((676, 37), (660, 52), (553, 53)) #
        r.fillTriangle((659, 214), (660, 52), (682, 175))
        r.fillTriangle((660, 52), (682, 175), (659, 214)) #
        r.fillTriangle((660, 52), (682, 175), (708, 120))
        r.fillTriangle((682, 175), (708, 120), (660, 52)) #
        r.fillTriangle((708, 120), (660, 52), (682, 175)) #
        r.fillTriangle((660, 52), (750, 145), (708, 120))
        r.fillTriangle((750, 145), (708, 120), (660, 52)) #
        r.fillTriangle((750, 145), (708, 120), (735, 148))
        r.fillTriangle((708, 120), (735, 148), (750, 145)) #
        r.fillTriangle((750, 145), (761, 179), (735, 148))
        r.fillTriangle((735, 148), (739, 170), (761, 179))
        r.fillTriangle((761, 179), (672, 192), (682, 175))
        r.fillTriangle((672, 192), (682, 175), (761, 179))
        r.fillTriangle((761, 179), (682, 175), (739, 170))
        r.fillTriangle((682, 175), (739, 170), (761, 179)) #

        # Escribir al archivo
        r.glFinish('Lab1.bmp')  
    
    # Opción : Salir
    elif (op == '7'):
        menu = False

    else: 
        print("\n[La opción ingresada no es válida]")
#"""