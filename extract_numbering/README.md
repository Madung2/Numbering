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


## [결과]
output=
{
    0:{
        "numbering_txt" : '1.', //실제 번호매기기 txt
        "num" : 1,  //번호매기기의 숫자 integer (is_numberic 이 False면 None이되야 함)
        "is_num" : True,  //번호매기기가 이있는지 여부
        "is_numeric":True,  //번호매기기 타입이 연속성이 있는지 여부
        "type": "digit",  //digit, ganada, 
    },
    1:{
        "numbering" : '2.',
        "is_num" : True, 
        "is_numeric":True, 
        "type": "digit",
    }
}

## 인풋값은 Document 오브젝트일수도 있고
## 

## [api1]
json으로 넘버링 데이터를 리턴한다

## [api2]
텍스트를 바로 numbering 추가된 텍스트로 만들어준다.


[dependancies]
libreoffice 엔진 필요