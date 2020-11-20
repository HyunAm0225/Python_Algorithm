# 입력 값 받기
number = input()
k = int(input())

stack = [number[0]]
# 현재 숫자 길이 - 뺄 숫자 개수 = 정답 숫자 길이

# 숫자중 처음을 stack에 넣어놔서 1부터 시작하게 지정해 줍니다.
for i in number[1:]:
    # 만약 스택이 0보다 크고 i가 스택에서 제일 위에 있는 값보다 크고 k가 0보다 크면 실행
    while len(stack) > 0 and stack[-1] < i and k > 0:
        # 숫자 한개를 뺐으니까 k에다가 -1진행
        k -= 1
        # 스택에서 제일 뒷부분 pop 시킨다.
        stack.pop()
    # 스택에 값을 넣어준다
    stack.append(i)
# 만약 충분히 제거 되지 않았을 수도 있으니까 제거 남은 숫자 만큼 제거 해줍니다.
if k != 0:
    stack = stack[:-k]

# 출력
print(''.join(stack))
