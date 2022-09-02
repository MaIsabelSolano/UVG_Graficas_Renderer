class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
        
        self.vertices = []
        self.faces = []
        self.tvertices = []

        tvertices_temp = []
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

                # A
                """
                if add:
                    self.tvertices.append(tvertices_temp)
                    tvertices_temp = []
                    add = False 
                """
                if add:
                    cant_vt += 1
                    add = False

            if (prefix == 'vt'): #cambiar a un for
                temp = list(
                    map(
                        float, values.split(' ')
                    )
                )

                temp.append(cant_vt) 
                
                self.tvertices.append(temp)
                
                add = True

            if (prefix == 'f'):
                self.faces.append([
                    list(map(int,face.split('/'))) for face in values.split(' ')
                ])

                # A
                """
                if add:
                    self.tvertices.append(tvertices_temp)
                    tvertices_temp = []
                    add = False 
                """
                if add:
                    cant_vt += 1
                    add = False


         