
from constraintsearch import *


def nao_ataca(var1,var2,col1,col2):
    if col1==col2:
        return False
    linha = { "r1":1, "r2":2, "r3":3, "r4":4 }
    lin1 = linha[var1] 
    lin2 = linha[var2] 
    return abs(lin1-lin2)!=abs(col1-col2)

s = ConstraintSearch( [ ("r1",[1,2,3,4]),
                        ("r2",[1,2,3,4]),
                        ("r3",[1,2,3,4]),
                        ("r4",[1,2,3,4]) ],

                      [ ("r1","r2",nao_ataca),
                        ("r1","r3",nao_ataca),
                        ("r1","r4",nao_ataca),
                        ("r2","r3",nao_ataca),
                        ("r2","r4",nao_ataca),
                        ("r3","r4",nao_ataca),
                        ("r2","r1",nao_ataca),
                        ("r3","r1",nao_ataca),
                        ("r4","r1",nao_ataca),
                        ("r3","r2",nao_ataca),
                        ("r4","r2",nao_ataca),
                        ("r4","r3",nao_ataca) ] )



