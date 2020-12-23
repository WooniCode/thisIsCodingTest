# 7-4. 한 줄 입력받아 출력하는 소스코드
# - 입력 데이터가 많은 문제에 input() 대신 readline() 함수를 사용한다.

import sys
# 하나의 문자열 데이터 입력 받기
input_data = sys.stdin.readline().rstrip()

print(input_data)