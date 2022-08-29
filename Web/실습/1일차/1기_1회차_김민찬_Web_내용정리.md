# HTML(Hyper Text Markup Language)

웹을 이루는 가장 기초적인 구성 요소


## 기본 구조

* html : 문서의 최상위(root) 요소
* head : 문서 메타데이터 요소
* body : 문서 본문 요소


## head 예시

<head>
  <title> HTML 복습 </title>
  <meta charset='UTF-8'>
  <link href='style/css' rel='stylesheet'>
  <script src='javascript.js'></script>
  <style>
    p {
      color: blue;
    }
  </style>
</head>


## HTML 속성

* id : 문서 전체에서 유일한 고유 식별자 지정
* class : 공백으로 구분된 해당 요소의 클래스 목록
* data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용

## HTML 코드 예시

<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <title>Document</title>
</head>
<body>
  <!-- 이것은 주석입니다. -->
  <h1>나의 첫번째 HTML</h1>
  <p>이것은 본문입니다.</p>
  <span>이것은 인라인 요소</span>
  <a href='https://www.naver.com'>네이버로 이동!!</a>
</body>
</html>


## 텍스트 요소

* <a></a> : href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성
* <b></b> / <strong></strong> : 굵은 글씨
* <i></i> / <em></em> : 기울임 글씨
* &nbsp; : 띄어쓰기
* <br> : 텍스트 내에 줄 바꿈 생성
* <img> : 이미지 표현
* <img alt> : 이미지를 보여줄 수 없을 때 해당 이미지를 대체할 텍스트
* <span></span> : 의미 없는 인라인 컨테이너
* <hr> : 수평선


## 그룹 컨텐츠

* <p></p> : 하나의 문단(paragraph)
* <ol></ol> : 순서가 있는 리스트(ordered)
* <ul></ul> : 순서가 없는 리스트(unorderd)
* <pre></pre> : HTML에 작성한 내용을 그대로 표현 -> 보통 고정폭 글꼴이 사용되고 공백문자를 유지
* <blockquote></blockquote> : 텍스트가 긴 인용문 -> 주로 들여쓰기를 한 것으로 표현
* <div></div> : 의미 없는 블록 레벨 컨테이너


# CSS(Cascading Style Sheets)

스타일을 지정하기 위한 언어


## CSS 구문

h1 {
  color: blue;
  font-size: 15px;
}

* h1 : 선택자(Selector)
* color: blue : 선언(Declaration)
* font-size : 속성(Property)
* 15px : 값(Value)

## CSS 특성

* 선택해서 스타일을 적용
* 적용에는 우선순위 -> id - class - 태그 순
* 같은 레벨이라면 나중에 '선언'된 것이 적용
* 다만, 일반적으로 CSS 스타일링은 클래스로만 함
* id는 문서에서 반드시 한번만 등장