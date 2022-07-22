from nltk.corpus import wordnet

print("\nComparing go anb return:")
v1 = wordnet.synset('go.v.01')
v2 = wordnet.synset('return.v.01')
print(v1.wup_similarity(v2))

print("\nComparing buy anb sell:")
v1 = wordnet.synset('buy.v.01')
v2 = wordnet.synset('sell.v.01')
print(v1.wup_similarity(v2))

print("\nComparing begin anb start:")
v1 = wordnet.synset('begin.v.01')
v2 = wordnet.synset('start.v.01')
print(v1.wup_similarity(v2))