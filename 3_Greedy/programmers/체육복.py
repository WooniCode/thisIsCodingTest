# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

def solution(n, lost, reserve):
    losts = len(lost)
    lost.sort()
    reserve.sort()
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                reserve[j] = 1e9
                lost[i] = -1e9
                losts -= 1
                break
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if abs(lost[i] - reserve[j]) == 1:
                reserve[j] = 1e9
                lost[i] = -1e9
                losts -= 1
                break
    return (n - losts)