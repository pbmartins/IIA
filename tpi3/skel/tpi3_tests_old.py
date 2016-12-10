#encoding: utf8

from tpi3 import *

import math
import time

# -------------------------------------------------------------
# Dominio de aplicacao para exercicios sobre pesquisa em arvore
# -------------------------------------------------------------

class Cidades(SearchDomain):
    def __init__(self,connections, coordinates):
        self.connections = connections
        self.coordinates = coordinates
    def actions(self,Cidade):
        actlist = []
        for (C1,C2,D) in self.connections:
            if (C1==Cidade):
                actlist += [(C1,C2)]
            elif (C2==Cidade):
               actlist += [(C2,C1)]
        return actlist 
    def result(self,state,action):
        (C1,C2) = action
        if C1==state:
            return C2
    def cost(self,state,action):
        (A,B) = action
        if A != state:
            return None
        for (P,Q,D) in self.connections:
            if (P==A and Q==B) or (P==B and Q==A):
                return D
        return None
    def heuristic(self,state,goal):
        (x1,y1) = self.coordinates[state]
        (x2,y2) = self.coordinates[goal]
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

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
                      ('Faro', 'Beja', 147),
                      ('Braga', 'Guimaraes', 25),
                      ('Porto', 'Guimaraes', 44),
                      ('Guarda', 'Covilha', 46),
                      ('Viseu', 'Covilha', 57),
                      ('Castelo Branco', 'Covilha', 62)
                     ],

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
                       'Faro': (120, -250),
                       'Guimaraes': ( 71, 300),
                       'Covilha': ( 130, 175)
                     } )


p = SearchProblem(cidades_portugal,'Braga','Faro')
print("-------------------------------------------")
t = MyTree(p,'depth')
print("Solution: {0}".format(t.search2()))
print(t.solution_cost,t.tree_size)
print("-------------------------------------------")
t = MyTree(p,'banbou')
print("Solution: {0}".format(t.search2()))
print(t.solution_cost,t.tree_size)
print("-------------------------------------------")

q = SearchProblem(cidades_portugal,'Guarda','Lisboa')
r = MyTree(q,'banbou')
print("Solution: {0}".format(r.search2()))
print(r.solution_cost,r.tree_size)
print("-------------------------------------------")


# -------------------------------------------------------------
# Rede de Bayes para testar o método markov_blanket()
# -------------------------------------------------------------

bn = MyBN()

bn.add('a',[],0.003)
bn.add('b_a',[],0.002)
bn.add('c_s',[('a',True )],0.48)
bn.add('c_s',[('a',False)],0.08)

bn.add('d',[],0.01)
bn.add('m_f',[],0.01)
bn.add('b_v',[('c_s',True ),('b_a',True )],0.18)
bn.add('b_v',[('c_s',True ),('b_a',False)],0.02)
bn.add('b_v',[('c_s',False),('b_a',True )],0.90)
bn.add('b_v',[('c_s',False),('b_a',False)],0.68)
bn.add('s_m',[],0.05)

bn.add('s_p',[],0.3)
bn.add('v_p',[('m_f',True),('d',True ),('b_v',True )],0.003)
bn.add('v_p',[('m_f',True),('d',True ),('b_v',False )],0.12)
bn.add('v_p',[('m_f',True),('d',False ),('b_v',True)],0.08)
bn.add('v_p',[('m_f',True),('d',False),('b_v',False )],0.01)
bn.add('v_p',[('m_f',False),('d',True),('b_v',True)],0.04)
bn.add('v_p',[('m_f',False),('d',True ),('b_v',False)],0.07)
bn.add('v_p',[('m_f',False),('d',False),('b_v',True )],0.13)
bn.add('v_p',[('m_f',False),('d',False),('b_v',False)],0.09)
bn.add('h',[('b_v',True )],0.44)
bn.add('h',[('b_v',False)],0.89)
bn.add('s_s',[('s_m',True),('m_f',True ),('b_v',True )],0.3)
bn.add('s_s',[('s_m',True),('m_f',True ),('b_v',False )],0.21)
bn.add('s_s',[('s_m',True),('m_f',False ),('b_v',True)],0.34)
bn.add('s_s',[('s_m',True),('m_f',False),('b_v',False )],0.12)
bn.add('s_s',[('s_m',False),('m_f',True),('b_v',True)],0.15)
bn.add('s_s',[('s_m',False),('m_f',True ),('b_v',False)],0.14)
bn.add('s_s',[('s_m',False),('m_f',False),('b_v',True )],0.132)
bn.add('s_s',[('s_m',False),('m_f',False),('b_v',False)],0.44)

bn.add('s_t',[('d',True )],0.08)
bn.add('s_t',[('d',False)],0.002)
bn.add('s_q',[('s_p',True ),('v_p',True )],0.008)
bn.add('s_q',[('s_p',True ),('v_p',False)],0.4)
bn.add('s_q',[('s_p',False),('v_p',True )],0.51)
bn.add('s_q',[('s_p',False),('v_p',False)],0.13)
bn.add('f_s',[],0.1)
bn.add('c_c',[('s_s',True )],0.49)
bn.add('c_c',[('s_s',False)],0.023)

bn.add('car_s',[('c_c',True),('s_t',True),('s_q',True ),('f_s',True )],0.091)
bn.add('car_s',[('c_c',True),('s_t',True),('s_q',True ),('f_s',False )],0.081)
bn.add('car_s',[('c_c',True),('s_t',True),('s_q',False ),('f_s',True )],0.045)
bn.add('car_s',[('c_c',True),('s_t',True),('s_q',False ),('f_s',False )],0.065)
bn.add('car_s',[('c_c',True),('s_t',False),('s_q',True ),('f_s',True)],0.087)
bn.add('car_s',[('c_c',True),('s_t',False),('s_q',True),('f_s',False )],0.043)
bn.add('car_s',[('c_c',True),('s_t',False),('s_q',False ),('f_s',True)],0.035)
bn.add('car_s',[('c_c',True),('s_t',False),('s_q',False),('f_s',False )],0.067)
bn.add('car_s',[('c_c',False),('s_t',True),('s_q',True),('f_s',True)],0.052)
bn.add('car_s',[('c_c',False),('s_t',True),('s_q',True),('f_s',False)],0.054)
bn.add('car_s',[('c_c',False),('s_t',True),('s_q',False),('f_s',True)],0.056)
bn.add('car_s',[('c_c',False),('s_t',True),('s_q',False),('f_s',False)],0.078)
bn.add('car_s',[('c_c',False),('s_t',False),('s_q',True),('f_s',True )],0.045)
bn.add('car_s',[('c_c',False),('s_t',False),('s_q',True),('f_s',False)],0.031)
bn.add('car_s',[('c_c',False),('s_t',False),('s_q',False),('f_s',True )],0.034)
bn.add('car_s',[('c_c',False),('s_t',False),('s_q',False),('f_s',False)],0.023)

print("-------------------------------------------")
print("Cobertura de Markov para 's_t'")
print(bn.markov_blanket('s_t'))
print("-------------------------------------------")
print("Cobertura de Markov para 'c_s'")
print(bn.markov_blanket('c_s'))
print("-------------------------------------------")
print("Cobertura de Markov para 's_s'")
print(bn.markov_blanket('s_s'))
print("-------------------------------------------")
print("Cobertura de Markov para 'b_v'")
print(bn.markov_blanket('b_v'))
print("-------------------------------------------")
print("Cobertura de Markov para 's_q'")
print(bn.markov_blanket('s_q'))
print("-------------------------------------------")
print("Cobertura de Markov para 'f_s'")
print(bn.markov_blanket('f_s'))
print("-------------------------------------------")
print("Cobertura de Markov para 'car_s'")
print(bn.markov_blanket('car_s'))
print("-------------------------------------------")

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
domains['TX2OF'] = filter_domain(domains['TX2OF'],tx2of)

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

print("-------------------------------------------")
print("Procura de uma solução")
print("-------------------------------------------")
t0 = time.clock()
sol = cs.search() 

print("Solucao:",sol)

print("Tempo:",time.clock()-t0)


print("-------------------------------------------")
print("Procura de todas as soluções")
print("-------------------------------------------")
t0 = time.clock()
lsols = cs.search_all()

print("Soluções:")
for s in lsols:
    print([(v,s[v]) for v in ['F','O','R','T','U','W']])

print("Tempo:",time.clock()-t0)

print(len(lsols)," soluções")
