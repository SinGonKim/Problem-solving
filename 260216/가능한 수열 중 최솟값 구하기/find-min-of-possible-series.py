
# Please write your code here.

def solution(num, cnt):
    if cnt == 0:
        print(num)
        return
    
    for c in ["4", "5", "6"]:
        candidate = num + c
        for l in range(1, len(candidate)//2+1):
            if candidate[len(candidate)-l:] == candidate[len(candidate)-2*l:len(candidate)-l]:
                break
        else:
            solution(candidate, cnt-1)
            break

    

if __name__ == "__main__":
    n = int(input())
    solution("4", n-1)