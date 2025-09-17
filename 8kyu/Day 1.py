
# >> 1. 불리언(boolean) 값을 입력으로 받아, true일 경우 문자열 "Yes"를, false일 경우 문자열 "No"를 반환하는 메서드를 완성하시오.

# 1-1. 내 정답

# def bool_to_word(bool):
#     if bool:
#         return 'Yes'
#     else:
#         return 'No'
    
# 1-2. 예시

def bool_to_word(bool):
    return "Yes" if bool else "No"

# ----------------------------------------------------------------------------------------------

# >> 2. 두 개의 인자를 받는 함수를 만들고, x의 처음 n개의 배수를 배열(또는 리스트)로 반환하시오.

# 주어진 수(x)와 반복 횟수(n)는 모두 0보다 큰 양수라고 가정한다.

# 반환값은 배열 또는 리스트 형태여야 한다(사용하는 언어에 따라 다름).
# Examples
# x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
# x = 2, n = 5  --> [2,4,6,8,10]

# 2-1. 내 정답

# def count_by(x, n):
#     arr = []
#     for num in range(1, n+1):
#         result = x * num
#         arr.append(result)
#     return arr

2-2. 예시 1

def count_by(x, n):
    return [i * x for i in range(1, n + 1)]

2-3. 예시 2

def count_by(x, n):
    return list(range(x, n * x + 1, x))

# ----------------------------------------------------------------------------------------------

# >> 3. 

