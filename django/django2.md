

HTTP 응답 상태 코드 : 특정 HTTP 요청이 성공적으로 완료되었는지 알려줍니다.

![image-20220408091646575](django2.assets/image-20220408091646575.png)

403 Forbidden : 서버가 클라이언트가 누구인지 알고 있지만, csrf token이 없을 때

404 Not Found :

500 : 정확한 원인을 알 수 없음





![image-20220408094106117](django2.assets/image-20220408094106117.png)



![image-20220408095715791](django2.assets/image-20220408095715791.png)



![image-20220408095951296](django2.assets/image-20220408095951296.png)



![image-20220408095101504](django2.assets/image-20220408095101504.png)





None : 값이 없음(값)

null : 비어있음(값x)



MEDIA_URL

업로드된 파일의 주소를 만들어주는 역할

MEDIA_ROOT는 STATIC_ROOT와 다른 경로로 지정해야 함



이미지 업로드 전 이미지가 어디



키워드 인자 순서 : 데이터, 파일, 인스턴스







로그인

* `login(request, user, backend=None)`
  * 현재 세션에 연결하려는 인증된 사용자가 있는 경우 login() 함수가 필요
  * Django의 session framework를 사용하여 세션에 user의 ID를 저장(== 로그인)
  * HttpRequest 객체와 User 객체가 필요
* `get_user()`
  * AuthenticationForm의 인스턴스 메서드
  * user_cache : 인스턴스 생성 시, None으로 할당됨. 유효성 검사를 통과했을 때 로그인한 사용자 객체로 할당됨.



로그아웃

* session을 Delete하는 로직과 같음
* 





회원가입

회원탈퇴

