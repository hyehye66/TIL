# 트리



## 트리



* 비선형 구조

* 계층형 자료구조

* 노드 : 트리의 원소

  * 최상위 노드 : 루트(root)
  * 정점(node, vertex)
  * 단말노드/잎(leaf) 노드

* 간선(edge) : 노드를 연결하는 선

* 차수(degree)

  * 노드의 차수 : 노드에 연결된 자식 노드의 수
  * 트리의 차수: 트리에 있는 노드의 차수 중 가장 큰 값
  * 단말 노드는 차수가 0

* 높이

  * 노드의 높이 : 루트에서 노드에 이르는 간선의 수
  * 트리의 높이 : 트리에 있는 노드의 높이 중 가장 큰 값/최대 레벨

* 이진트리 : 모든 노드들이 2 개의 서브트리를 갖는 특별한 형태의 트리

  



## 힙



* 완전 이진트리



### 삽입

1) 마지막 인덱스 뒤에 인덱스 하나 더 추가 후 숫자 삽입
2) 부모노드와 추가한 값을 비교
3) 최대힙일 경우, 부모노드보다 크면/ 최소힙일 때는 부모노드보다 작으면 => 자리 바꿈 => 반복
4) 비교할 부모 노드가 없으면 자리 확정

* 예시

```python
# 최대 100개의 정수
# 최대힙

def enq(n):
	global last
    last += 1
    tree[last] = n  # 완전이진트리 유지
    c = last        # 새로 추가된 정점을 자식으로
    p = c//2        # 완전이진트리에서의 부모 정점 번호
    # 부모가 있는 상태에서 자식의 키값이 더 크면 교환
    while p >= 1 and tree[p] < tree[c]:    
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

# 포화이진트리의 정점번호
tree = [0]*101
last = 0    # 마지막 정점 번호
enq(3)
enq(2)
enq(4)
enq(7)
enq(5)
enq(1)
print(tree[1])
==> 7

```



### 삭제

* 힙에서는 루트 노드의 원소만을 삭제할 수 있음
* 루트 노드의 원소를 삭제하여 반환함
* 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있음 



최대힙일 경우,

1. 루트 노드의 원소 삭제 but 원소 따로 보관
2. 마지막 노드 삭제, 루트에 마지막 노드의 원소를 복사
3. last(마지막 인덱스) 감소시킴
4. 루트 노드의 자식 노드 중 더 큰 자식과 자리 바꿈 => 반복

* 예시

  ```python
  # 최대 100개의 정수
  # 최대힙
  
  #=== def enq(n) 생략===
  
  def deq(n):
  	global last
      tmp = tree[1]   # 루트의 key값
      tree[1] = tree[last]   # 마지막 정점의 키를 루트에 복사
      last -= 1       # 마지막 정점 삭제
      # 부모 > 자식 규칙 유지
      p = 1
      c = p*2         # 왼쪽자식노드 번호
      while c <= last:       # 왼쪽자식이 있으면
          # 오른쪽 자식노드가 있고 더 크면
          if c+1 <= last and tree[c] < tree[c+1]:
              c += 1         # 오른쪽 자식 선택
          # 자식의 키값이 더 크면 교환
          if tree[p] < tree[c]:
              tree[p], tree[c] = tree[c], tree[p]
              p = c
              c = p*2
          else:
              break
      return tmp            
  
  # 포화이진트리의 정점번호
  tree = [0]*101
  last = 0    # 마지막 정점 번호
  enq(3)
  enq(2)
  enq(4)
  enq(7)
  enq(5)
  enq(1)
  enq(9)
  while last>0:
      print(deq())
      print(tree(1))
  ==> 
  9 7
  7 5
  5 4
  4 3
  3 2
  2 1
  1 1
  ```

  

### 완전이진트리에서의 순회

```python
def pre_order(v):
    global last
    if v <= last: # 마지막 정점번호 이내
        print(v)  # visit(v)
        pre_order(v*2)   # 왼쪽
        pre_order(v*2+1)   # 오른쪽        
```

* 일반트리와 완전이진트리의 차이점 : 일반트리는 일일이 다 가봐야 존재하는지 앎(리스트에 저장된 값을 가져오는 방식). 완전이진트리는 유추가능. 자식노드가 존재하면 반드시 left, right 순으로 존재하므로.

cf. 일반트리에서의 순회

```python
def pre_order(v):
    if v:  # 0번 정점이 없으므로
        print(v)
        pre_order(ch1[v])    # 리스트에 저장된 값을 가져오는 방식
        pre_order(ch2[v])
        
def in_order(v):
    if v:
        in_order(ch1[v])
        print(v)
        in_order(ch2[v])             
```

