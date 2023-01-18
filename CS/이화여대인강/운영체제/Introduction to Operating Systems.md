# Introduction to Operating Systems



## 운영체제(Operating System, OS)

- 컴퓨터 하드웨어 바로 위에 설치되어 있음

- 사용자 및 다른 모든 SW와 HW를 연결하는 SW 계층

- 좁은 의미로 부를 땐, 커널
  
  - 운영체제의 핵심 부분
  
  - 부팅 일어난 이후로 항상 메모리에 상주하는 부분

- 넓은 의미로
  
  - 커널뿐만 아니라 각종 주변 시스템 유틸리티 포함한 개념

- 목적
  
  - 컴퓨터 시스템의 <mark>자원을 효율적으로 관리</mark>
    
    - 프로세서, 기억장치, 입출력 장치 등 HW 자원의 효율적 관리
      
      - 주어진 자원으로 최대한의 성능 내도록(효율성)
      
      - 사용자간의 형평성있는 자원 분배(형평성)
    
    - 사용자 및 운영체제 자신의 보호
    
    - 프로세스, 파일, 메시지 등 SW 자원을 관리
  
  - 컴퓨터 시스템을 편리하게 사용할 수 있는 환경 제공

- 분류
  
  - 동시 작업 가능 여부에 따른
    
    - 단일 작업(single tasking)
      
      - 한 번에 하나의 작업만
    
    - <mark>다중 작업(multi tasking)</mark>
      
      - 동시에 2 개 이상의 작업 처리
  
  - 사용자의 수에 따른
    
    - 단일 사용자(single user)
      
      - ex) MS-DOS, MS Windows
    
    - <mark>다중 사용자(multi user)</mark>
      
      - ex) UNIX, NT server
  
  - 처리 방식에 따른
    
    - 일괄 처리(batch processing)
      
      - 작업 요청의 일정량 모아서 한꺼번에 처리
      
      - 작업이 완전 종료될 때까지 기다려야
    
    - <mark>시분할(time sharing)</mark>
      
      - 우리가 사용하는 컴퓨터 그 자체
      
      - 여러 작업을 수행할 때 컴퓨터 처리 능력을 일정 시간 단위로 분할하여 사용
      
      - interactive한 방식
    
    - 실시간(Realtime OS)
      
      - 데드라인 정해져 있음, 정확한 시간에 맞춰서 처리되어야 하는 시스템
      
      - 정해진 시간 안에 어떠한 일이 반드시 종료됨이 보장되어야 하는 실시간 시스템을 위한 OS
      
      - 실시간 시스템의 개념 확장
        
        - Hard realtime system(경성 실시간 시스템)
        
        - Soft realtime system(연성 실시간 시스템)

- 기타 용어
  
  - Multitasking
  
  - Multiprogramming : 여러 프로그램이 메모리에 올라가 있음
  
  - Time sharing : CPU 시간을 분할하여 나누어 쓴다는 의미 강조
  
  - Multiprocessor : 하나의 컴퓨터에 CPU(processor)가 여러 개 붙어있음을 의미

- 예
  
  - 유닉스(UNIX)
    
    - 서버를 위한 운영체제
  
  - DOS(Disk Operating System)
  
  - MS Windows
    
    - 불안정성
  
  - Handheld device를 위한 OS

- 구조
  
  - 누구한테 CPU를 줄까? => CPU 스케줄링
  
  - 한정된 메모리를 어떻게 쪼개어 쓰지? => 메모리 관리
  
  - 디스크에 파일을 어떻게 보관하지? => 파일 관리
  
  - 각기 다른 입출력장치와 컴퓨터 간에 어떻게 정보를 주고 받게 하지?(장치들이 느림) => 입출력 관리
    
    - I/O device가 CPU한테 보고/요청할 때 interupt를 걸어서 알림 -> 그럼 CPU가 다음 작업을 하기 전에 요청을 처리해줌(CPU가 최대한 방해받지 않게 함) 


