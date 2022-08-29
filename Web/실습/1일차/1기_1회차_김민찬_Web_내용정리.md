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
* <br> : 텍스트 내에 줄 바꿈 생성
* <img> : 이미지 표현
* <span></span> : 의미 없는 인라인 컨테이너
* <hr> : 수평선


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

### id - class - 태그 순