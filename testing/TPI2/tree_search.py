#encoding: utf8
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

# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
    def __init__(self, domain, initial, goal):
        self.domain = domain
        if type(initial) is list:
            self.initial = initial
        else:
            self.initial = [initial]

        if type(goal) is list:
            self.goal = goal
        else:
            self.goal = [goal]
    def goal_test(self, state):
        return state in self.goal

# Nos de uma arvore de pesquisa
class SearchNode:
    def __init__(self,state,parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth

    def __str__(self):
        return u"no({},{})".format(self.state, self.parent)

    def __repr__(self):
        return unicode(self)

# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='breadth'):
        self.problem = problem
        self.open_nodes = [ SearchNode(initial, None, 0) for initial in problem.initial ]
        self.strategy = strategy

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self,node):
        if node.parent == None:
            return [node.state]
        path = self.get_path(node.parent)
        path += [node.state]
        return(path)

    def search(self, limit=None):
        while self.open_nodes != []:
            node = self.open_nodes[0]
            if self.problem.goal_test(node.state):
                return self.get_path(node)

            self.open_nodes[0:1] = []
            if limit != None and node.depth >= limit:
                continue

            lnewnodes = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)
                lnewnodes += [ SearchNode(newstate, node,
			node.depth+1
			)]
            self.add_to_open([ newnode for newnode in lnewnodes
                if newnode.state not in self.get_path(node)])
        return None

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.open_nodes[0:0] = lnewnodes
        else:
            print "ERROR INVALID STRATEGY"
