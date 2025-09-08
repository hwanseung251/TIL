## 자료구조

문제마다 어떤 것을 선택 해야 할지 감이옴 

- 리스트
- set
- dictionary
- 트리
- 그래프

## 알고리즘 접근 순서

알고리즘은 어떤 순서로 고민해야 할까?

### 1️⃣ 완전 탐색 (Brute Force)

- **모든 경우의 수**를 탐색
- 시간 복잡도 확인 필수
- 가지치기(Pruning)로 경우의 수를 줄여볼 수 있음

👉 그래도 시간 복잡도가 크다면 다음 단계로 이동

---

### 2️⃣ 규칙 찾기 (Greedy)

- 탐색을 줄일 **규칙이나 패턴** 발견
- 매 순간 최적 선택이 전체 최적해가 될 수 있는지 검증 필요

👉 그리디가 불가능하다면?

---

### 3️⃣ 동적 계획법 (DP)

- **점화식**을 세워서 부분 문제를 풀고,
- 결과를 저장/재활용하여 전체 문제 해결
- 예: 피보나치 수열, 최장 증가 부분 수열(LIS)

---

👉 요약:

**완전 탐색 → 규칙(그리디) → DP**

**시간 복잡도**를 기준으로 판단하며 점진적으로 최적화한다.

→ 다른 알고리즘

# 반복과 재귀

### 반복과 재귀는 유사한 작업을 수행할 수 있다

- 반복은 수행하는 작업이 완료될 때 까지 계속  반복
    - 루프(for ,while)
    - 반복문은 코드를 n번 반복시킬 수 있음
- 재귀는 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법
    - 하나의 큰 문제를 해결할 수 있는 (해결하기 쉬운) 더 작은 문제로 쪼개고 결과들을 결합
    - 재귀호출은 n중 반복문과 같은 효과

### 재귀를 연습하기 전, 알아야 하는 함수의 특징

1. 함수를 호출할 때, int 타입 객체를 전달하면 값만 복사 됨
    
    ```python
    def KFC(x):
    		print(x) # 4
    		x += 1
    		print(x) # 5
    		
    x = 3
    KFC(x + 1)
    print(x) # 3
    
    ## 출력 순서 ##
    # 4 5 3
    ```
    
2. BTS 함수가 끝나면 Main으로 되돌아 오는 것이 아니라 해당 함수를 호출했던 곳으로 돌아옴
    
    ```python
    def BBQ(x):
    		x += 10
    		print(x)
    def KFC(x):
    		print(x)
    		x += 3
    		BBQ(x + 2)
    		print(x)
    		
    x = 3
    KFC(x + 1)
    print(x) 
    ## 출력 순서 ##
    # 4 19 7 3
    ```
    

### 재귀 호출의 종료 조건

- 재귀 호출은 무한 출력을 막기 위해 무조건 조건으로 종료를 알려야함 → 기저조건(base case)
    - 아래에서는 if문으로 기저조건 설정
        
        ```python
        path = []
        def recur(depth):
            if depth == 4:
                return [path[:]]
            result = []
            for i in range(4):
                path.append(i)
                result.append(recur(depth+1))
                path.pop()
            return result
        print(recur(0))
        ```
        
    

# ✍️추가 학습

재귀를 활용해서 0,1,2,3 으로 만들 수 있는 길이가 4인 수열 생성

재귀의 구조에 따른 반환 방식과 출력을 비교해보자

```python
# 1번
path = []
def recur(depth):
    if depth == 4:
        return path
    for i in range(4):
        path.append(i)
        recur(depth+1)
        path.pop()
print(recur(0)) # None
```

```python
# 2번
path = []
def recur(depth):
    if depth == 4:
        print(path) # path경로가 각각 출력
        return # 마지막은 None 출력: return으로 끝나기 때문
        # None 안보고 싶으면 recur(0) 호출만.
    for i in range(4):
        path.append(i)
        recur(depth+1)
        path.pop()
print(recur(0)) 
'''
[0, 0, 0, 0]
[0, 0, 0, 1]
[0, 0, 0, 2]
[0, 0, 0, 3]
[0, 0, 1, 0]
[0, 0, 1, 1]
[0, 0, 1, 2]
[0, 0, 1, 3] ....
None
'''
```

```python
# 3번
path = []
def recur(depth):
    if depth == 4:
        return [path[:]]
    result = []
    for i in range(4):
        path.append(i)
        result.append(recur(depth+1))
        path.pop()
    return result
print(recur(0)) # [[[[[[0, 0, 0, 0]], [[0, 0, 0, 1]], [[0, 0, 0, 2]], [[0, 0, 0, 3]]], [[[0, 0, 1, 0]], ...
# [path[:]] 이렇게 복사를 해서 그때의 path값을 반환해야 함
# 왜냐하면 같은 path를 활용해서 계속 수정이 일어나고 있기 때문에 
```

```python
# 4번
def recur(depth, path):
    if depth == 4:
        return [path]

    result = []
    for i in range(4):
		    # extend로 한 줄기의 재귀가 depth가 4가 되었을때 쌓인 그 결과를 result에 넣어주고
		    # result를 반환해줌.
        result.extend(recur(depth + 1, path + [i]))
    return result

all_paths = recur(0, [])
print(all_paths)
```

👉 정리:

1번은 N==4 일 때만 리턴이 일어나고 N > 4 일때는 호출만하고 그 반환값을 return하지 않음.

그래서 recur(0)은 아무 값도 반환하지 않아서 리턴이 없음.

**재귀에서 값을 모으고 싶으면 return을 통해 상위 호출로 전달**해야 한다. (3번)

출력만 하고 싶으면 print로 경로를 출력하는 건 가능 (2번)

4번처럼 전역변수를 사용하지 않고 파라미터로 사용하는게 가장 좋을 듯함.

---

# 순열

- 서로 다른 N 개에서, R개를 중복 없이, 순서를 고려하여 나열하는 것
- **중복순열** 이란?
    - 서로 다른 N 개에서, R개를 중복을 허용하고, 순서를 고려하여 나열하는 것
    - 중복순열 구현 원리
        1. 재귀호출을 할 때 마다, 이동 경로를 흔적으로 남김
        2. 가장 마지막 레벨에 도착했을 때, 이동 경로를 출력
- **중복을 취급하지 않는 순열** 구현
    - 중복순열 코드를 작성
    - 이후 중복을 제거하는 코드를 추가하면 됨
        - 전역 리스트를 사용으로 이미 선택한 숫자인지 아닌지 구분
        - “used” 또는 “visited”배열이라고 부름(in 사용 X,, 리스트 전체를 확인하기 때문에 오래걸림)

### 완전탐색 문제 1. 주사위 눈의 합

문제: 주사위를 3번 던져서 합이 10 이상인 경우의 수를 구하시오

**전역 변수를 활용**

```python
path = []
result = 0

def recur(cnt):
		global result
		if cnt == 3:
				if sum(path) <= 10:
						result += 1
						
		for num in range(1, 7):
				path.append(num)
				recur(cnt + 1)
				path.pop()
				
recur(0)
```

**전역 변수 없이 계산**

```python
path = []

def recur(cnt):
    if cnt == 3:
        if sum(path) <= 10:
            return 1
        return 0

    result = 0
    for num in range(1, 7):
        path.append(num)
        result += recur(cnt + 1)
        path.pop()

    return result

print(recur(0))
```

**더 최적화 하는 방식이 없을까?**

1. 가지치기
2. 굳이 path 리스트를 append할 필요 없이 누적 합을  활용

```python
p_sum = 0
result = 0

def recur(cnt, p_sum):
		global result
		
		if p_sum > 10:
				return 
		
		if cnt == 3:
				result += 1
				return
						
		for num in range(1, 7):
				recur(cnt + 1, p_sum + num)

				
recur(0)
```

### 완전탐색 문제2: 연속 3장의 트럼프 카드
```python
cards = ['A', 'J', 'Q', 'K']
path = []
result = 0

# 연속된 3개가 나오면 return True, 아니면 False
def count_three():
		if path[0] == path[1] == path[2]: return True
		if path[1] == path[2] == path[3]: return True
		if path[2] == path[3] == path[4]: return True
		return False

def recur(cnt):
		global result
		if cnt == 5:
				# Todo: 연속된 3개가 나오면 counting
				if count_three():
						result += 1
						print(*path)
				return
		
		# 카드 중 하나를 선택
		for idx in range(len(cards)):
				path.append(cards[idx])
				recur(cnt + 1)
				path.pop()
recur(0) 
```