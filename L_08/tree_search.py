
# Modulo: tree_search
# 
# Fornece um conjunto de classes para suporte a resolucao de 
# problemas por pesquisa em arvore:
#    SearchDomain  - dominios de problemas
#    SearchProblem - problemas concretos a resolver 
#    SearchNode    - nos da arvore de pesquisa
#    SearchTree    - arvore de pesquisa, com metodos para 
#                    a respectiva construcao
#
#  (c) Luis Seabra Lopes, Introducao a Inteligencia Artificial, 2012-2014

from heapq import merge

# Dominios de pesquisa
# Permitem calcular
# as accoes possiveis em cada estado, etc
class SearchDomain:
    # construtor
    def __init__(self):
        abstract
    # lista de accoes possiveis num estado
    def actions(self, state):
        abstract
    # resultado de uma accao num estado, ou seja, o estado seguinte
    def result(self, state, action):
        abstract
    # custo de uma accao num estado
    def cost(self, state, action):
        abstract
    # custo estimado de chegar de um estado a outro
    def heuristic(self, state, goal_state):
        abstract

# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
    def __init__(self, domain, initial, goal):
        self.domain = domain
        self.initial = initial
        self.goal = goal
    def goal_test(self, state):
        return state == self.goal

# Nos de uma arvore de pesquisa
class SearchNode:
    def __init__(self,state,parent, cost=0, depth=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.depth = depth
        self.heuristic = heuristic
    def __str__(self):
        return "no({state}, {parent}, {cost}, {depth})".format(state=self.state, \
                parent=self.parent, cost=self.cost, depth=self.depth)
    def __repr__(self):
        return str(self)

    # Check if state is in node's parents
    def in_parent(self, state):
        if self.parent == None:
            return False
        if self.parent.state == state:
            return True
        return self.parent.in_parent(state)

# Arvores de pesquisa
class SearchTree:
    # construtor
    def __init__(self,problem, strategy='breadth', boundary=7): 
        self.problem = problem
        root = SearchNode(problem.initial, None, 0, 0)
        self.open_nodes = [root]
        self.strategy = strategy
        self.boundary = boundary

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self,node):
        if node.parent == None:
            return [node.state]
        path = self.get_path(node.parent)
        path += [node.state]
        return(path)

    # procurar a solucao
    def search(self):
        while self.open_nodes != []:
            node = self.open_nodes[0]
            if self.problem.goal_test(node.state):
                self.depth = node.depth
                self.cost = node.cost
                return (self.get_path(node), self.cost, self.depth)
            self.open_nodes[0:1] = []
            lnewnodes = []
            if self.strategy != 'depth' or node.depth < self.boundary:
                for a in self.problem.domain.actions(node.state):
                    newstate = self.problem.domain.result(node.state, a)
                    if not node.in_parent(newstate):
                        newcost = self.problem.domain.cost(newstate, a) + node.cost
                        heuristic = self.problem.domain.heuristic(newstate, self.problem.goal)
                        lnewnodes += [SearchNode(newstate, node, newcost, \
                                node.depth + 1, heuristic)]
                self.add_to_open(lnewnodes)
        return None

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self, lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.open_nodes[0:0] = lnewnodes
        elif self.strategy == 'uniform':
            lnewnodes.sort(key=lambda n: n.cost)
            self.open_nodes = list(merge(self.open_nodes, lnewnodes, key=lambda n: n.cost))
        elif self.strategy == 'greedy':
            lnewnodes.sort(key=lambda n: n.heuristic)
            self.open_nodes = list(merge(self.open_nodes, lnewnodes, key=lambda n: n.heuristic))
