'''
1,2,4,8,16,....

2^k의 수로 나누어지는 자연수 확인

문제 링크 : https://edu.goorm.io/learn/lecture/15551/%EC%9C%84%ED%81%B4%EB%A6%AC-%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%8B%9C%EC%A6%8C2-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%8C%80%EB%B9%84-%EC%9E%85%EB%AC%B8%ED%8E%B8/lesson/736435/09%EC%9B%94-1%EC%A3%BC%EC%B0%A8-%ED%99%98%EC%83%81%EC%9D%98-%EC%A1%B0%ED%95%A9-2
'''
# 방법 1(while 문 이용)
# x = int(input())

# while x%2 == 0:
# 	x /= 2

# if(x==1): print("Yes")
# else: print("No")

# 방법 2(shift연산자 이용)
x = int(input())

if(x==(x&(-x))): print("Yes")
else: print("No")