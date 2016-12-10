from tpi3 import *

names = ['André', 'Bernardo', 'Cláudio', 'Eduardo']

def friends_constraint(f1, bh1, f2, bh2):
    if bh1[0] == bh2[0] or bh1[1] == bh2[1]:
        return False
    if bh1[0] == 'Bernardo' and bh1[1] != 'Cláudio'\
            or bh2[0] == 'Bernardo' and bh2[1] != 'Cláudio':
                return False
    return True

def make_domains():
    return {f:[(b, h) for b in names for h in names\
            if f != b and f != h and b != h]\
            for f in names}

def make_constraint_graph():
    return {(f1, f2):friends_constraint for f1 in make_domains() for f2 in names\
            if f1 != f2}

cs = MyCS(make_domains(), make_constraint_graph())
s = cs.search_all()

print(len(s))
