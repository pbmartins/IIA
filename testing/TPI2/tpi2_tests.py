#encoding: utf8

from tpi2 import *

z = MySemNet()

print z.add_association('descartes','socrates','professor','filosofia')
print z.add_subtype('descartes','mamifero','vertebrado')
print z.add_subtype('descartes','homem','mamifero')
print z.add_association('descartes','socrates','professor','matematica')
print z.add_member('descartes','platao','homem')
print z.add_association('descartes','platao','professor','filosofia')
print z.add_association('descartes','socrates','peso',80)
print z.add_member('descartes','socrates','homem')
print z.add_member('descartes', 'aristoteles','homem')
print z.add_association('descartes','mamifero','altura','number','one',1.2)
print z.add_association('descartes','socrates','altura',1.85)

print z.add_subtype('darwin','homem','mamifero')
print z.add_subtype('darwin','mamifero','vertebrado')

print z.add_association('simao','socrates','professor','matematica')
print z.add_association('simao','platao','professor','filosofia')

print z.add_association('simoes','socrates','professor','matematica')

print z.add_member('damasio','socrates','filosofo')

#z.query_local()
#z.show_query_result()



#print are_two_pages_connected('Social_thought','Philosophy')

#print all_paths_to_philosophy(lambda p: "Taekwondo" in p)

print "------------------------------"
print "1 a):"
print z.object_exists('descartes','socrates')
print z.object_exists('descartes','homem')
print z.object_exists('descartes','merkel')
print z.object_exists('descartes','filosofia')

print "------------------------------"
print "1 b):"
print z.type_exists('descartes','socrates')
print z.type_exists('descartes','homem')
print z.type_exists('descartes','number')
print z.type_exists('descartes','reptil')

print "------------------------------"
print "1 c):"
print "objet_type:"
print z.infer_object_type('descartes','platao')
print z.infer_object_type('descartes','marx')
print z.infer_object_type('descartes','filosofia')
print z.infer_object_type('descartes',1.85)
print "assoc_type:"
print z.infer_assoc_type('descartes','professor')
print z.infer_assoc_type('descartes','amigo')
print z.infer_assoc_type('descartes','altura')
