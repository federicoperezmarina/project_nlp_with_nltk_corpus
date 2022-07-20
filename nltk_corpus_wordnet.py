from nltk.corpus import wordnet 
syns = wordnet.synsets("car")

print("Syns")
print(syns)

for syn in syns:
	print("\nDefination of the said word:")
	print(syn.definition())

	print("Examples of the word in use:")
	print(syn.examples())