# project_nlp_with_nltk_corpus
This repository is about natural language toolkit focused in the nltk package corpus

## Table of Contents
* [Docker image](#docker-image)
* [Docker build](#docker-build)
* [Docker run and execute](#docker-run-and-execute)
* [Corpus available](#corpus-available)
* [Corpus stopwords](#corpus-stopwords)
* [Corpus stopwords removing](#corpus-stopwords-removing)
* [Corpus stopwords omit](#corpus-stopwords-omit)
* [Corpus wordnet](#corpus-wordnet)
* [Corpus wordnet synonyms and antonyms](#corpus-wordnet-synonyms-and_antonyms)

## Docker image
First of all we are going to use docker to prepare the environment.

This is the Dockerfile were we can see how to install python and library nltk.
```sh
FROM ubuntu:latest

COPY . /tmp/

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    pip3 install nltk && \
    python3 -m nltk.downloader all
```


## Docker build
We need to create the docker image in order to launch / execute the code. This is the way to create the docker image
```sh
docker build -t python_nlp_nltk .
```


## Docker run and execute
Now we are able to use the image with the next command
```sh
docker run -it python_nlp_nltk /bin/bash
```


## Corpus available

```python
import nltk.corpus

print("\nAvailable corpus names:")
print(dir(nltk.corpus))
```

How to execute:
```sh
cd /tmp
python3 nltk_corpus_available.py 
```

Output:
```sh
Available corpus names:
['_LazyModule__lazymodule_globals', '_LazyModule__lazymodule_import', '_LazyModule__lazymodule_init', '_LazyModule__lazymodule_loaded', '_LazyModule__lazymodule_locals', '_LazyModule__lazymodule_name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```


## Corpus stopwords
We are going to show the languages of stopwords downloaded and some english stopwords

```python
from nltk.corpus import stopwords

print("Stopwords languages: ")
print(stopwords.fileids())

print("English stopwords")
print(stopwords.words("english"))
```

How to execute:
```sh
cd /tmp
python3 nltk_corpus_stopwords.py 
```

Output:
```sh
Stopwords languages: 
['arabic', 'azerbaijani', 'basque', 'bengali', 'catalan', 'chinese', 'danish', 'dutch', 'english', 'finnish', 'french', 'german', 'greek', 'hebrew', 'hinglish', 'hungarian', 'indonesian', 'italian', 'kazakh', 'nepali', 'norwegian', 'portuguese', 'romanian', 'russian', 'slovene', 'spanish', 'swedish', 'tajik', 'turkish']
English stopwords
['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
```


## Corpus stopwords removing
In this section we are going to introduce a text and remove all the stopwords.

```python
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
```

How to execute:
```sh
cd /tmp
python3 nltk_corpus_stopwords_remove.py 
```

Output:
```sh
Original string:
Episode 1: The Phantom Menace – the one in which Star Wars becomes a lesson in trade disputes and economic sanctions.
Turmoil has engulfed the Galactic Republic. The taxation of trade routes to outlying star systems is in dispute.
Hoping to resolve the matter with a blockade of deadly battleships, the greedy Trade Federation has stopped all shipping to the small planet of Naboo.
While the congress of the Republic endlessly debates this alarming chain of events, the Supreme Chancellor has secretly dispatched two Jedi Knights, the guardians of peace and justice in the galaxy, to settle the conflict....


After removing stop words from the said text:
['Episode', '1:', 'The', 'Phantom', 'Menace', '–', 'one', 'Star', 'Wars', 'becomes', 'lesson', 'trade', 'disputes', 'economic', 'sanctions.', 'Turmoil', 'engulfed', 'Galactic', 'Republic.', 'The', 'taxation', 'trade', 'routes', 'outlying', 'star', 'systems', 'dispute.', 'Hoping', 'resolve', 'matter', 'blockade', 'deadly', 'battleships,', 'greedy', 'Trade', 'Federation', 'stopped', 'shipping', 'small', 'planet', 'Naboo.', 'While', 'congress', 'Republic', 'endlessly', 'debates', 'alarming', 'chain', 'events,', 'Supreme', 'Chancellor', 'secretly', 'dispatched', 'two', 'Jedi', 'Knights,', 'guardians', 'peace', 'justice', 'galaxy,', 'settle', 'conflict....']
```

## Corpus stopwords omit
In this section we are going omit some stopwords from the original list

```python
from nltk.corpus import stopwords

result = set(stopwords.words('english'))

print("List of stopwords in English:")
print(result)

stop_words = set(stopwords.words('english')) - set(['again', 'once', 'from'])

print("\nOmit - 'again', 'once' and 'from':")
print (stop_words)
```

How to execute:
```sh
cd /tmp
python3 nltk_corpus_stopwords_omit.py 
```

Output:
```sh
List of stopwords in English:
{'because', 'what', 'between', 'nor', 'shouldn', 'in', 'has', "that'll", 'after', 'both', "won't", 'through', 've', 'wasn', 'doing', 'had', 'won', 'those', 'about', 'do', 'have', 'don', 'him', 'they', 'up', "didn't", 'where', 'does', 'all', "you'll", 'over', 'before', 'yourselves', 'you', 'there', 'each', 'themselves', 'only', 'an', 'any', 'such', 'hasn', 'itself', 'so', 'off', 'while', "mightn't", 'herself', 'are', 'if', 'once', 'how', 'out', 'under', 'your', 'too', 'isn', 'some', 'theirs', 'mightn', 'few', 'be', 'but', 'more', 'a', 'the', "isn't", 'own', 'that', 'mustn', "hasn't", 'did', 'again', "you've", "couldn't", 'most', 'weren', 'we', 'am', 'ourselves', 'were', "should've", 'which', "wasn't", 'whom', 'aren', "you're", 'who', 'ma', 'not', "shouldn't", 'this', 'why', 'into', 'd', 'at', 'other', 'ain', 'my', 't', 'wouldn', 'when', 'now', 'yourself', 'from', 'them', 'haven', 'been', 'its', 'against', "shan't", 'didn', 'll', 'no', 'on', 'until', 'to', 'hadn', 'and', 'our', 'should', 'of', 'by', 'having', 'further', 'myself', "she's", 'is', 'here', 'y', 'm', 'then', 'will', "mustn't", "wouldn't", 'his', 'very', "don't", 'can', 'or', 'these', 'shan', 'me', 'yours', 'she', 'i', 'couldn', "weren't", "you'd", 'down', 'her', 'below', "hadn't", 'their', "it's", 'o', 'than', 'he', 'same', 's', "doesn't", 'during', "haven't", 'doesn', 're', 'being', 'just', 'it', 'for', 'with', 'above', "needn't", 'as', 'needn', 'hers', 'was', "aren't", 'ours', 'himself'}

Omit - 'again', 'once' and 'from':
{'because', 'what', 'between', 'nor', 'shouldn', 'in', 'has', "that'll", 'after', 'both', "won't", 'through', 've', 'wasn', 'doing', 'had', 'won', 'those', 'about', 'do', 'have', 'don', 'him', 'they', 'up', "didn't", 'where', 'does', 'all', "you'll", 'over', 'before', 'yourselves', 'you', 'there', 'each', 'themselves', 'only', 'an', 'any', 'such', 'hasn', 'itself', 'so', 'off', 'while', "mightn't", 'herself', 'are', 'if', 'how', 'out', 'under', 'your', 'too', 'isn', 'some', 'theirs', 'mightn', 'few', 'be', 'but', 'more', 'a', 'the', "isn't", 'own', 'that', 'mustn', "hasn't", 'did', "you've", "couldn't", 'most', 'weren', 'we', 'am', 'ourselves', 'were', "should've", 'which', "wasn't", 'whom', 'aren', "you're", 'who', 'ma', 'not', "shouldn't", 'this', 'why', 'into', 'd', 'at', 'other', 'ain', 'my', 't', 'wouldn', 'when', 'now', 'yourself', 'them', 'haven', 'been', 'its', 'against', "shan't", 'didn', 'll', 'no', 'on', 'until', 'to', 'hadn', 'and', 'our', 'should', 'of', 'by', 'having', 'further', 'myself', "she's", 'is', 'here', 'y', 'm', 'then', 'will', "mustn't", "wouldn't", 'his', 'very', "don't", 'can', 'or', 'these', 'shan', 'me', 'yours', 'she', 'i', 'couldn', "weren't", "you'd", 'down', 'her', 'below', "hadn't", 'their', "it's", 'o', 'than', 'he', 'same', 's', "doesn't", 'during', "haven't", 'doesn', 're', 'being', 'just', 'it', 'for', 'with', 'above', "needn't", 'as', 'needn', 'hers', 'was', "aren't", 'ours', 'himself'}
```

## Corpus wordnet
In this section we are going to find the definition and examples of a given word using WordNet

```python
from nltk.corpus import wordnet 
syns = wordnet.synsets("car")

print("Syns")
print(syns)

for syn in syns:
	print("\nDefination of the said word:")
	print(syn.definition())

	print("Examples of the word in use:")
	print(syn.examples())
```

How to execute:
```sh
cd /tmp
python3 nltk_corpus_wordnet.py 
```

Output:
```sh
Syns
[Synset('car.n.01'), Synset('car.n.02'), Synset('car.n.03'), Synset('car.n.04'), Synset('cable_car.n.01')]

Defination of the said word:
a motor vehicle with four wheels; usually propelled by an internal combustion engine
Examples of the word in use:
['he needs a car to get to work']

Defination of the said word:
a wheeled vehicle adapted to the rails of railroad
Examples of the word in use:
['three cars had jumped the rails']

Defination of the said word:
the compartment that is suspended from an airship and that carries personnel and the cargo and the power plant
Examples of the word in use:
[]

Defination of the said word:
where passengers ride up and down
Examples of the word in use:
['the car was on the top floor']

Defination of the said word:
a conveyance for passengers or freight on a cable railway
Examples of the word in use:
['they took a cable car to the top of the mountain']
```

## Corpus wordnet synonyms and antonyms
In this section we are going to find the synonyms and antonyms of a word with wordnet

```python
from nltk.corpus import wordnet
synonyms = []
antonyms = []
word = "old"

for syn in wordnet.synsets(word):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print("\nWord: ")
print(word)
print("\nSet of synonyms of the said word:")
print(set(synonyms))
print("\nSet of antonyms of the said word:")
print(set(antonyms))
```

How to execute:
```sh
cd /tmp
python3 nltk_corpus_wordnet_as.py 
```

Output:
```sh
Word: 
old

Set of synonyms of the said word:
{'one-time', 'erstwhile', 'old', 'onetime', 'honest-to-god', 'previous', 'older', 'honest-to-goodness', 'sure-enough', 'Old', 'quondam', 'former', 'sometime'}

Set of antonyms of the said word:
{'new', 'young'}
```