class Node:
    def __init__(self, data):
        self.data = data
        self.rigth_child = None
        self.left_child = None
        
NodoPadre = Node("Padre")
NodoHijo = Node("Hijo")
NodoHijo2 = Node("Hijo2")
NodoHijo3 = Node("Hijo3")
NodoHijo4 = Node("Hijo4")

NodoPadre.rigth_child = NodoHijo
NodoHijo.rigth_child = NodoHijo2
NodoHijo2.rigth_child = NodoHijo3
NodoHijo3.rigth_child = NodoHijo4

current = NodoPadre
while current:
    print(current.data)
    current = current.rigth_child