
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


