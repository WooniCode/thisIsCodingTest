# level 2. H-index
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse = True)
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i
    return len(citations)