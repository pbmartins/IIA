
# Pesquisa para resolucao de problemas de atribuicao
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2014
# v1.0 - 2014/11/27
#

class ConstraintSearch:

    # varvals e' uma lista de pares (var,lvals), em que lvals
    # e' a lista de todos os valores possiveis de var
    def __init__(self,varvals,constraints):
        self.varvals = varvals
        self.constraints = constraints
        self.iterations = 0

    # varvals e' a lista actual de valores possiveis 
    # de todas as variaveis
    # ( ver acetato "Pesquisa com propagacao de restricoes
    #   em problemas de atribuicao - algoritmo" )

    def search(self,varvals=None):

        if varvals == None:
            varvals = self.varvals

        self.iterations += 1

        # se alguma variavel tiver lista de valores vazia, falha
        if [v for (v,lv) in varvals if lv==[]] != []:
            return None
        
        # se nenhuma variavel tiver mais do que um valor possivel, sucesso
        if [v for (v,lv) in varvals if lv[1:]!=[]] == []:
            # se valores violam restricoes, falha
            # ( verificacao desnecessaria se for feita a propagacao
            #   de restricoes )
            for (var1,var2,constraint) in self.constraints:
                val1 = [lv[0] for (v,lv) in varvals if v==var1][0]
                val2 = [lv[0] for (v,lv) in varvals if v==var2][0]
                if not constraint(var1,var2,val1,val2):
                    return None 
            return [ (var,vals[0]) for (var,vals) in varvals ]

        # opcoes para a proxima iteracao
        options = [ (var,val) \
                        for (var,lvals) in varvals if len(lvals)>1 \
                        for val in lvals ]
        for (var,val) in options:
            newvarvals = []
            for (v,lv) in varvals:
                if v==var:
                    newvarvals += [(v,[val])]
                else:
                    newvarvals += [(v,lv)]

            # falta fazer a propagacao de restricoes
            # ............

            # chamada recursiva
            rec = self.search(newvarvals)
            if rec==None:
                continue
            # se encontrou solucao, retorna
            return rec
        return None


