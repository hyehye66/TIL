# 1 : N 데이터베이스 관계



> ## Foreign Key
>
> * 외래 키(외부 키)
> * 관계형 DB에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
> * 참조하는 테이블에서 속성(필드)에 해당 & 참조되는 테이블의 기본키(Primary Key)를 가리킴
> * 참조하는 테이블의 외래키는 참조되는 테이블 행 1개에 대응됨
> * 참조하는 테이블의 행 여러 개가 참조되는 테이블의 동일한 행을 참조할 수 있음
>
> >
> >
> >### 특징
> >
> >* 참조 무결성 : 키를 사용하여 부모 테이블의 유일한 값을 참조
> >* 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요X, but 유일한 값이어야 
> >* cf) 참조 무결성
> >  * DB 관계 모델에서 관련된 2개의 테이블 간의 일관성
> >  * 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함