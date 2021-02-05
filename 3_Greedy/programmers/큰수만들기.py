# level 2. 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ''
    while k > 0:
        max_value = -1
        index = 0
        for i in range(k+1):
            if int(number[i]) == 9:
                max_value = int(number[i])
                index = i
                break
            if int(number[i]) > max_value:
                max_value = int(number[i])
                index = i
        k -= index
        answer += number[index]
        number = number[index+1:]
        if k == len(number):
            number = ''
            break
    return answer + number