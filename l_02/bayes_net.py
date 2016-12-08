from itertools import product
from functools import reduce

class BayesNet:

    def __init__(self,ldep={}):
        self.dependencies = ldep

    # Os dados estao num dicionario (var,dependencies)
    # em que as dependencias de cada variavel
    # estao num dicionario (mothers,prob);
    # "mothers" e' um frozenset de pares (mothervar,boolvalue)
    def add(self,var,mothers,prob):
        self.dependencies.setdefault(var,{})[frozenset(mothers)] = prob

    # Probabilidade conjunta de uma dada conjuncao 
    # de valores das variaveis da rede
    def jointProb(self,conjunction):
        prob = 1.0
        for (var,val) in conjunction:
            for (mothers,p) in self.dependencies[var].items():
                if mothers.issubset(conjunction):
                    prob*=(p if val else 1-p)
        return prob

    # Three different implementations of the same problem
    def indvProb(self, var, boolean):
        all_vars = [key for key in self.dependencies.keys() if key != var]
        return sum([self.jointProb(list(zip(all_vars, comb)) + [(var, boolean)]) \
                for comb in itertools.product([True, False], repeat=len(all_vars))])

    def indProb(self, var, val):
        all_vars = [v for v in self.dependencies if v != var]
        conj_probs = [[(v, True), (v, False)] for v in all_vars] + [[(var, val)]]
        probs = [list(c) for c in list(product(*conj_probs))]
        return reduce(lambda a, b: a + b, [self.jointProb(p) for p in probs], 0)


    def individualProb(self, var):
        v, b = var
        s = 0
        all_vars = [vv for vv in self.dependencies.keys() if v != vv]
        conj_b = product([True, False], repeat=len(all_vars))
        for c in conj_b:
            s += self.jointProb(list(zip(all_vars, c)) + [var])
        return s
