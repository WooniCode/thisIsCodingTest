# level 2. 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839
import math
from itertools import permutations


def is_prime_number(n):
    k = math.sqrt(n)
    if n < 2:
        return False
    for i in range(2, int(k) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []

    for i in range(1, len(numbers) + 1):
        permu_list = list(map(''.join, permutations(list(numbers), i)))
        for j in list(set(permu_list)):
            if is_prime_number(int(j)):
                answer.append(int(j))
    answer = len(set(answer))
    return answer