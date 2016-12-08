
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

print("SOF13")

bn2 = BayesNet()

bn2.add('s', [], 0.6)
bn2.add('p', [], 0.05)

bn2.add('c', [('s', True ), ('a', False)], 0.010)
bn2.add('c', [('s', True ), ('a', True )], 0.020)
bn2.add('c', [('s', False), ('a', False)], 0.001)
bn2.add('c', [('s', False), ('a', True )], 0.011)


bn2.add('e', [('s', False)], 0.001)
bn2.add('e', [('s', True )], 0.900)


bn2.add('a', [('p', True )], 0.250)
bn2.add('a', [('p', False)], 0.004)


bn2.add('r', [('p', False), ('a', True )], 0.100)
bn2.add('r', [('p', False), ('a', False)], 0.010)
bn2.add('r', [('p', False)], 0.900)

print(bn2.indvProb('a', True))
