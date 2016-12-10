#encoding: utf8

from tpi3 import *

import math
import time


# -------------------------------------------------------------
# TWO + TWO = FOUR
# ( teste da pesquisa com restricoes )
# -------------------------------------------------------------


digits = list(range(0,10))

domains = { D:digits for D in ['O','R','T','U','W'] }
domains['F']  = [0,1]
domains['X1'] = [0,1]
domains['X2'] = [0,1]


def all_different(Aux1):
    return len(set(Aux1)) == len(Aux1)

def orx1(Aux2):
    return 2*Aux2[0] == Aux2[1]+10*Aux2[2]

def wx1ux2(Aux3):
    return 2*Aux3[0]+Aux3[1] == Aux3[2]+10*Aux3[3]

def tx2of(Aux4):
    return 2*Aux4[0]+Aux4[1] == Aux4[2]+10*Aux4[3]

domains['FORTUW'] = generate_product_domain(['F','O','R','T','U','W'],domains)
domains['FORTUW'] = filter_domain(domains['FORTUW'],all_different)

domains['ORX1'] = generate_product_domain(['O','R','X1'],domains)
domains['ORX1'] = filter_domain(domains['ORX1'],orx1)

domains['WX1UX2'] = generate_product_domain(['W','X1','U','X2'],domains)
domains['WX1UX2'] = filter_domain(domains['WX1UX2'],wx1ux2)

domains['TX2OF'] = generate_product_domain(['T','X2','O','F'],domains)
domains['TX2OF'] = filter_domain(domains['TX2OF'],wx1ux2)


constraints = []

constraints += [ (edge,lambda var,val,auxvar,auxval : val==auxval[0]) 
    for edge in [('F','FORTUW'),('O','ORX1'),('W','WX1UX2'),('T','TX2OF')] ]
constraints += [ (edge,lambda auxvar,auxval,var,val : val==auxval[0]) 
    for edge in [('FORTUW','F'),('ORX1','O'),('WX1UX2','W'),('TX2OF','T')] ]

constraints += [ (edge,lambda var,val,auxvar,auxval : val==auxval[1]) 
    for edge in [('O','FORTUW'),('R','ORX1'),('X1','WX1UX2'),('X2','TX2OF')] ]
constraints += [ (edge,lambda auxvar,auxval,var,val : val==auxval[1]) 
    for edge in [('FORTUW','O'),('ORX1','R'),('WX1UX2','X1'),('TX2OF','X2')] ]

constraints += [ (edge,lambda var,val,auxvar,auxval : val==auxval[2]) 
    for edge in [('R','FORTUW'),('X1','ORX1'),('U','WX1UX2'),('O','TX2OF')] ]
constraints += [ (edge,lambda auxvar,auxval,var,val : val==auxval[2]) 
    for edge in [('FORTUW','R'),('ORX1','X1'),('WX1UX2','U'),('TX2OF','O')] ]

constraints += [ (edge,lambda var,val,auxvar,auxval : val==auxval[3]) 
    for edge in [('T','FORTUW'),('X2','WX1UX2'),('F','TX2OF')] ]
constraints += [ (edge,lambda auxvar,auxval,var,val : val==auxval[3]) 
    for edge in [('FORTUW','T'),('WX1UX2','X2'),('TX2OF','F')] ]

constraints += [ (edge,lambda var,val,auxvar,auxval : val==auxval[4]) 
    for edge in [('U','FORTUW')] ]
constraints += [ (edge,lambda auxvar,auxval,var,val : val==auxval[4]) 
    for edge in [('FORTUW','U')] ]

constraints += [ (edge,lambda var,val,auxvar,auxval : val==auxval[5]) 
    for edge in [('W','FORTUW')] ]
constraints += [ (edge,lambda auxvar,auxval,var,val : val==auxval[5]) 
    for edge in [('FORTUW','W')] ]


cs = MyCS(domains,dict(constraints))
t0 = time.clock()
lsols = cs.search_all()
t1 = time.clock()
print(t1-t0,"(above 1s: " +str(list(domains.keys())) +")" if t1-t0>1 else "")

