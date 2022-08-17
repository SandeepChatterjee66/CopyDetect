# import these modules
import os, timeit
from math import log, sqrt
from pandas import DataFrame
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')
ps = PorterStemmer()

#set of stop words from NLTK
stop_words = set(stopwords.words('english'))

#utlity to tokenize a long string
def tokenize(data):
	data = data.replace(',',' ',len(data)).replace('.',' ',len(data)
	       ).replace('’',' ',len(data)).replace('-',' ',len(data)).lower()
	return word_tokenize(data)
   
#utility to read text file
def read_text(file):
    with open(file,'r') as f:
        return f.read()
        
#utility to make frequency dictionary
def freq(l):
	d = {}
	for x in l:
		d[x] = d.get(x,0)+1
	return d
    

'''changing directory to read corpus'''
dnames = []
voc_set = set()
corpus = []

path = input("\nenter folder path : ").strip()
curr_dir = str(os.getcwd())
new_path = ""
if "\\" in curr_dir:
	new_path = curr_dir + "\\" + path
elif "/" in curr_dir:
	new_path = curr_dir + "/" + path
os.chdir(new_path)
	

'''reading the documents in corpus'''
for file in os.listdir():
    if file.endswith(".txt"):
        dnames.append(file.replace('.txt',''))
        file_path = f"{file}"
        content = read_text(file_path)
        words = tokenize(content)
        doc = freq(words)
        voc_set = voc_set.union(doc)
        corpus.append(doc)

print("Documents found",dnames)
        
vocab = sorted(list(voc_set))
M = len(vocab)

print("\n\nVocabulary is :\n",vocab)
print("\nLength of vocab : ",M)

stop_vocab_set  = voc_set.difference(stop_words)
stop_vocab = sorted(list(stop_vocab_set))
M_new = len(stop_vocab)

print("\n\nVocab without stopwords is :\n", stop_vocab)
print("\nLength of vocab : "    , M_new)

removed_words = sorted(list(voc_set.intersection(stop_words)))
print("\n\nremoved words are :\n", removed_words)
print("\n no of words removed : "    , len(removed_words))

"""stemming"""
stemmed_vocab = [ps.stem(word) for word in stop_vocab]

#printing stemmed_df
stemmed_df = DataFrame({"original":stop_vocab, "stemmed":stemmed_vocab})
print('\n\n\tStemming:\n',stemmed_df.to_string())

stemmed_vocab = sorted(list(set(stemmed_vocab)))
M_final = len(stemmed_vocab)

print("\n\nStemmed Vocab is :\n", stemmed_vocab)
print("  \nLength of vocab : "    , M_final)


def Working(text):
  
