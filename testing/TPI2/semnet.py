#encoding: utf8

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2015
# v1.7 - 2015/10/13
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

class Relation:
    def __init__(self,e1,name,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = name
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,name,e2,cardin=None,default=None):
        Relation.__init__(self,e1,name,e2)
        self.cardin = cardin
        self.default = default
    def __str__(self):
        if self.cardin==None:
            default=""
        elif self.default==None:
            default = "[=?]"
        else:
            default = "[=" + str(self.default) + "]"
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + default + ")"

#   Exemplos:
#   a = Association('socrates','professor','filosofia')
#   b = Association('mamifero','altura','number','one',1.2)
#   c = Association('mamifero','amigo','mamifero','many')

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

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
        return "decl("+str(self.user)+", "+str(self.relation)+")"
    def __repr__(self):
        return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=[]):
        self.declarations = ldecl
    def __str__(self):
        return my_list2string(self.declarations)
    def insert(self,decl):
        self.declarations.append(decl)
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))

    # Seguem-se funcoes para acrescentar novas relações,
    # fazendo as verificações prévias que forem necessárias.
    # Precisariam, para serem completadas, das funcoes que 
    # vai fazer.

    def add_member(self,user,obj,type):
        """
        if self.type_exists(user,obj) or self.object_exists(user,type):
            return False
        """
        self.insert(Declaration(user,Member(obj,type)))
        return True

    def add_subtype(self,user,subt,supert):
        """
        if self.object_exists(user,subt) or self.object_exists(user,supert):
            return False
        """
        self.insert(Declaration(user,Subtype(subt,supert)))
        return True

    def add_association(self,user,e1,assoc,e2,cardin=None,default=None):  # new

        if cardin=='many' and default != None:
            return False

        """
        if (self.object_exists(user,e1) and self.type_exists(user,e2)) \
              or  (self.type_exists(user,e1) and self.object_exists(user,e2)):
            return False

        at = self.infer_assoc_type(user,assoc)
        if at!=None:
            (t1,t2) = at
            pass
        """
        self.insert(Declaration(user,Association(e1,assoc,e2,cardin,default)))
        return True


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
    

