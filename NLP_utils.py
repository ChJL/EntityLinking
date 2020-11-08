import nltk
'''
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
'''
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize, sent_tokenize

# stemming package
from nltk.stem import PorterStemmer 
from nltk.stem import LancasterStemmer
# lemmatization package
from nltk.stem import WordNetLemmatizer
# stopwords package
from nltk.corpus import stopwords
from nltk.tree import Tree

def get_NER(postag_text, NER_List):
    #get NER
    chunked = nltk.ne_chunk(postag_text)

    for i in chunked:
        if type(i) == Tree:

            chunk_label = i.label()
            chunk_string = " ".join([token for token, pos in i.leaves()])
            NER_List.append((chunk_string, chunk_label))
            #print(current_chunk)
        '''
        if current_chunk:
            named_entity = " ".join(current_string)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                NER_List.append()
                current_chunk = []
        else:
            continue
        '''
        
    return 

def NLProcess(text):
	# tokenize, remove punctuation, remove stopwords
	tokenizer = RegexpTokenizer(r'\w+')
	#intermediate = tokenizer.tokenize(text)
	sent_text = sent_tokenize(text)
	#print(sent_text)
	for sent in sent_text:
		word_token = word_tokenize(sent)
		#word_token = tokenizer.tokenize(sent)	
	# ==== Stemming process =====
		#porter = PorterStemmer()
		#lancaster = LancasterStemmer()
		#word_token = [lancaster.stem(i) for i in word_token]
		#intermediate = [porter.stem(i) for i in word_token]
		intermediate = [w for w in word_token if not w in stopwords.words('english')]


	
	#==== pos taging ====
		postag_token = nltk.pos_tag(intermediate)
		#print(postag_token)
		NER_token = []
		get_NER(postag_token, NER_token)


	
    

	return NER_token