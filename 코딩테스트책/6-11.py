# 성적이 낮은 순서로 학생 출력하기

N = int(input())

array = []
for i in range(N):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))

array = sorted(array, key=lambda x : x[1])

# 정렬이 수행된 결과를 출력 
for student in array:
    print(student[0],end=' ')