from nltk.corpus import stopwords

result = set(stopwords.words('english'))

print("List of stopwords in English:")
print(result)

stop_words = set(stopwords.words('english')) - set(['again', 'once', 'from'])

print("\nOmit - 'again', 'once' and 'from':")
print (stop_words)