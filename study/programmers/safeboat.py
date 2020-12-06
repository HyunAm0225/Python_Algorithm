# 구명보트 문제
# 그리디
from collections import deque
people = list(map(int, input().split()))
limit = int(input())
count = 0
people.sort()
people = deque(people)
# 사람들을 정렬한다
while people:
    left = 0
    right = len(people)-1
    if people[left] + people[right] > limit:
        # 혼자밖에 못탄다
        people.pop()
        # 보트 사용 했으니까 카운트 플러스
        count += 1
        right -= 1
        print(people)
    else:
        people.pop()
        try:
            people.popleft()
            left += 1
            right -= 1
            count += 1
        except:
            count += 1
            break
        print(people)

print(count)
