
# ----------------------------------------------------------------------------------------------

# >>6. 문제 해석

# 함수 설명
# 개인화된 인사를 해주는 함수를 만드세요.
# 이 함수는 두 개의 매개변수를 받습니다: name 과 owner

# 조건문을 사용해서 적절한 메시지를 반환하세요:


# name 이 owner 와 같을 때	'Hello boss'
# 그 외의 경우	'Hello guest'


# 6-1. 내 방법

# def greet(name, owner):
#     return "Hello boss" if name == owner else "Hello guest"

6-2. 예시 1

def greet(name, owner):
    return "Hello {}".format("boss" if name == owner else "guest")

# ----------------------------------------------------------------------------------------------

# >>7. 문제 해석

# 문제 설명
# 주어진 배열 안에 있는 숫자들의 평균을 계산하는 함수를 작성하세요.

# 주의:
# 배열이 비어 있는 경우에는 0을 반환해야 합니다.

# 7-1. 내 방법

# def find_average(numbers):
    
#     sum = 0
    
#     if len(numbers) == 0:
#         return 0
    
#     else :    
#         for i in numbers:
#             sum += i
#         avg = sum / len(numbers)
    
#         return avg
    
7-2. 예시 1

def find_average(array):
    return sum(array) / len(array) if array else 0

7-3. 예시 2 (try except 구문 활용) 

def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:  ## 이렇게 에러를 명시해놨을 경우, 여기에 해당하지 않는 오류가 발생했을 땐 똑같이 에러가 남
        return 0
    
# ----------------------------------------------------------------------------------------------

# >>8. 문제 해석

# 문제 설명
# 정수들이 들어 있는 배열이 주어집니다. 배열 안에는 문자열로 된 숫자와 숫자 자체가 섞여 있을 수 있습니다.

# 배열의 모든 값을 숫자로 변환한 후 합을 구해서 반환하세요.

# 반환값: 숫자(number) 형태로 반환해야 합니다.


# 8-1. 내 방법 (map으로 iterable 요소들을 모두 int로 바꾸기)
# def sum_mix(arr):
#     return sum(map(int, arr))

8-2. 예시 1

def sum_mix(arr):
    return sum(int(i) for i in arr)

8-3. 예시 2

def sum_mix(arr):
    result = 0
    for a in arr:
        try:
            result += a
        except TypeError:
            result += int(a)
    return result


# ----------------------------------------------------------------------------------------------

# >>9. 문제 해석
# 문제 설명
# 비어 있지 않은 정수 배열이 주어집니다.

# 배열 안의 값들을 순서대로 모두 곱한 결과를 반환하세요.


# 9-1. 내 방법
# def grow(arr):
    
#     multiple = 1
#     for i in arr:
#         multiple *= i
        
#     return multiple

9-2. 예시 1 (functools.reduce 사용)  // reduce (적용할 함수, 배열iterable, 초기값)

from functools import reduce
import operator

def multiply_array(arr):
    return reduce(operator.mul, arr, 1)  # 초기값 1, operator.mul : 곱셈 함수

print(multiply_array([1, 2, 3, 4]))  # 24

9-3. 예시 2 ((lambda로 압축))--------------------------------

from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)

# ----------------------------------------------------------------------------------------------

# >>10. 문제 해석
# 문제 설명
# 정수를 하나 입력받아, 짝수이면 "Even", **홀수이면 "Odd"**를 반환하는 함수를 작성하세요.

# 10-1. 내 방법
# def even_or_odd(number):
# 	return 'Odd' if number % 2 else 'Even'


10-2. 예시 1

def even_or_odd(number):
  return ["Even", "Odd"][number % 2]

10-3. 예시 2
# lambda로 함수를 정의하고 있으므로, def even_or_odd()로 추가로 정의하면 안 됨
even_or_odd = lambda number: "Odd" if number % 2 else "Even"

# ----------------------------------------------------------------------------------------------

# >>11. 문제 해석

# 문제 설명

# 문자열의 첫 글자와 마지막 글자를 제거하는 함수를 작성하세요.

# 함수는 원본 문자열을 하나 매개변수로 받습니다.

# 문자열 길이는 최소 2글자 이상이라고 가정합니다.

# 중요 사항

# 길이가 정확히 2글자인 문자열은 **빈 문자열('')**을 반환해야 합니다.

# 예시
# 입력	출력
# 'eloquent'	'loquen'
# 'country'	'ountr'
# 'person'	'erso'
# 'ab'	'' (빈 문자열)
# 'xyz'	'y'

# 11-1. 내 방법
def remove_char(s):
    original = s
    
    return original[1:-1]

// 슬라이싱 관련 개념
sequence[start:stop:step]

s = 'Hello, World!'

print(s[0:5])  # 'Hello' → 인덱스 0~4
print(s[7:12]) # 'World' → 인덱스 7~11
print(s[-6:-1]) # 'World' → 뒤에서 6번째부터 뒤에서 2번째까지
print(s[::2])   # 'Hlo ol!' → 한 글자 건너뛰면서 가져오기
print(s[::-1])  # '!dlroW ,olleH' → 문자열 뒤집기

lst = [1, 2, 3, 4, 5, 6]

lst[-3:] → [4, 5, 6] 
lst[:-4:-1] → [6, 5, 4] // step으로 먼저 리스트 방향 설정한 뒤 슬라이싱하게 됨 ([6,5,4,3,2,1]인 리스트를 처음부터 인덱스 번호 -4 전(-5까지)인 요소까지 잘라오겠다는 말)


# ----------------------------------------------------------------------------------------------

# >>12. 문제 해석

문제 설명

숫자 집합(리스트)이 주어지면, 각 숫자의 **가산 역수(additive inverse)**를 반환하세요.

양수는 음수로, 음수는 양수로 바꿔야 합니다.

예시
[1, 2, 3, 4, 5]   --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[]                 --> []

12-1. 내 방법
