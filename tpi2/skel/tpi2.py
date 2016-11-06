#encoding: utf8
# Author: Pedro Martins - 76551

from tree_search import *
from semnet import *
from functools import reduce
from itertools import groupby

class MySemNet(SemanticNetwork):
    def __init__(self,ldecl=[]):
        SemanticNetwork.__init__(self,ldecl)

        # Current declaration variable for insert2
        self.current_decl = None

        # lambda helpers
        # self.rel_equals : check if two relations are the same
        # self.is_in : check if a relation is in a list of relations
        # self.conc_list : concatenate two lists
        # self.get_freq : get relative frequence of types on a list (some types may be sublists of types)
        # self.get_subfreq : get relative frequence of sublists of types
        # self.assoc_name : get name of association from tuple
        # self.group : group relative frequences of the same type
        # example: 
        # self.group([('mamifero', 0.25), ('homem', 0.25), ('filosofo', 0.25), ('homem', 0.25)]) = \
        #        [('mamifero', 0.25), ('homem', 0.5), ('filosofo', 0.25)]
        # self.decl_equals : check if two declarations are the same
        self.rel_equals = lambda rel1, rel2: rel1.__dict__ == rel2.__dict__
        self.is_in = lambda obj, lst: len([o for o in lst if self.rel_equals(obj, o)]) > 0
        self.conc_list = lambda a, b: a + b
        self.get_freq = lambda elem, lst: \
                round(len([e for e in lst if e == elem]) / len(lst), 2)
        self.get_subfreq = lambda lst: reduce(self.conc_list, \
                [[(e[0], e[1] * elem[1]) for e in elem[0]] if isinstance(elem[0], list) \
                else [elem] for elem in lst], [])
        self.assoc_name = lambda elem: elem[0]
        self.group = lambda lst: [(assoc, sum(f[1] for f in freqs)) for assoc, freqs \
                in groupby(sorted(lst, key=self.assoc_name), self.assoc_name)]
        self.decl_equals = lambda decl1, decl2: not (decl1 == None or decl2 == None) \
                and decl1.user == decl2.user and self.rel_equals(decl1.relation, decl2.relation)

        
    # Devolve lista de todos os objectos existentes na rede
    def getObjects(self):
        member_objs = [d.relation.entity1 for d in self.query_local(rel='member')]
        all_assocs = [d.relation for d in self.query_local() if isinstance(d.relation, Association)]
        assoc_objs = reduce(self.conc_list, [[a.entity1, a.entity2] \
                for a in all_assocs if a.cardin == None], [])
        assoc_type_objs = [a.default for a in all_assocs \
                if a.cardin != None and a.default != None]
        return list(set(member_objs + assoc_objs + assoc_type_objs))


    # Devolve, para o nome de associação dado, uma lista de tuplos 
    # (t1,t2,freq), em que:
    #   t1 - tipo da primeira entidade da associação
    #   t2 - tipo da segunda entidade da associação
    #   freq - frequência relativa com que ocorre
    def getAssocTypes(self,assocname):
        assoc_types = [d.relation for d in self.query_local(rel=assocname) \
                if d.relation.cardin != None]
        assoc_set = [(assoc, len([a for a in assoc_types if self.rel_equals(a, assoc)])) \
                for assoc in self.createSet(assoc_types)]
        return [(assoc[0].entity1, assoc[0].entity2, assoc[1] / len(assoc_types)) \
                for assoc in assoc_set]

    # Create set of relations
    def createSet(self, lst):
        rtn = []
        [rtn.append(rel) for rel in lst if not self.is_in(rel, rtn)]
        return rtn


    # Devolve uma lista de tuplos (t,freq) para o objecto dado, 
    # em que:
    #    t - tipo do objecto
    #    freq - frequência com que ocorre
    def getObjectTypes(self,obj):
        obj_decl_1 = self.query_local(e1=obj)
        obj_decl_2 = self.query_local(e2=obj)
        default_types = [d.relation.entity2 for d in self.query_local() \
                if isinstance(d.relation, Association) and d.relation.default == obj]

        # Relations obtained by members
        member_assocs = [d.relation for d in obj_decl_1 if d.relation.name == 'member']
        # Types of member associations
        member_types = [a.entity2 for a in member_assocs]
        
        # Associations obtained between objects
        obj_assocs = [(d.relation, 0) for d in obj_decl_1 if isinstance(d.relation, Association)] \
                + [(d.relation, 1) for d in obj_decl_2 if isinstance(d.relation, Association)] \
        # Types of object associations (will create a tuple of (type, inside_rel_freq)
        get_types = lambda assoc, idx: [(t[idx], t[2]) \
                for t in self.getAssocTypes(assoc.name)]
        obj_types = [t for t in [get_types(a, idx) \
                for (a, idx) in obj_assocs] if t != []]

        # Concatenate all types into a single list
        types_list = member_types + obj_types + default_types
        # Return list of association types and each relative frequence
        return [] if types_list == [] else \
                self.group(self.get_subfreq([(at, self.get_freq(at, types_list)) \
                for at in self.createSetWSublists(types_list)]))


    # Create a set of elements of a list that may contain sublists
    def createSetWSublists(self, lst):
        rtn = []
        [rtn.append(rel) for rel in lst if not (isinstance(rel, list) and rel in rtn)]
        return rtn

    # Insere uma nova relação "rel" declarada por "user".
    # Se a relação for uma associação fluente entre objectos,
    # tem que fazer a gestão do intervalo de tempo
    # em que a associação se mantém verdadeira
    def insert2(self,user,rel):
        self.tick += len(rel.name)   # simula a passagem do tempo

        # If it's a association between types, add imediatly
        if isinstance(rel, Association) and rel.cardin != None and rel.fluent:
            self.declarations.append(Declaration(user, rel))
        # If type does not exist, return None
        types = [d.relation for d in self.query_local(rel=rel.name) \
                if d.relation.cardin != None and d.relation.fluent]
        if len(types) == 1:
            decl = None
            # Get current declaration from semnet
            cd = [d for d in self.query_local(user=user, rel=rel.name, e2=rel.entity2)]
            # Compare it with the one saved localy
            if cd != [] and self.decl_equals(self.current_decl, cd[0]):
                decl = cd[0]
                self.declarations.pop(self.declarations.index(decl))
                decl.relation.time = (decl.relation.time[0], self.tick)
            else:
                # Add new declaration and save it localy if it's different from the current one
                rel.time = (self.tick, self.tick)
                self.current_decl = decl = Declaration(user, rel)
            self.declarations.append(decl)

    
class MyTree(SearchTree):
    def __init__(self, problem, strategy='depth'):
        SearchTree.__init__(self, problem, strategy)

    # optimizar e devolver uma solucao previamente 
    # guardada em self.solution
    def optimize(self):
        self.optimizations = []
        self.optimized = self.solution
        if len(self.solution) > 2:
            idx_c1 = 0
            idx_c2 = 2
            while len(self.optimized) > 1 and idx_c1 < len(self.optimized) - 2:
                c1 = self.optimized[idx_c1]
                c2 = self.optimized[idx_c2]
                if self.problem.domain.cost(c1, (c1, c2)) != None:
                    self.optimized[idx_c1+1:idx_c2] = []
                    self.optimizations += [(c1, c2)]
                elif idx_c2 < len(self.optimized) - 1:
                    idx_c2 += 1
                else:
                    idx_c1 += 1
                    idx_c2 = idx_c1 + 2
        return self.optimized


