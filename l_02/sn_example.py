



# Redes semanticas
# -- Exemplo
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2014
# 2014/10/15
#


from semantic_network import *

a = Association('socrates','professor','filosofia')
s = Subtype('homem','mamifero')
m = Member('socrates','homem')

da = Declaration('descartes',a)
ds = Declaration('darwin',s)
dm = Declaration('descartes',m)

z = SemanticNetwork()
z.insert(da)
z.insert(ds)
z.insert(dm)
z.insert(Declaration('darwin',Association('mamifero','mamar','sim')))
z.insert(Declaration('darwin',Association('homem','gosta','carne')))

# novas declaracoes

z.insert(Declaration('darwin',Subtype('mamifero','vertebrado')))
z.insert(Declaration('descartes', Member('aristoteles','homem')))

b = Association('socrates','professor','matematica')
z.insert(Declaration('descartes',b))
z.insert(Declaration('simao',b))
z.insert(Declaration('simoes',b))

z.insert(Declaration('descartes', Member('platao','homem')))

e = Association('platao','professor','filosofia')
z.insert(Declaration('descartes',e))
z.insert(Declaration('simao',e))

z.insert(Declaration('descartes',Association('mamifero','altura',1.2)))
z.insert(Declaration('descartes',Association('homem','altura',1.75)))
z.insert(Declaration('simao',Association('homem','altura',1.85)))
z.insert(Declaration('darwin',Association('homem','altura',1.75)))

z.insert(Declaration('descartes', Association('socrates','peso',80)))
z.insert(Declaration('darwin', Association('socrates','peso',75)))
z.insert(Declaration('darwin', Association('platao','peso',75)))


z.insert(Declaration('damasio', Association('filosofo','gosta','filosofia')))
z.insert(Declaration('damasio', Member('socrates','filosofo')))

print(z)
print("-------------------------------------")
print("predecessor('vertebrado', 'socrates'):")
print(z.predecessor('vertebrado', 'socrates'))
print("-------------------------------------")
print("predecessor_path('vertebrado', 'socrates'):")
print(z.predecessor_path('vertebrado', 'socrates'))
print("-------------------------------------")
print("association_names():")
print(z.association_names())
print("-------------------------------------")
print("members():")
print(z.members())
print("-------------------------------------")
print("users():")
print(z.users())
print("-------------------------------------")
print("types():")
print(z.types())
print("-------------------------------------")
print("associations():")
print(z.associations())
print("-------------------------------------")
print("user_relations('descartes'):")
print(z.user_relations('descartes'))
print("-------------------------------------")
print("n_user_associations('descartes'):")
print(z.n_user_associations('descartes'))
print("-------------------------------------")
print("entity_associations('socrates'):")
print(z.entity_associations('socrates'))
print("-------------------------------------")
print("query('socrates', 'altura'):")
print(z.query('socrates', 'altura'))
print("-------------------------------------")
print("query2('socrates', 'altura'):")
print(z.query2('socrates', 'altura'))
print("-------------------------------------")
print("query_cancel('socrates', 'altura'):")
print(z.query_cancel('socrates', 'altura'))
print("-------------------------------------")
print("query_assoc_value('socrates', 'altura'):")
print(z.query_assoc_value('socrates', 'altura'))
print("-------------------------------------")
print("query_down('vertebrado', 'altura'):")
print(z.query_down('vertebrado', 'altura'))
print("-------------------------------------")
print("query_induce('vertebrado', 'altura'):")
print(z.query_induce('vertebrado', 'altura'))

