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









