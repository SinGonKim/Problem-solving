import sys
input = sys.stdin.readline
def solve():
    for char in s:
        stack.append(char)
        if char == last_Char and ''.join(stack[-l:]) == d:
            del stack[-l:]
    answer = ''.join(stack)
    if answer =='':
        print("FRULA")
    else:
        print(answer)
    return
if __name__=="__main__":
    s = str(input().strip())
    d = str(input().strip())
    last_Char = d[-1]
    stack = [] #스텍으로 안하고 while구문으로 s문자열 안에 d가 있는지 없는지로 찾을 수 있지만 시간초과가 된다.
    l = len(d)
    solve()
