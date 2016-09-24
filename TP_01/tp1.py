def locais(lst):
    if lst == []:
        return None
    loc = [flight[1] for flight in lst]
    loc += [flight[3] for flight in lst if flight[3] not in loc]
    return unique(loc)

def unique(lst, head=True, to_rtn=[]):
    if lst == []:
        return None if head else to_rtn
    return unique(lst[1:], False, to_rtn) if lst[0] in to_rtn \
            else unique(lst[1:], False, to_rtn + [lst[0]])

def tempo_medio_em_loc(lst, loc, head=True, hours=0, stays=0, init=None):
    if lst == []:
        return None if head else hours / stays
    if head and loc == lst[0][1]:
        return None
    if lst[0][3] == loc:
        return tempo_medio_em_loc(lst[1:], loc, False, hours, stays, lst[0][4])
    if lst[0][1] == loc:
        return None if head else tempo_medio_em_loc(lst[1:], loc, False, \
                hours + hour_diff(init, lst[0][2]), stays + 1, lst[0][4])
    return tempo_medio_em_loc(lst[1:], loc, False, hours, stays, None)

def hour_diff(initial, final):
    return 24 - initial + final if initial > final else final - initial

def local_central(lst, visits=[], head=True):
    if lst == []:
        if head:
            return None
        n_visits = [x[1] for x in visits]
        return visits[max(n_visits, key=lambda i: n_visits[i])][0]
    visited = [x[0] for x in visits]
    if lst[0][1] in visited:
        visits = [x if x[0] != lst[0][1] else (x[0], x[1] + 1) for x in visits]
    else:
        visits += [(lst[0][1], 1)]
    return local_central(lst[1:], visits, False)

def etapas_principais(lst):
    return ep_aux(lst, local_central(lst))

def ep_aux(lst, central, stages=[], idx=0, finished=True, head=True):
    if lst == []:
        return None if head else stages
    if finished:
        stages += [(0, [])]
    if lst[0][3] == central or len(lst) == 1:
        stages[idx] = (stages[idx][0] + hour_diff(lst[0][2], lst[0][4]), \
            stages[idx][1] + [lst[0][1]] + [lst[0][3]])
        return ep_aux(lst[1:], central, stages, idx + 1, True, False)
    else:
        stages[idx] = (stages[idx][0] + hour_diff(lst[0][2], lst[0][4]), \
            stages[idx][1] + [lst[0][1]])
        return ep_aux(lst[1:], central, stages, idx, False, False)

viagem = [ \
        ("aviao", "SaCarneiro", 10, "Stansted", 12), 
        ("comboio", "Stansted", 13, "LiverpoolStreet", 14), 
        ("metro", "LiverpoolStreet", 14, "WestBrompton", 15),
        ("metro", "WestBrompton", 16, "OxfordStreet", 17),
        ("metro", "OxfordStreet", 21, "WestBrompton", 22),
        ("metro", "WestBrompton", 9, "Victoria", 10),
        ("autocarro", "Victoria", 11, "Bristol", 14), 
        ("autocarro", "Bristol", 10, "Victoria", 13),
        ("metro", "Victoria", 13, "Westminster", 14),
        ("metro", "Westminster", 19, "CoventGarden", 20), 
        ("metro", "CoventGarden", 22, "WestBrompton", 23),
        ("metro", "WestBrompton", 9, "LiverpoolStreet", 10), 
        ("metro", "LiverpoolStreet", 10, "Stansted", 11),
        ("aviao", "Stansted", 12 ,"SaCarneiro", 14)
    ]

print(locais(viagem))
print(tempo_medio_em_loc(viagem, "WestBrompton"))
print(tempo_medio_em_loc(viagem, "Westminster"))
print(tempo_medio_em_loc(viagem, "Victoria"))
print(local_central(viagem))
print(etapas_principais(viagem))
