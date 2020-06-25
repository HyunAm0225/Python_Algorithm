'''
문제 링크 : https://edu.goorm.io/learn/lecture/15551/%EC%9C%84%ED%81%B4%EB%A6%AC-%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%8B%9C%EC%A6%8C2-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%8C%80%EB%B9%84-%EC%9E%85%EB%AC%B8%ED%8E%B8/lesson/736435/09%EC%9B%94-1%EC%A3%BC%EC%B0%A8-%ED%99%98%EC%83%81%EC%9D%98-%EC%A1%B0%ED%95%A9-2
'''
n, s = map(int, input().split())
arr = list(map(int,input().split()))
hong = arr.pop(0)
ans = 0

# 비트마스킹 

def powerset(s):
    masks = [1 << i for i in range(len(s))]
    for i in range(1<<len(s)):
        yield [ss for ss,mask in zip(s,masks) if mask & i]

for power in powerset(arr):
    if sum(power)+hong == s:
        ans += 1
print(ans)
