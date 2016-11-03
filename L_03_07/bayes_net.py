

# Guiao de representacao do conhecimento
# -- Redes de Bayes
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2014
# v1.0 - 2014/11/04
#
#

from functools import reduce

class ProbCond:

    def __init__(self,var,mothers,prob):
        self.var = var
        self.mothers = mothers
        self.prob = prob
    def __str__(self):
        return "pc(" + self.var + "," + str(self.mothers) + \
               "," + str(self.prob) + ")"
    def __repr__(self):
        return str(self)


#   Exemplo:
#      ProbCond("a", [ ("r",True),  ("t",True)  ], 0.95) )
#      Ou seja: a probabilidade condicionada de "alarme" dado que 
#      ocorreu "roubo" e "terramoto" e 95%

# ------------------------------------------------------------

class BayesNet:

#   construtor:
#   ( por defeito, inicializa rede com lista vazia )
#
    def __init__(self,prob_list=[]):
        self.prob_list = prob_list

#   insere uma probabilidade condicionada na rede:
#
    def insert(self,pc):
        self.prob_list.append(pc)

#   calcula a probabilidade conjunta, dados os valores de todas
#   as variaveis da rede;
#   recebe uma lista de pares (var,val):
#
    def joint_prob(self,conjunction):
        prob = 1.0
        for (var,val) in conjunction:
            contido = lambda c1,c2: ([e for e in c1 if e not in c2]==[])
            listprob = [ pc.prob \
                           for pc in self.prob_list \
                           if pc.var == var \
                           and contido(pc.mothers,conjunction) ]
            if val:
                prob *= listprob[0]
            else:
                prob *= 1.0-listprob[0]
        return prob

    def ind_prob(self, var):
       return reduce([], 0)
