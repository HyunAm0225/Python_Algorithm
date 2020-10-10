# 9012 
# 괄호
# 스택문제

# 테스트 케이스의 숫자를 입력받음
t = int(input())
ans = []
data = []
def check_vps(stack_list):
    # pop 한 괄호를 담을 list
    temp_list = []
    temp_list.append(stack_list.pop())
    for i in range(len(stack_list)):
        # temp_list 비어있을 경우 append
        if not temp_list:
            temp_list.append(stack_list.pop())
            
        # temp에는 ), stackList 는 (
        elif (temp_list[-1] == ')' and stack_list[-1] =='('):
            temp_list.pop()
            stack_list.pop()
        else:
            temp_list.append(stack_list.pop())
    if not temp_list:
        # print(temp_list)
        return "YES"
    else:
        # print(temp_list)
        return "NO"
for _ in range(t):
    data = list(input())
    ans.append(check_vps(data))


# 결과값 출력
for i in ans:
    print(i)
