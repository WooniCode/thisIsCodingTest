# Q30. 가사 검색
from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro??"]

words_array = [[] for i in range(10001)]
reversed_array = [[] for i in range(10001)]
for i in words:
    word_length = len(i)
    words_array[word_length].append(i)
    reversed_array[word_length].append(i[::-1])

for i in range(10001):
    words_array[i].sort()
    reversed_array[i].sort()

for search_string in queries:
    if search_string[0] != "?":
        length = len(search_string)
        start_string = search_string.replace("?", "a")
        end_string = search_string.replace("?", "z")
        right_index = bisect_right(words_array[length], end_string)
        left_index = bisect_left(words_array[length], start_string)
        print(right_index - left_index)
    else:
        length = len(search_string)
        search_string = search_string[::-1]
        start_string = search_string.replace("?", "a")
        end_string = search_string.replace("?", "z")
        right_index = bisect_right(reversed_array[length], end_string)
        left_index = bisect_left(reversed_array[length], start_string)
        print(right_index - left_index)
