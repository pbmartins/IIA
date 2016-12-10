#encoding: utf8
# Pedro Martins, 76551

from tree_search import *
from bayes_net import *
from constraintsearch import *
from pprint import pprint

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
        # Initialize root values
        self.tree_size = 1
        self.open_nodes[0].arg3 = 0
        self.open_nodes[0].arg4 = self.problem.domain.heuristic( \
                self.open_nodes[0].state, self.problem.goal)
        self.solution_cost = None
        best_path = None
        # Evalution function to check if new cost is less then the actual solution's cost
        eval_func = lambda cost: self.solution_cost == None \
                or self.solution_cost > cost

        while self.open_nodes != []:
            node = self.open_nodes[0]
            self.open_nodes[:1] = []
            if self.strategy == 'banbou' and not eval_func(node.arg3 + node.arg4):
                continue
            if self.problem.goal_test(node.state):
                path = self.get_path(node)
                # Check if the new solution is better than the current one
                # If there is no solution, update the values anyways
                if eval_func(node.arg3):
                    self.solution_cost = node.arg3
                    best_path = path
                #if self.strategy != 'banbou':
                #    return path
                # If strategy is 'banbou' iterate until open_nodes is empty 
                # finding the optimal solution
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
        # If the strategy if 'banbou' return the best path
        # For other strategies, it means it didn't find a solution
        # (best_path may be None too if there no solutions using 'banbou'
        return best_path if self.strategy == 'banbou' else None

class MyBN(BayesNet):
    """
    Calcula a cobertura de Markov para uma dada
    variavel, na forma de uma lista contendo as variáveis 
    mães, as variáveis filhas e as outras mães das filhas
    """
    def markov_blanket(self,var):
        # Construct dict of all var: mothers
        all_mothers = {v: [m[0] for m in list(list(self.dependencies[v].keys())[0])] \
                for v in self.dependencies.keys()}
        # Get sons of var by checking if var belongs to their mothers domain
        sons = [v for v, mothers in all_mothers.items() if var in mothers]
        # Get all sons mothers except var
        sons_mothers = [v for v in sum([all_mothers[son] for son in sons], []) \
                if v != var]
        # Return unique values of the sum of sons, sons' mothers and mothers of var
        return list(set(sons + sons_mothers + all_mothers[var]))

class MyCS(ConstraintSearch):
    """
    Calcula todas as soluções para um problema
    de satisfação de restrições.
    Optimiza de forma a encontrar cada solução
    apenas uma vez.
    """
    def search_all(self,domains=None,xpto=[],all_vars=None):
        if domains==None:
            domains = self.domains

        # If any of the vars has an empty values list, then this is not a solution
        if any([lv==[] for lv in domains.values()]):
            return None

        # If all vars have only one possible value, then append this solution to the list
        if all([len(lv)==1 for lv in list(domains.values())]):
            solution = { v:lv[0] for (v,lv) in domains.items() }
            xpto += [solution] if not solution in xpto else []
            return None
      
        # Create list of all domain vars and remove them if the size of their
        # domain is less than 2
        all_vars = list(domains.keys()) if all_vars == None else all_vars
        var = all_vars[0]
        while len(domains[var]) < 2:
            all_vars = all_vars[1:]
            var = all_vars[0]
        # Each solution will contain a value of a var
        # Iterate over the selected var domain (possible values) and call
        # recursivly search_all() for the next var and a selected var value
        # and the constraints it'll produce in the rest of the vars' domains
        for val in domains[var]:
            newdomains = dict(domains)
            newdomains[var] = [val]
            edges = [(v1,v2) for (v1,v2) in self.constraints if v2==var]
            newdomains = self.constraint_propagation(newdomains,edges)
            self.search_all(newdomains, xpto, all_vars[1:])

        return xpto
