# 단어 빈도 분석
import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


text = 'Chief Justice Roberts, President Carter...'

tokenizer = RegexpTokenizer('[\w]+')
stop_words = stopwords.words('english')

words = text.lower()
tokens = tokenizer.tokenize(words)
stopped_tokens = [i for i in list((tokens)) if not i in stop_words]
stopped_tokens2= [i for i in stopped_tokens if len(i) > 1]

pd.Series(stopped_tokens2).value_counts().head(10)
