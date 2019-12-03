import re
p = re.compile("\W+")
print(p.sub(" ", "★서울 부동산 가격이 올해 들어 평귱 30% 상승했습니다!"))
print(p.sub(" ", "주제_1: 건강한 몸과 건강한 정신!"))

import nltk
nltk.download('stopwords')

words_Koread = ['추석', '연휴', '민족', '민족', '대이동', '을', '시작']
stopwords = ['가다', '늘어', '나타', '것', '기자']
print([ i for i in words_Koread if i not in stopwords])