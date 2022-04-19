# Django Form



## Form

> ### Django's forms
>
> * Django의 유효성 검사 도구 중 하나
>
> * 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단
>
> * Django는 Form과 관련한 유효성 검사를 단순화하고 자동화할 수 있는 기능을 제공 
>
>   👉 직접 작성하는 코드보다 안전하고 빠르게 수행하는 코드 작성할 수 있음
>
> * Django가 처리해주는 form에 관련한 작업 3 가지
>
>   * 렌더링을 위한 데이터 준비 및 재구성
>   * 데이터에 대한 HTML forms 생성
>   * 클라이언트로부터 받은 데이터 수신 및 처리



> ### The Django 'Form Class'
>
> * Django Form 관리 시스템의 핵심
> * Form 내 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않는 field에 관련된 에러 메세지를 결정



> ### Form 선언하기
>
> * Model 선언과 유사
> * 같은 필드타입 사용
> * forms 라이브러리에서 파생된 Form 클래스를 상속받음



> ### Form rendering options
>
> * <label> & <input> 쌍에 대한 3 가지 출력 옵션
>
> 1. as_p()
>    * 각 필드가 단락(`<p>` 태그)으로 감싸져서 렌더링됨
> 2. as_ul()
>    * 각 필드가 단락(`<li>` 태그)으로 감싸져서 렌더링됨
>    * `<ul>` 태그는 직접 작성해야 함
> 3.  as_table()
>    * 각 필드가 단락(`<tr>` 태그)으로 감싸져서 렌더링됨
>    * `<table>` 태그는 직접 작성해야 함



> ### Django의 HTML input 요소 표현 방법 2 가지
>
> 1. Form fields
>    * input에 대한 유효성 검사 로직을 처리하며 템플릿에서 직접 사용됨
> 2. Widgets
>    * 웹 페이지의 HTML input 요소 렌더링
>    * GET/POST 딕셔너리에서 데이터 추출
>    * widgets은 반드시 Form fields에 할당됨



> ### Widgets
>
> * Django의 HTML input element 표현
> * HTML 렌더링 처리
> * 주의사항
>   * Form Fields와 혼동되어서는 안됨
>   * Form Fields는 input 유효성 검사를 처리 
>   * Widgets은 웹 페이지에서 input element의 단순 raw한 렌더링 처리



## ModelForm





