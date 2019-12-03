import glob
import numpy as np
import pandas as pd
from afinn import Afinn
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

pos_reviews =[]

lines_pos = []
for review in pos_reviews:
    try:
        with open(i, 'r') as f:
            temp = f.readlines()[0]
            lines_pos.append(temp)
    except Exception as e:
        continue

neg_reviews = []
lines_neg = []
for review in neg_reviews:
    try:
        with open(i, 'r') as f:
            temp = f.readlines()[0]
            lines_neg.append(temp)
    except Exception as e:
        continue

total_text = lines_pos + lines_neg
x = np.array(["pos", "neg"])
class_Index=np.repeat(x, [len(lines_pos)])
