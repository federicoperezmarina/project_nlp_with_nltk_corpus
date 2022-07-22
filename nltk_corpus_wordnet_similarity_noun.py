from nltk.corpus import wordnet

print("\nComparing car anb automobile:")
n1 = wordnet.synset('car.n.01')
n2 = wordnet.synset('automobile.n.01')
print(n1.wup_similarity(n2))

print("\nComparing ship anb boat:")
n1 = wordnet.synset('ship.n.01')
n2 = wordnet.synset('boat.n.01')
print(n1.wup_similarity(n2))

print("\nComparing bus anb boat:")
n1 = wordnet.synset('bus.n.01')
n2 = wordnet.synset('boat.n.01')
print(n1.wup_similarity(n2))