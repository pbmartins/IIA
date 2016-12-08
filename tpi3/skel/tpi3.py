#encoding: utf8

from tree_search import *
from bayes_net import *
from constraintsearch import *
from pprint import pprint
from functools import reduce

class MyTree(SearchTree):
    """
    Acrescentar novos nós à fila
      - Os novos nós são acrescentados à fila de forma a
        que sejam visitados por ordem crescente da função 
        de avaliação, sem no entanto afectar o princípio
        da pesquisa em profundidade
    """
    def banbou_add_to_open(self,lnewnodes):
        self.open_nodes[:0] = sorted(lnewnodes, key=lambda n: n.arg3 + n.arg4)

    """
    Suportar a estratégia de pesquisa "banbou"
      - O processo vai encontrar várias soluções e só termina
        quando a fila estiver vazia
      - Mantém-se registo da melhor solução encontrada
      - Quando um nó visitado tem uma função de avaliação superior ao
        custo da melhor solução já encontrada, esse nó é descartado
      - Quando se encontra uma solução com custo inferior
        ao da melhor solução anteriormente encontrada, regista-se a
        nova solução
      - Atribui valores aos atributos self.solution_cost 
        e self.tree_size
    """
    def search2(self):
        self.tree_size = 1
        self.open_nodes[0].arg3 = 0
        self.open_nodes[0].arg4 = self.problem.domain.heuristic( \
                self.open_nodes[0].state, self.problem.goal)
        self.solution_cost = None
        best_path = None
        eval_func = lambda cost: self.solution_cost == None \
                or self.solution_cost > cost
        while self.open_nodes != []:
            node = self.open_nodes[0]
            self.open_nodes[:1] = []
            if self.strategy == 'banbou' and not eval_func(node.arg3 + node.arg4):
                continue
            if self.problem.goal_test(node.state):
                path = self.get_path(node)
                if eval_func(node.arg3):
                    self.solution_cost = node.arg3
                    best_path = path
                if self.strategy == 'banbou':
                    continue
                return path    
            actions = self.problem.domain.actions(node.state)
            lnewnodes = []
            for a in actions:
                newstate = self.problem.domain.result(node.state,a)
                newcost = node.arg3 + self.problem.domain.cost(node.state, a)
                heuristic = self.problem.domain.heuristic(newstate, self.problem.goal)
                if newstate not in self.get_path(node):
                    newnode = SearchNode(newstate,node, newcost, heuristic)
                    lnewnodes += [newnode]
            self.add_to_open(lnewnodes)
            self.tree_size += len(lnewnodes)
        return best_path if self.strategy == 'banbou' else None

class MyBN(BayesNet):
    """
    Calcula a cobertura de Markov para uma dada
    variavel, na forma de uma lista contendo as variáveis 
    mães, as variáveis filhas e as outras mães das filhas
    """
    def markov_blanket(self,var):
        dependencies = [(v, list(list(self.dependencies[v].keys())[0])) \
                for v in self.dependencies.keys() if v != var]
        sons = [v for v, dep in dependencies if var in [e[0] for e in dep]]
        all_mothers = [[list(s)[0] for s in list(self.dependencies[v].keys())[0] \
                if list(s)[0] != var] for v in sons + [var]]
        return list(set(reduce(lambda a, b: a + b, all_mothers, []) + sons))

class MyCS(ConstraintSearch):
    """
    Calcula todas as soluções para um problema
    de satisfação de restrições.
    Optimiza de forma a encontrar cada solução
    apenas uma vez.
    """
    def search_all(self,domains=None,xpto=[],i=0):
        if domains==None:
            domains = self.domains

        # se alguma variavel tiver lista de valores vazia, falha
        if any([lv==[] for lv in domains.values()]):
            return None

        # se nenhuma variavel tiver mais do que um valor possivel, sucesso
        if all([len(lv)==1 for lv in list(domains.values())]):
            solution = { v:lv[0] for (v,lv) in domains.items() }
            if not solution in xpto:
                xpto += [solution]
            return xpto
      
        # continuação da pesquisa
        for var in domains.keys():
            stop_flag = False
            if len(domains[var])>1:
                for val in domains[var]:
                    newdomains = dict(domains)
                    newdomains[var] = [val]
                    edges = [(v1,v2) for (v1,v2) in self.constraints if v2==var]
                    newdomains = self.constraint_propagation(newdomains,edges)
                    stop_flag = self.search_all(newdomains, xpto, i+1) == None
            if stop_flag:
                break
        return xpto


