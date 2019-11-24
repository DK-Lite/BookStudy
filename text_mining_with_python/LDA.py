from nltk.corpus import stopwords
from nltk.stem.porter import PorterSteammer
from gensim import corpora, models
import gensim
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer('[\w]+')
stop_words = stopwords.words('english')
p_stemmer = PorterSteammer()

doc_a = ""


doc_set = [doc_a, doc_b, doc_c]
texts = []

for w in doc_set:
    raw = w.lower()
    tokens = tokenizer.tokenize(raw)
    stoped_tokens = [ i for i in tokens if i in stop_words]
    stemmed_tokens = [ p_stemmer.stem(i) for i in stoped_tokens]
    texts.append(stemmed_tokens)

dictionary = corpora.Dictionary(texts)
corpus = [dixtionary.doc2bos(text) for text in texts]
idamodel = gensim.models.ldamodel.LadaModel(corpus, num_topics=3, id2word=dictionary)
ldamodel.print_topics(num_words=5)