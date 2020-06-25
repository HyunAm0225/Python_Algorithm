'''
중복된 숫자 검사 후 
중복된 값 제거 한 count 출력
문제 링크 : https://edu.goorm.io/learn/lecture/15551/%EC%9C%84%ED%81%B4%EB%A6%AC-%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%8B%9C%EC%A6%8C2-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%8C%80%EB%B9%84-%EC%9E%85%EB%AC%B8%ED%8E%B8/lesson/726506/09%EC%9B%94-1%EC%A3%BC%EC%B0%A8-%EC%8B%9C%EA%B3%B5%EC%9D%98-%ED%8F%AD%ED%92%8D-%EC%86%8D%EC%9C%BC%EB%A1%9C-1

'''

team = list(map(int,input().split()))
my = list(map(int,input().split()))
count = 0
for i in team:
	if i in my:
	  count+=1
print(len(my)-count)