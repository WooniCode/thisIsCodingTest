# Q12. 기둥과 보 설치

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 기둥일 경우
            # 바닥 위 혹은 보의 한쪽 긑부분 위 혹은 다른 기둥 위이면 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1: # 설치된 것이 보일 경우
            # 한쪽 끝부분이 기둥 위 혹은 양쪽 끝부분이 다른 보와 동시에 연결이라면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
        return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제한 다음
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 불가능할 경우 구조물 다시 설치
        elif operate == 1: # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치한 다음
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 불가능할 경우 구조물 다시 삭제
    return sorted(answer)