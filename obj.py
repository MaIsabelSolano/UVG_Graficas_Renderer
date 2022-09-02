class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
        
        self.vertices = []
        self.faces = []
        self.tvertices = []

        # Variables utilizadas para determinar grupos de vértices de textura
        cant_vt = 0
        add = False

        for line in self.lines:
            prefix, values = line.split(' ', 1)

            if (prefix == 'v'): #cambiar a un for
                self.vertices.append(
                    list(
                        map(
                            float, values.split(' ')
                        )
                    )
                )

                # Pequeño if que permite determinar cuántos conjuntos de vt's hay
                if add:
                    cant_vt += 1
                    add = False

            if (prefix == 'vt'): 
                # Se añaden los valores a una lista temporal
                temp = list(
                    map(
                        float, values.split(' ')
                    )
                )
                # A la lista temporal se le añade el número de agrupación de vt's
                temp.append(cant_vt) 
                
                # Se añade la lista temporal a la lista de vértices de textura 
                self.tvertices.append(temp)
                
                # Indica que se está en un grupo de vértices de textura
                add = True

            if (prefix == 'f'):
                self.faces.append([
                    list(map(int,face.split('/'))) for face in values.split(' ')
                ])

                # Pequeño if que permite determinar cuántos conjuntos de vt's hay
                if add:
                    cant_vt += 1
                    add = False


         