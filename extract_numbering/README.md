# Numbering
***
## 목표: python-docx랑 호환가능한 para_idx별 번호매기기를 모듈화


## HowTo:
1. docx파일에서 table을 제거   
2. Libreoffice를 이용해 txt로 변경   
3. 각 줄 별로 매치해 비교한다.   
4. 비교한 값이 다르다 특히 왼쪽에 있는 값이 추가되어 있다 하면 그걸 번호매기기로 인식.   
5. 번호매기기 타입이 어떤지 분석하고 결과물을 리턴   
6. 가능하다면 library로 만들어서 install 해서 사용할 수 있게 만든다   


## [What it can do]
Former word-processor processing libraries often fail to extract numbering info properly. Numbering can extract numbering infos and store it by each document
You can use it with python-docx library

## [How to use it]
```python
from numbering import DocNumberingExtractor

num = DocNumberingExtractor('NH_전담중개업무계약서.docx')
print(num.numbering_data)


from docx import Document
doc = Document('NH_전담중개업무계약서.docx')


## if 7th paragraph has missing numbering You can combine numbering info like this!

seventh_txt = doc.paragraph[7].text
seventh_numbering = num.numbering_data['numbering']

final_text = seventh_numbering + seventh_txt





```


## [Result]
output=
{
    9: 
        {
            'num_type': 'decimalEnclosedFullstop', 
            'num': 1, 
            'numbering': '1.', 
            'is_decimal': True
        }, 
    10: 
        {
            'num_type': 'decimalEnclosedFullstop', 
            'num': 2, 
            'numbering': '2.', 
            'is_decimal': True
        },
}



[dependancies]
libreoffice 엔진 필요