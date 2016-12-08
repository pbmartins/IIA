from constraintsearch import *

#################################
# Exercise 4
colors = ['azul', 'amarelo', 'vermelho', 'branco', 'cinzento', 'castanho', 'laranja']
color_constraint = lambda p1, c1, p2, c2: c1 != c2
create_cgraph = lambda domain, frontiers: {(country, frontier): color_constraint \
        for country in domain for frontier in frontiers[country]}

# Alinea a)
a_domain = {'A': colors, 'B': colors, 'C': colors, 'D': colors, 'E': colors}
a_frontiers = {
            'A': ['B', 'D', 'E'],
            'B': ['A', 'C', 'E'],
            'C': ['B', 'D', 'E'],
            'D': ['A', 'C', 'E'],
            'E': ['A', 'B', 'C', 'D']
        }

cs_a = ConstraintSearch(a_domain, create_cgraph(a_domain, a_frontiers))
print(cs_a.search())


# Alinea b)
b_domain = {'A': colors, 'B': colors, 'C': colors, 'D': colors, \
        'E': colors, 'F': colors}
b_frontiers = {
            'A': ['B', 'D', 'E'],
            'B': ['A', 'C', 'E'],
            'C': ['B', 'E', 'F'],
            'D': ['A', 'E', 'F'],
            'E': ['A', 'B', 'C', 'D', 'F'],
            'F': ['C', 'D', 'E']
        }

cs_b = ConstraintSearch(b_domain, create_cgraph(b_domain, b_frontiers))
print(cs_b.search())


# Alinea c)
c_domain = {'A': colors, 'B': colors, 'C': colors, 'D': colors, \
        'E': colors, 'F': colors, 'G': colors}
c_frontiers = {
            'A': ['B', 'D', 'E', 'F'],
            'B': ['A', 'C', 'F'],
            'C': ['B', 'D', 'F', 'G'],
            'D': ['A', 'C', 'E', 'G'],
            'E': ['A', 'D', 'F', 'G'],
            'F': ['A', 'B', 'C', 'E', 'G'],
            'G': ['C', 'D', 'E', 'F']
        }

cs_c = ConstraintSearch(c_domain, create_cgraph(c_domain, c_frontiers))
#print(cs_c.search())


#################################
# Exercise 5
friends = ['André', 'Bernardo', 'Cláudio', 'Daniel']
all_combs = [(b, c) for b in friends for c in friends]
domain = {f: [(b, c) for b in friends for c in friends \
        if b != f and c != f and b != c] for f in friends}
def friends_rest(f1, comb1, f2, comb2):
    b1, c1 = comb1
    b2, c2 = comb2
    if c1 == 'Cláudio' and b1 != 'Bernardo' or c2 == 'Cláudio' and b2 != 'Bernardo':
        return False

    if b1 == b2 or c1 == c2:
        return False
    return True

restrictions = {(f1, f2): friends_rest for f1 in friends for f2 in friends if f1 != f2}
cs = ConstraintSearch(domain, restrictions)
print(cs.search())

