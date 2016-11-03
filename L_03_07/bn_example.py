
from bayes_net import *


# Exemplo:
# ( ver acetatos das aulas teorico-praticas )
#
z = BayesNet()
z.insert( ProbCond("r", [], 0.001))
z.insert( ProbCond("t", [], 0.002))
z.insert( ProbCond("a", [ ("r",True),  ("t",True)  ], 0.95) )
z.insert( ProbCond("a", [ ("r",True),  ("t",False) ], 0.94) )
z.insert( ProbCond("a", [ ("r",False), ("t",True)  ], 0.29) )
z.insert( ProbCond("a", [ ("r",False), ("t",False) ], 0.001))
z.insert( ProbCond("j", [ ("a",True) ], 0.9))
z.insert( ProbCond("j", [ ("a",False) ], 0.05))
z.insert( ProbCond("m", [ ("a",True) ], 0.7))
z.insert( ProbCond("m", [ ("a",False) ], 0.1))

print(z.prob_list)

#       p(j & m & a & ~t & ~r)
#       Em Python:
#           joint_prob([ ("j",True ), ("m", True ), ("a",True), 
#                          ("t",False), ("r", False)              ] )
#

print(z.joint_prob( [ ("j",True ), ("m", True ), ("a",True), \
                      ("t",False), ("r", False)              ] ))
#   Exemplo:
