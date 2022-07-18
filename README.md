# project_nlp_with_nltk_corpus
This repository is about natural language toolkit focused in the nltk package corpus

## Table of Contents
* [Docker image](#docker-image)
* [Docker build](#docker-build)
* [Docker run and execute](#docker-run-and-execute)
* [Corpus available](#corpus_available)


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
Tokenizing is spliting a text in sentences or in words.

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