
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

# >> 3. 문제 해석

# DNA(데옥시리보핵산) 생물학적 시스템에서 정보 저장의 주된 분자

# 네 가지 염기(base)로 구성:
# Guanine → 'G'
# Cytosine → 'C'
# Adenine → 'A'
# Thymine → 'T'

# RNA(리보핵산) 세포 안에서 주요 메신저 분자
# DNA와 화학 구조가 조금 다르며, Thymine(T) 없음, DNA의 Thymine(T)은 RNA에서는 **Uracil(U)**로 대체됨

# 함수 요구 사항
# DNA 문자열을 입력으로 받아 RNA 문자열로 변환하는 함수 작성

# 변환 규칙:
# 'G' → 'G'
# 'C' → 'C'
# 'A' → 'A'
# 'T' → 'U'

# 입력 문자열 길이는 임의이며, 빈 문자열도 가능

# 입력은 항상 유효하며, 'G', 'C', 'A', 'T'만 포함


# 3-1. 내 방법

# def dna_to_rna(dna):
#     return dna.replace('T', 'U')

# 3-2. 예시 1 (join 메서드와 리스트 내포 활용)

def dna_to_rna(dna):
    return ''.join(['U' if x == 'T' else x for x in dna])

# 3-3. 예시 2 (정규식 활용)

import re
def dna_to_rna(dna):
    return re.sub('T', 'U', dna) # re.sub("찾을문자","바꿀문자", "전체문자열")

# ----------------------------------------------------------------------------------------------

# >> 4. 문제 해석

# 조건 (time 당 0.5리터 마시기 때문에, 소수점 버림 문제)

# Nathan은 시간당 0.5리터 물을 마심

# 입력: time (시간, 소수 가능)

# 출력: Nathan이 마시는 물의 정수 리터 수, 소수점은 내림 처리

# 예시

# time = 3 → 3 * 0.5 = 1.5 → 내림 → 1

# time = 6.7 → 6.7 * 0.5 = 3.35 → 내림 → 3

# time = 11.8 → 11.8 * 0.5 = 5.9 → 내림 → 5

# 4-1. 내 방법

# def litres(time) :
#     return int(time * 0.5)


4-2. 예시 1

def litres(time) :
    return time // 2

4-3. 예시 2

import math
def litres(time) :
    return math.floor(time * 0.5)

# ----------------------------------------------------------------------------------------------

# >> 5. 문제 해석

# 예시

# 입력: 2 → 출력: 3 (1 + 2 = 3)

# 입력: 8 → 출력: 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36)

# 요구사항 정리

# 입력값은 항상 1 이상의 정수

# 출력값은 1부터 num까지의 합

# 계산 과정은 보여주지 않고 최종 합만 반환


# 5-1. 내 방법

# def summation(num):
    
#     sum = 0
#     for i in range(1, num+1):
#         sum += i
        
#     return sum

5-2. 예시 1

def summation(num):
    return sum(range(1,num+1))

5-3. 예시 2

summation=lambda n:n*-~n>>1


