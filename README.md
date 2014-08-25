py_dogeify
==========

So doge. Much conversion. Very Python. Wow. 

Simple python script to convert standard English prose into [Doge](http://en.wikipedia.org/wiki/Doge_(meme)). The script uses the [Python Natural Language Toolkit](http://www.nltk.org/) to perform parts of speech tagging/tokenization. First, all non-nouns are removed from the sentence. Each noun is then prepended with a random Doge adjective ("so", "such", "very", "much", "many", "how"). Finally, each processed sentence is appended with a random Doge exclaimation ("wow", "amaze", "excite").

Here is an example using an excerpt from the US Declaration of Independence. 

Plain text:
"We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness."

Doge-ified text:
"many truths. so self-evident. such men. how Creator. so certain. so unalienable. many Rights. much Life. much Liberty. such pursuit. very Happiness. wow."
