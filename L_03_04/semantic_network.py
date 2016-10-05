

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
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = rel
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

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
        return "decl("+str(self.user)+","+str(self.relation)+")"
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
    def query_local(self,user=None,e1=None,rel=None,relc=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (relc == None or isinstance(d.relation, relc))
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))

    def predecessor(self, e1, e2):
        ancestors = [d.relation.entity2 for d in self.query_local(e1=e2, rel='member') \
                + self.query_local(e1=e2, rel='subtype')]
        #ancestors = [d.relation.entity2 for d in self.query_local(e1=e2, rel=(Member, Subtype))]
        return True if e1 in ancestors \
                else any([self.predecessor(e1=e1, e2=d) for d in ancestors])

    def predecessor_path(self, e1, e2):
        ancestors = [d.relation.entity2 for d in self.query_local(e1=e2, rel='member') \
                + self.query_local(e1=e2, rel='subtype')]
        if e1 in ancestors:
            return [e2, e1]
        elif ancestors == []:
            return None
        predecessors = [self.predecessor_path(e1=e1, e2=d) for d in ancestors]
        to_rtn = [[e2] + p for p in predecessors if p != None]
        return None if to_rtn == [] else to_rtn[0]

    def association_names(self):
        #return list(set([d.relation.name for d in self.declarations \
                #if not (d.relation.name == 'subtype' or d.relation.name == 'member')]))
        return list(set([d.relation.name for d in self.query_local(relc=Association)]))

    def members(self):
        return list(set([d.relation.entity1 for d in self.query_local(rel='member')]))

    def users(self):
        return list(set([d.user for d in self.declarations]))

    def types(self):
        return list(set([d.relation.entity2 for d \
                in self.query_local(rel='member') + self.query_local(rel='subtype')]))

    def associations(self):
        return list(set([d.relation.name for d in self.query_local(relc=Association) \
                if not (d.relation == 'member' or d.relation == 'subtype')]))

    def user_relations(self, user):
        return None if user == None \
                else list(set([d.relation.name for d in self.declarations]))

    def n_user_associations(self, user):
        return None if user == None \
                else len(set([d.relation.name for d in self.query_local(relc=Association)]))

    def entity_associations(self, entity):
        return None if entity == None else list(set([(d.relation.name, d.user) \
                for d in self.query_local(relc=Association, e1=entity) \
                + self.query_local(relc=Association, e2=entity)]))

    def query(self, entity, assoc=None):
        if entity == None:
            return None
        ancestors = [d.relation.entity2 \
                for d in self.query_local(e1=entity, relc=(Member, Subtype))]
        self.query_result = self.query_local(e1=entity, relc=Association) \
                if assoc == None else self.query_local(e1=entity, rel=assoc)
        for a in ancestors:
            self.query_result += self.query(a, assoc)
        return self.query_result

    def query2(self, entity, assoc=None):
        if entity == None:
            return None
        ancestors = self.query_local(e1=entity, relc=(Member, Subtype))
        self.query_result = self.query_local(e1=entity, relc=Association) \
                if assoc == None else self.query_local(e1=entity, rel=assoc)
        for a in ancestors:
            self.query_result += [a] + self.query2(a.relation.entity2, assoc)
        return self.query_result

    def query_cancel(self, entity, assoc=None):
        if entity == None:
            return None
        ancestors = [d.relation.entity2 \
                for d in self.query_local(e1=entity, relc=(Member, Subtype))]
        qr = self.query_local(e1=entity, relc=Association) \
                if assoc == None else self.query_local(e1=entity, rel=assoc)
        query_assocs = [d.relation.name for d in qr]
        to_rtn = []
        to_rtn[0:] = qr
        for a in ancestors:
            pred_assocs = self.query_cancel(a, assoc)
            for d in pred_assocs:
                if d.relation.name not in query_assocs:
                    to_rtn += [d]
        self.query_result = to_rtn
        return self.query_result

    def query_assoc_value(self, entity, assoc, head=True):
        if entity == None or assoc == None:
            return None
        qr = self.query_local(e1=entity, rel=assoc)
        if all([d.relation.entity2 == qr[0].relation.entity2 for d in qr]):
            return qr[0].relation.entity2

        ancestors = [d.relation.entity2 \
                for d in self.query_local(e1=entity, relc=(Member, Subtype))]
        qr_ancestors = [query_assoc_value(a, assoc, False) \
                for a in ancestors]

        elems = list(set([d.relation.entity2 for d in qr]))
        count = [len([e for e in qr if e.relation.entity2 == d]) for d in elems]
        max_rep = count[max(count, key = lambda i: count[i])]

        if not head:
            if ancestors == []:
                return (max_rep, len(qr))

        # not working


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
    
