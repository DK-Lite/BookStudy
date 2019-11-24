import pandas as pd
import glob
from afinn import Afinn
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
import numpy as np
import matplotlib.pyplot as plt

pos_review=(glob.glob(""))[20]

with open(pos_review, 'r') as f:
    lines1 = f.readlines()[0]

afinn = Afinn()
print(afinn.score(lines1))

neg_review=(glob.glob(""))[20]

with open(pos_review, 'r') as f:
    lines2 = f.readlines()[0]

afinn = Afinn()
print(afinn.score(lines2))

NRC=pd.read_csv()
NRC=NRC[(NRC != 0).all(1)]
NRC=NRC.reset_index(drop=True)
tokenizer = RegexpTokenizer('[\w]+')
stop_words = stopwords.words('english')
p_stremmer = PorterStemmer()

raw = line1.lower()
tokens = tokenizer.tokenize(raw)
stopped_tokens = [i for i in tokens if not i in stop_words]
match_words = [x for x in stopped_tokens if x in list(NRC[0])]
emotion =[]
for i in match_words:
    temp=list(NRC.iloc[np.where(NRC[0]==i)[0],1])
    for j in temp:
        emotion.append(j)

sentiment_result1 = pd.Series(emotion).value_count()
sentiment_result1.plot.bar()



