import heapq
scoville = list(map(int, input().split()))
h = []
k = int(input())
count = 0
heapq.heapify(scoville)
while scoville:
    if scoville[0] < k:
        try:
            print(scoville)
            new_scoville = heapq.heappop(scoville) + heapq.heappop(scoville)*2
            heapq.heappush(scoville, new_scoville)
            count += 1
        except:
            count = -1
    else:
        break
print(scoville)
print(count)
