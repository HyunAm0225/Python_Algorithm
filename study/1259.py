# import sys
# input = sys.stdin.readlinex

def check_palindrome(s):
    if s[0] == '0':
        print("no")
    elif s==s[::-1]:
        print("yes")
    else:
        print("no")


while True:
    s = input()
    if s == '0':
        break
    else:
        check_palindrome(s)