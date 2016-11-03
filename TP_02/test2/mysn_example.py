
from mysemnet import *
from semantic_network import *

z = MySN()

# socrates
z.insert(Declaration('descartes',Member('socrates','homem')))
z.insert(Declaration('damasio', Member('socrates','filosofo')))

z.insert(Declaration('damasio', Association('socrates','tem_pai','sofronisco')))
z.insert(Declaration('descartes', Association('socrates','tem_pai','sofronisco')))
z.insert(Declaration('simao', Association('socrates','tem_pai','sofronisco')))
z.insert(Declaration('simoes', Association('socrates','tem_pai','sofronesio')))

z.insert(Declaration('einstein',Association('socrates','professor','matematica')))
z.insert(Declaration('descartes',Association('socrates','professor','filosofia')))
z.insert(Declaration('simao',Association('socrates','professor','filosofia')))
z.insert(Declaration('simoes',Association('socrates','professor','filosofia')))
z.insert(Declaration('silva',Association('socrates','professor','filosofia')))


# platao
z.insert(Declaration('descartes', Member('platao','homem')))
z.insert(Declaration('descartes',Association('platao','professor','filosofia')))
z.insert(Declaration('simao',Association('platao','professor','filosofia')))

# aristoteles
z.insert(Declaration('descartes', Member('aristoteles','homem')))

# filosofo
z.insert(Declaration('platao', Association('filosofo','tem_cerebro','sim')))

# homem
z.insert(Declaration('darwin',Subtype('homem','mamifero')))
z.insert(Declaration('darwin', Association('homem','tem_cerebro','sim')))
z.insert(Declaration('damasio',Association('homem','tem_cerebro','sim')))
z.insert(Declaration('et',Association('homem','tem_cerebro','nao')))
z.insert(Declaration('darwin',Association('mamifero','mamar','sim')))

# mamifero
z.insert(Declaration('darwin',Subtype('mamifero','vertebrado')))
z.insert(Declaration('damasio', Association('mamifero','tem_cerebro','sim')))

# Extra - descomentar para o exercicio 3.

z.insert(Declaration('descartes', AssocNum('socrates','peso',80)))
z.insert(Declaration('darwin', AssocNum('socrates','peso',75)))
z.insert(Declaration('darwin', AssocNum('platao','peso',75)))

z.insert(Declaration('descartes',AssocNum('homem','altura',1.75)))
z.insert(Declaration('simao',AssocNum('homem','altura',1.85)))
z.insert(Declaration('darwin',AssocNum('homem','altura',1.75)))
z.insert(Declaration('descartes',AssocNum('mamifero','altura',1.2)))

z.insert(Declaration('darwin',AssocSome('homem','gosta','carne')))
z.insert(Declaration('simao',AssocSome('homem','gosta','carne')))
z.insert(Declaration('darwin',AssocSome('homem','gosta','peixe')))
z.insert(Declaration('simao',AssocSome('homem','gosta','peixe')))
z.insert(Declaration('simao',AssocSome('homem','gosta','couves')))

z.insert(Declaration('damasio', AssocSome('filosofo','gosta','filosofia')))

print("z.most_frequent_triple():")
print(z.most_frequent_triple())
print("--------------------------------------")
print("z.query_assoc('socrates', 'professor'):")
print(z.query_assoc('socrates', 'professor'))
print("--------------------------------------")
print("z.query_assoc('socrates', 'tem_cerebro'):")
print(z.query_assoc('socrates', 'tem_cerebro'))
print("--------------------------------------")
print("z.query_assoc('homem', 'tem_cerebro'):")
print(z.query_assoc('homem', 'tem_cerebro'))
print("--------------------------------------")
print("z.query_local_assoc('socrates', 'professor'):")
print(z.query_local_assoc('socrates', 'professor'))
print("--------------------------------------")
print("z.query_local_assoc('homem', 'gosta'):")
print(z.query_local_assoc('homem', 'gosta'))
print("--------------------------------------")
print("z.query_local_assoc('socrates', 'peso'):")
print(z.query_local_assoc('socrates', 'peso'))
