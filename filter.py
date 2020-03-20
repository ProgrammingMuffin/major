from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

def removeStopWords(sentence):
    words = word_tokenize(sentence)
    stopWords = set(stopwords.words('english'))
    newWords = [word for word in words if not word in stopWords]
    return newWords

def extractUselessWords(words):
    #handle removal of useless words

