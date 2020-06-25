# 0~4번째 항목 1(4)1(3)1(2)1(1)1(0)
test = 0b11111

print(bin(test))

# 3번째 항목 빼기
test &= ~(1<<3)
print(bin(test)) # 10111 출력

