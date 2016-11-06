#
# Modulo: cidades
# 
# Implementacao de um dominio para planeamento de caminhos
# entre cidades usando para esse efeito o modulo tree_search
#
# (c) Luis Seabra Lopes, Introducao a Inteligencia Artificial, 2012/2013
#

import math
from tree_search import *

class Cidades(SearchDomain):
    def __init__(self,connections, coordinates):
        self.connections = connections
        self.coordinates = coordinates
    def actions(self,cidade):
        actlist = []
        for (C1,C2,D) in self.connections:
            if (C1==cidade):
                actlist += [(C1,C2)]
            elif (C2==cidade):
               actlist += [(C2,C1)]
        return actlist 
    def result(self,cidade,action):
        (C1,C2) = action
        if C1==cidade:
            return C2
    def cost(self, state, action):
        for (c1, c2, d) in self.connections:
            if (c1, c2) == action or (c2, c1) == action:
                return d
        return None
    def heuristic(self, state, goal):
        coor1 = self.coordinates[state]
        coor2 = self.coordinates[goal]
        return math.sqrt((coor1[0] - coor2[0])**2 + (coor1[1] - coor2[1])**2)

cidades_portugal = Cidades( 
                    # Ligacoes por estrada
                    [
                      ('Coimbra', 'Leiria', 73),
                      ('Aveiro', 'Agueda', 35),
                      ('Porto', 'Agueda', 79),
                      ('Agueda', 'Coimbra', 45),
                      ('Viseu', 'Agueda', 78),
                      ('Aveiro', 'Porto', 78),
                      ('Aveiro', 'Coimbra', 65),
                      ('Figueira', 'Aveiro', 77),
                      ('Braga', 'Porto', 57),
                      ('Viseu', 'Guarda', 75),
                      ('Viseu', 'Coimbra', 91),
                      ('Figueira', 'Coimbra', 52),
                      ('Guarda', 'Castelo Branco', 96),
                      ('Leiria', 'Castelo Branco', 169),
                      ('Figueira', 'Leiria', 62),
                      ('Leiria', 'Santarem', 78),
                      ('Santarem', 'Lisboa', 82),
                      ('Santarem', 'Castelo Branco', 160),
                      ('Castelo Branco', 'Viseu', 174),
                      ('Santarem', 'Evora', 122),
                      ('Lisboa', 'Evora', 132),
                      ('Evora', 'Beja', 80),
                      ('Lisboa', 'Beja', 178),
                      ('Faro', 'Beja', 147) ],

                    # Coordenadas das cidades:
                     { 'Aveiro': (41,215),
                       'Figueira': ( 24, 161),
                       'Coimbra': ( 60, 167),
                       'Agueda': ( 58, 208),
                       'Viseu': ( 104, 217),
                       'Braga': ( 61, 317),
                       'Porto': ( 45, 272),
                       'Lisboa': ( 0, 0),
                       'Santarem': ( 38, 59),
                       'Leiria': ( 28, 115),
                       'Castelo Branco': ( 140, 124),
                       'Guarda': ( 159, 204),
                       'Evora': (120, -10),
                       'Beja': (125, -110),
                       'Faro': (120, -250)
                     } )


p = SearchProblem(cidades_portugal,'Braga','Faro')
t = SearchTree(p,'breadth')
print("breadth:")
print(t.search())

# Atalho para obter caminho de c1 para c2 usando strategy:
def search_path(c1,c2,strategy,boundary=0):
    my_prob = SearchProblem(cidades_portugal,c1,c2)
    my_tree = SearchTree(my_prob, strategy, boundary)
    return my_tree.search()

print("depth - 12 limit:")
print(search_path('Braga', 'Faro', 'depth', 12))
print("depth - 8 limit:")
print(search_path('Braga', 'Faro', 'depth', 8))
print("uniform:")
print(search_path('Braga', 'Faro', 'uniform'))
print("greedy:")
print(search_path('Braga', 'Faro', 'greedy'))
print("a*:")
print(search_path('Braga', 'Faro', 'a*'))

