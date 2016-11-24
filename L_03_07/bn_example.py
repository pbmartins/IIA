
from bayes_net import *

# Exemplo dos acetatos:

bn = BayesNet()

bn.add('r',[],0.001)
bn.add('t',[],0.002)

bn.add('a',[('r',True ),('t',True )],0.950)
bn.add('a',[('r',True ),('t',False)],0.940)
bn.add('a',[('r',False),('t',True )],0.290)
bn.add('a',[('r',False),('t',False)],0.001)

bn.add('j',[('a',True )],0.900)
bn.add('j',[('a',False)],0.050)

bn.add('m',[('a',True )],0.700)
bn.add('m',[('a',False)],0.100)

conjunction = [('j',True),('m',True),('a',True),('r',False),('t',False)]

print(bn.jointProb(conjunction))
print(bn.indProb('a', True))
print(bn.indProb('a', False))

# Exemplo exercicio
# a - precisa de ajuda
# s - sobre-carregado
# c - cara preocupada
# e - email não lido
# p - processador de texto
# r - util rato

#bn = BayesNet()

#bn.add('s',[],0.600)
#bn.add('p',[],0.050)

#bn.add('a',[('p',True )],0.250)
#bn.add('a',[('p',False)],0.004)

#bn.add('r',[('p',True )],0.100)
#bn.add('r',[('p',False)],0.004)

#bn.add('c',[('s',True ),('a',True )],0.020)
#bn.add('c',[('s',True ),('a',False)],0.010)
#bn.add('c',[('s',False),('a',True )],0.011)
#bn.add('c',[('s',False),('a',False)],0.001)

#bn.add('e',[('s',True )],0.900)
#bn.add('e',[('s',False)],0.001)

