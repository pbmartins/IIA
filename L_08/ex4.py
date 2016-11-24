
from constraintsearch import *

cores = ['azul', 'vermelho', 'verde', 'amarelo', 'cinzento']
mapa_restricao = lambda p1, c1, p2, c2: c1 != c2

mapa_a = {
            'A': cores,
            'B': cores,
            'C': cores,
            'D': cores,
            'E': cores
        }
fronteiras_a = {
            'A': ['B', 'E', 'D'],
            'B': ['A', 'E', 'C'],
            'C': ['B', 'E', 'D'],
            'D': ['A', 'E', 'C'],
            'E': ['A', 'B', 'C', 'D']
        }

restricoes_a = {(pais, vizinho): mapa_restricao for pais in mapa_a for vizinho in fronteiras_a[pais]}
cs = ConstraintSearch(mapa_a, restricoes_a)
print(cs.search())

mapa_b = {
            'A': cores,
            'B': cores,
            'C': cores,
            'D': cores,
            'E': cores,
            'F': cores
        }
fronteiras_b = {
            'A': ['B', 'E', 'D'],
            'B': ['A', 'E', 'C'],
            'C': ['B', 'E', 'F'],
            'D': ['A', 'E', 'C'],
            'E': ['A', 'B', 'C', 'D', 'F'],
            'F': ['C', 'E', 'D']
        }
restricoes_b = {(pais, vizinho): mapa_restricao for pais in mapa_b for vizinho in fronteiras_b[pais]}
cs = ConstraintSearch(mapa_b, restricoes_b)
print(cs.search())

mapa_c = {
            'A': cores,
            'B': cores,
            'C': cores,
            'D': cores,
            'E': cores,
            'F': cores,
            'G': cores
        }
fronteiras_c = {
            'A': ['B', 'E', 'D', 'F'],
            'B': ['A', 'F', 'C'],
            'C': ['B', 'F', 'G', 'D'],
            'D': ['A', 'E', 'G', 'C'],
            'E': ['A', 'F', 'G', 'D'],
            'F': ['A', 'B', 'C', 'G', 'E'],
            'G': ['E', 'F', 'C', 'D']
        }
restricoes_c = {(pais, vizinho): mapa_restricao for pais in mapa_c for vizinho in fronteiras_c[pais]}
cs = ConstraintSearch(mapa_c, restricoes_c)
print(cs.search())

