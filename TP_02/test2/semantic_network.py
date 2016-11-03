

# Redes semanticas
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2013
# v0.5 - 2013/10/21
#

# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#
class Relation:
    def __str__(self):
        return str(self.relation)+"("+ \
               str(self.entity1)+","+  \
               str(self.entity2)+")"
    def __repr__(self):
        return str(self)
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        self.entity1 = e1
        self.relation = assoc
        self.entity2 = e2

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,type1,type2):
        self.entity1 = type1
        self.relation = 'subtype'
        self.entity2 = type2

#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        self.entity1 = obj
        self.relation = 'member'
        self.entity2 = type

#   Exemplo:
#   m = Member('socrates','homem')

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self):
        self.declarations = []
    def __str__(self):
        return my_list2string(self.declarations)
    def insert(self,decl):
        self.declarations.append(decl)
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d \
                   for d in self.declarations \
                   if  (user == None or d.user==user) \
                   and (e1 == None or d.relation.entity1 == e1) \
                   and (rel == None or d.relation.relation == rel) \
                   and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))


# Funcao auxiliar para converter para cadeias de caracteres
# listas cujos elementos sejam convertiveis para
# cadeias de caracteres
def my_list2string(list):
   if list == []:
       return "[]"
   s = "[ " + str(list[0])
   for i in range(1,len(list)):
       s += ", " + str(list[i])
   return s + " ]"
    

