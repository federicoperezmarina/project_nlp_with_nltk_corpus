from nltk.corpus import stopwords

stoplist = stopwords.words('english')

text = '''Episode 1: The Phantom Menace – the one in which Star Wars becomes a lesson in trade disputes and economic sanctions.
Turmoil has engulfed the Galactic Republic. The taxation of trade routes to outlying star systems is in dispute.
Hoping to resolve the matter with a blockade of deadly battleships, the greedy Trade Federation has stopped all shipping to the small planet of Naboo.
While the congress of the Republic endlessly debates this alarming chain of events, the Supreme Chancellor has secretly dispatched two Jedi Knights, the guardians of peace and justice in the galaxy, to settle the conflict....
'''

print("\nOriginal string:")
print(text)

clean_word_list = [word for word in text.split() if word not in stoplist]
print("\nAfter removing stop words from the said text:")
print(clean_word_list)