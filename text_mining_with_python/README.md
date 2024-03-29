# 텍스트 마이닝 with Python

## 텍스트 데이터
텍스트는 수치형 데이터와 다르게 분석 전 정교한 정제 작업이 필요

### 정규 표현식
정규 표현식은 텍스트 문자열에서 패턴을 파악하여 식별하는데 쓰인다. 
 - 분석에 도음이 되지 않는 부분들은 제거 (신문 기사에서 이메일 정보는 필요가 없기에 삭제)
    ```python
    @신문 기사에서 이메일을 제거하는 정규표현식 

    import re
    re.sub("\([A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edy|net|co,kr)\)","", string)

    # [A-Za-z0-9\._+] : ID 
    # @ 
    # [A-Za-z]  : 주소
    # (com|org|edy|net|co,kr) : 뒤에 올 패턴

    # 이메일 주소가 처음 ( ) 안에 있으므로 \()
    # [] 안에 이메일주소 패턴을 삽입 (대괄호 안에 아무거나 라는 뜻)
    # A-Z, a-z, 0-9는 각각 범위를 의미
    # 마침표의 경우 원래 의미로 쓰기 위해 이스케이프 문자 \ 와 같이 사용
    ```


### 사전처리
텍스트 데이터 집합을 말뭉치(Corpus)라고 부름 이러한 말뭉치는 대용량의 정형화된 텍스트 집합으로
정의되는데 이 의미를 알아야함
- 텍스트 정형화는 원(raw) 텍스트 데이터를 정제하거나 사전 처리하는 작업을 **정형화 과정**이라함

 텍스트 사전처리는 아래와 같이 공통적인 과정을 거친다.
- 대소문자 통일
    ```python
    s = 'Hello World'
    s.lower(), s.upper()

    # hello world, HELLO WORLD
    ```
- 숫자, 문장부호, 특수문자 제거
    ```python
    @각 문서에서 사용된 날짜, 수치, 퍼센티지들은 각 문서에서만 의미가 있지 전체 문서 집합에서는 의미가 없으므로 분석시 어려움을 준다.

    import re
    p = re.compile("[0-9]+") # 0~9사이가 한번이라도 나타남
    p.sub("", "오늘 날씨는 40도 입니다")
    # 오늘 날씨는 도 입니다

    p = re.compile("\W+") # 모든 문자, 숫자, 밑줄까지 포함
    print(p.sub(" ", "★서울 부동산 가격이 올해 들어 평귱 30% 상승했습니다!"))
    print(p.sub(" ", "주제_1: 건강한 몸과 건강한 정신!"))
    ```

- 불용어 제거
    ```python
    @텍스트 마이닝 페키지 NLTK를 사용하면 된다 하지만 한국어는 미지원
    # pip install nltk : 설치 진행
    # import nltk, nltk.download('stopwords') : stopwords(불용어 패키지) 라이브러리를 다운
    import nltk
    nltk.download('stopwords')

    words_Koread = ['추석', '연휴', '민족', '민족', '대이동', '을', '시작']
    stopwords = ['가다', '늘어', '나타', '것', '기자']
    print([ i for i in words_Koread if i not in stopwords])

    # English case
    words_English = [...]
    print([ w for w in words_English if not w in stopwords.words('english')])
    ```

- 같은 어근 동일화(stemming)
    ```python
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize
    ps_stemmer = PorterStemmer()

    new_test = "It is important to ..."
    words = word_tokenize(new_test)
    for w in words:
        print(ps_stemmer.stem(w), end=' ')
    ```

- N-Gram
    ```python
    from nltk import ngrams
    sentence = "Chief Justice Roberts, President Catter, President Clinton, ..."
    grams = ngrams(sentence.split(), 2)
    for gram in grams:
        print(gram, end=" ")
    ```


### 품사분석
- 흔히 알고 있는 동사, 명사, 형용사 등 각각의 단어는 문장 안에서 품사에 맞는 고유한 기능을 수행
- 품사분석은 Part-Of-Speech의 앞글자를 따서 **POS태깅**이라고 부름
- 대부분의 텍스트 마이닝은 단어주머니(Bag of words)를 이용하여 분석을 수행
- 가장 기본적인 텍스트 마이닝은 문서에서 명사만을 추출하여 분석하는 경우


## 텍스트 마이닝 기법

### 단어 빈도분석
- 데이터에 대한 이해와 흐름을 살펴보기 위한 기초분석
- 데이터수, 평균, 표준편차, 4분위값, 최대값, 최솟값 같은 요약표를 살펴보고 분석
- 특정단어가 자주 출현 할 수록 핵심단어
- 불용어 제거가 필요

### 군집 분석


### 토픽모델링
- LDA ()
- LDA 토픽 개수 지정 방법
    - 통계적 방법으로는 크게 perplexity or topic coherence 점수를 사용
    -  perplexity : 특정 확률모델이 실제로 관측되는 값을 어마나 잘 예측하는지 평가할때 사용
    - 


### 감성분석

감성분석은 텍스트에 나타난 주관성 요소를 탐지하여 긍정과 부정의 요소 및 그 정도성을 판별하여 정량화하는 작업

감성분석은 크게 두가지 방법으로 **단어 사전 기반 분석**과 **지도 기계학습 기반 분석**으로 분류 할 수 있음.

- 단어 사전 기반 분석 
    텍스트에 쓰인 단어의 감성수준을 감성사전을 통해 구한 후 감성의 정도를 계산하는 방법
    - **감성사전**을 무엇으로 쓰느냐가 매우 중요
        - AFINN : 2477개의 감성어들이 영어 사용자의 판단을 근거로 부정적 or 긍정적 점수를 부여
        - EmoLex : 분노, 공포, 기대, 신뢰, 놀람, 기쁨 등등 8가지 감정으로 나눔
        - Bing Liu lexicon : 긍정, 부정만 분류 따로 점수는 지표하지 않음
        - SentiWordNet : 긍정, 부정 중립 으로 단어를 분류, python NLTK패키지에서 사용가능



- 지도 기계학습 기반 분석
기계학습이랑 훈련 데이터로 부터 하나의 함수를 유추해내기 위한 기계 학습의 방법
훈련데이터는 입력객체의 특징 벡터로 이루어짐
사용되는 알고리즘으로는 아래와 같다
- Support Vector Machine
    데이터가 사상된 공간에서 경계를 찾고자 할떄 가장 큰폭을 가지는 경계를 찾는 알고리즘
- Reggression 
    여러 속성들의 데이터들간의 수학적이 모델링을 통해 함수를 찾아냄
- Neunal Network
    네트워크 모델이 반복적인 학습을 통해서 최적의 가중치를 찾아냄
- Naive Bayes
    조건부 확률 모델을 이용하여 카테고리르 분류 모델을 생성
- Decision Tree
    데이터 분석을 통해 이들 사이의 규칙들의 조합을 찾아냄


### 연관어 분석






