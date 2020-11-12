# EntityLinking
## 2020 fall Period 2 Web Data Processing System Assignment1 

implement a program that receives a collection of web pages as input and returns all the entities mentioned with a link to the corresponding entity in Wikidata. Essentially, this task is to implement a entity linker.

### HTML to Text
* Use **warcio** to read warc file
* Use **BeautifulSoup** to retrieve Text from Html

### NLP Process
* Use **sent_tokenize** & **word_tokenize** from **NLTK**
* (Stemming and lemmatization may affect the results of POS tagging, so I currently skip this step)
* Stop words removal
* POS tag
* Implement NER to derive entities using **ne_chunk** in **NLTK**

### Candidate Generation
* Use **Elastic search** to get 10 potential candidates
* We are now still figuring out how to use sparql, but we first implement the cosine similarity using **strsimpy** package to compare the similarity of string between entity mention and entity candidates. 