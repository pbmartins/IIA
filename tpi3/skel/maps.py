from tpi3 import *

maps = ['A', 'B', 'C', 'D', 'E']
colors = ['blue', 'red', 'green']

def map_constraint(p1, c1, p2, c2):
    return not c1 == c2

def make_domains():
    return {m:colors for m in maps}

def make_constraint_graph():
    return {(p, neigh):map_constraint for p in make_domains() for neigh in borders[p]}

borders = {
            'A' : ['B', 'E', 'D'],
            'B' : ['A', 'E', 'C'],
            'C' : ['B', 'E', 'D'],
            'D' : ['A', 'E', 'C'],
            'E' : ['A', 'B', 'C', 'D']
        }

cs = MyCS(make_domains(), make_constraint_graph())
s = cs.search_all()
print(len(s))
