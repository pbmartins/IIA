from semantic_network import *
from functools import reduce

class MySN(SemanticNetwork):
    def __init__(self):
        SemanticNetwork.__init__(self)

    def most_frequent_triple(self):
        assocs = [d.relation for d in self.declarations \
                if not (d.relation.relation == 'member' or d.relation.relation == 'subtype')]
        unique_assocs = self.create_set_assocs(assocs)
        assocs_count = [(a, len([d for d in assocs if d == a])) \
                for a in unique_assocs]
        return max(assocs_count, key=lambda ac: ac[1])

    def query_assoc(self, entity, relation):
        ancestors = [d.relation.entity2 for d in self.query_local(e1=entity, rel='member') \
                + self.query_local(e1=entity, rel='subtype')]
        to_rtn = self.query_local_assoc(entity, relation)
        if to_rtn == [] and ancestors != []:
            return reduce(lambda a, b: a + b, [self.query_assoc(a, relation) \
                    for a in ancestors], [])
        return [to_rtn]

    def create_set_assocs(self, assocs):
        set_assocs = []
        for a in assocs:
            if not a in set_assocs:
                set_assocs.append(a)
        return set_assocs

    def query_local_assoc(self, entity, relation):
        local_assocs = [d.relation for d in self.query_local(e1=entity, rel=relation)]
        if local_assocs != []:
            if isinstance(local_assocs[0], AssocNum):
                return reduce(lambda a, b: a + b, [a.entity2 for a in local_assocs], 0) \
                        / len(local_assocs)
            
            set_local_assocs = self.create_set_assocs(local_assocs)
            local_assocs_count = [(a, round(len([d for d in local_assocs if d == a]) \
                    / len(local_assocs), 2)) for a in set_local_assocs]
            local_assocs_count.sort(key=lambda ac: ac[1], reverse=True)
            if isinstance(local_assocs[0], Association):
                return (local_assocs_count[0][0].entity1, local_assocs_count[0][0].entity2, \
                        local_assocs_count[0][1])
            elif isinstance(local_assocs[0], AssocSome):
                to_rtn = []
                i = 0
                while reduce(lambda a, b: a + b, \
                        [a[1] for a in local_assocs_count[:i+1]], 0) < 0.75:
                    to_rtn += [local_assocs_count[i]]
                    i += 1
                return to_rtn
        return []

class AssocSome(Relation):
    def __init__(self, e1, assoc, e2):
        Relation.__init__(self)
        self.entity1 = e1
        self.relation = assoc
        self.entity2 = e2

class AssocNum(Relation):
    def __init__(self, e1, assoc, e2):
        Relation.__init__(self)
        self.entity1 = e1
        self.relation = assoc
        self.entity2 = e2
