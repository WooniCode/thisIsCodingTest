# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    idx, cnt = 0, 0
    distance_list = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]

    while True:
        cnt += distance_list[idx]
        distance_list[idx] = 0

        if sum(distance_list) == 0:
            break
        left, right = 1, 1

        while distance_list[idx - left] == 0:
            left += 1
        while distance_list[idx + right] == 0:
            right += 1

        cnt += left if left < right else right
        idx += -left if left < right else right
    return cnt