#encoding: utf8

import sys
import json
from tree_search import *
from semnet import *

class MySemNet(SemanticNetwork):
    def __init__(self,ldecl=[]):
        SemanticNetwork.__init__(self,ldecl)

    # verifica se "obj" existe nas declaracoes de "user"
    def object_exists(self,user,obj):
        members = self.query_local(user=user, e1=obj, rel='member')
        assocs = [d for d in self.query_local(user=user, e2=obj) \
                if not (d.relation.name == 'member' or d.relation.name == 'subtype') \
                and d.relation.cardin == None]
        return len(members + assocs) > 0

    # verifica se "type" existe nas declaracoes de "user"
    def type_exists(self,user,ttype):
        members = self.query_local(user=user, e2=ttype, rel='member')
        subtypes = self.query_local(user=user, e1=ttype, rel='subtype') + \
                self.query_local(user=user, e2=ttype, rel='subtype')
        assocs = [d for d in self.query_local(user=user, e2=ttype) \
                if not (d.relation.name == 'member' or d.relation.name == 'subtype') \
                and d.relation.cardin != None]
        return len(members + subtypes + assocs) > 0

    # Infere o tipo de "obj" nas declaracoes de "user", retornando
    #    - None - se objecto nao existe
    #    - "__unknown__" - se objecto existe, mas nao se sabe o tipo
    #    - <tipo> - nome do tipo inferido
    def infer_object_type(self,user,obj):
        if not self.object_exists(user, obj):
            return None
        members = self.query_local(user=user, e1=obj, rel='member')
        assocs = [d for d in self.query_local(user=user, e2=obj) \
                if not (d.relation.name == 'subtype' or d.relation.name == 'member') \
                and d.relation.cardin == None]
        if assocs != []:
            assoc_types = [d for d in self.query_local(user=user, \
                    rel=assocs[0].relation.name) if d.relation.cardin != None]
            return assoc_types[0].relation.entity2 if len(assoc_types) > 0 \
                    else '__unknown__'
        return members[0].relation.entity2 if len(members) > 0 else '__unknown__'

    # Infere o tipo de "assoc" nas declaracoes de "user", retornando:
    #    - None - caso a associacao nao exista
    #    - (t1,t2) - em que t1 e t2 sao os tipos de entity1 e entity2
    def infer_assoc_type(self,user,assoc):
        assocs = [d for d in self.query_local(user=user, rel=assoc) \
                if d.relation.cardin == None]
        print assocs
        return (self.infer_object_type(user, assocs[0].relation.entity1),\
                self.infer_object_type(user, assocs[0].relation.entity2)) \
                if assocs != [] else None

class Wikipedia(SearchDomain):
    def __init__(self,links_filename,titles_filename):
        # IMPLEMENTAR AQUI
        pass
    def actions(self, state):
        # IMPLEMENTAR AQUI
        pass
    def result(self, state, action):
        # IMPLEMENTAR AQUI
        pass

wikipedia = Wikipedia('links-small.json', 'titles-small.json')

def are_two_pages_connected(pageA, pageB):
    p = SearchProblem(wikipedia,pageA, pageB)
    t = SearchTree(p,'breadth')
    r = t.search()
    return r != None


class MySearchTree(SearchTree):
    # IMPLEMENTAR AQUI
    pass

def all_paths_to_philosophy(criterio, limit=4):
    #IMPLEMENTAR AQUI
    pass


