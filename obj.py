class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
        
        self.vertices = []
        self.faces = []

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

            if (prefix == 'f'):
                self.faces.append([
                    list(map(int,face.split('/'))) for face in values.split(' ')
                ])


         