# F = open('Rhom', 'w')
# F.write('can this be read?\n')
# F.write('what do you think?')
# F.close()
#
# G = open('Rhom', 'r')
# text = G.read()
# print(text)

class A :
    def __init__(self):
        self.x = -10
        self.y = 0
        self.z = 10

    def show(self):
        print(self.x, self.y, self.z)

class B :
    def __init__(self, objA):
        self.a = objA.copy()

    def modify(self):
        self.a.x = 10
        self.a.z = -10

obA = A()
obB = B(obA)
obB.modify()
obA.show()