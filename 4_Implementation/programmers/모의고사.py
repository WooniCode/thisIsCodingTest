# level 1. 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []

    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score1, score2, score3 = 0, 0, 0

    for i in range(len(answers)):
        if person1[i % 5] == answers[i]:
            score1 += 1
        if person2[i % 8] == answers[i]:
            score2 += 1
        if person3[i % 10] == answers[i]:
            score3 += 1

    maxVal = max(score1, score2, score3)
    if score1 == maxVal:
        answer.append(1)
    if score2 == maxVal:
        answer.append(2)
    if score3 == maxVal:
        answer.append(3)

    return answer