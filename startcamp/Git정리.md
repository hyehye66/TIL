# Git

git은 분산버전관리시스템(DVCS) Distributed Version Control System

소스코드의 버전을 관리하고 이력도 관리할 수 있다.



## 준비하기

1. 윈도우에 git을 설치한다.(git bash 설치)
1. 초기 설치 완료 후 로컬 컴퓨터에 `Author` 정보를 설정해야한다.

```bash
$ git config --global user.email 유저이메일

$ git config --global user.name 유저이름



$ git config --global -ㅣ           // 설정값을 확인하는 명령어
```





 

## 로컬 저장소

### 1. 저장소 초기화

```bash
$ git init

~/ssafy (master)             // master명 확인으로 git 관리여부 확인
```

| Working Directory                                            | Staging Area                                                 | Local Repository(commit)                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------- |
| 실제 작업되는 공간<br  /> 변경점이 나타나면 이곳에 파일이 등록 | commit 되기 전 임시로 파일들이 보여지는 곳<br /> 이곳에서 commit 되어도 되는지 파일을 확인 | git으로 관리되는 파일들의 버전들이 저장되는 곳 |



### 2. 상태를 확인

​	$ git status       // WD, SA의 상태를 확인하기 위한 명령어

 * Untracked
   * git으로 관리되지 않았던 파일이 등록된 경우
   * WD에서 해당 단어를 확인할 수 있음
 * Tracked
   * New file : git으로 관리되지 않았던 파일이 Staging Area에 등록되었을 때 확인할 수 있음
   * modified : git으로 관리되는데 수정된 파일이 Staging Area에 등록되었을 때
   * removed : git으로 관리되는 파일 중에서 삭제된 파일인 경우



### 3. gitignore

* 프로젝트에 관련 없는 파일을 등록하여 commit 되지 않도록 하는 것

  * 민감한 개인 파일이나 

  * 개인 컴퓨터 설정파일(OS에서 활용되는 파일)

  * IDE 환경 설정 파일(.idea/)
  * 가상환경 폴더 및 파일(venv/ )

* `.gitignore` 파일을 생성(확장자는 따로 없음)

  * 제외하고 싶은 파일을 등록
  * 파일명을 적어주면 끝
  * https://gitignore.io
    * 공통적으로 제외되어야 하는 목록은 자동으로 생성
    * 우리가 직접 추가하거나 생성한 파일을 제외하고 싶다면 우리가 직접 등록해야 함
  
  
  
  
   주의! ) gitignore는 add하기 전에 미리 작성해두어야 함
  
  미리 add되어 있으면 gitignore에 등록되어 있어도 계속 관리됨
  
  

### 3. Commit을 위한 준비

```bash
$ git add 파일명
$ git add .           // 현재 폴더 내 있는 변경/추가된 파일 모두를 등록
```

* Working Directory에서 Staging Area로 관리 파일들을 이동시키는 명령어

* Staging Area에서 관리 대상에 대한 판단을 하고 commit 여부를 결정



### 4. Commit 하기

```bash
$ git commit -m "커밋 메세지를 남기자! 유의미한 내용으로 작성"
```

* 버전 이력을 확정짓는 명령어
* 해당 시점의 파일 변경된 내용을 스냅샷으로 기록해 남긴다.



### 5. Commit 이력 확인하기

```bash
$ git log
$ git log --oneline   // 한 줄로 축약해서 보여줌
$ git log -p          // 파일의 변경 내용도 같이 보여줌
$ git log -숫자        // 숫자만큼만 보여줌
```



### 원격 저장소(remote Repository)

* github/ gitlab

#### 1. 원격 저장소 등록

* 사용을 하기 위해서는 로컬에 원격 저장소의 url주소를 등록해야 함

  ```bash
  $ git remote add 저장소별명(origin) 저장소주소
  ```

* 등록된 원격 저장소의 주소를 확인하는 방법

  ```bash
  $ git remote -v
  ```

* 저장소 삭제

  ```bash
  $ git remote rm 저장소별명
  ```

  

#### 2. 원격 저장소에 commit 내용 보내기

* 로컬에 저장된 commit 정보를 원격 저장소로 전달하여 분산 버전 관리를 완성

```bash
$ git push 저장소별명 브랜치명
$ git push -u origin master
```

* -u : --set-upstream의 shortcut 형태이고 저장소 별명과 브랜치 명을 설정



### 원격 저장소에서 내려받기

#### 1. git clone (레포정보와 동기화)

* `git init`, `git remote add`, `git pull` 의 동작이 포함된 내려받기 명령어
* 아무것도 없는 상태일 때 사용
* git clone 리모트레포주소



#### 2. git pull

* remote Repository 정보를 내려받는 명령어
* remote 정보가 있어야 함
* `git pull 리모트별명 브랜치명` 



