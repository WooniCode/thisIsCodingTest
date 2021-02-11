# level 2. 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    sumValue = (brown + 4) // 2
    for i in range(1, sumValue):
        x = sumValue - i
        y = i
        if x < y:
            break
        if x - 2 > 0 and y - 2 > 0 and (x-2) * (y-2) == yellow:
            answer.append(x)
            answer.append(y)
            break
    return answer