import sys
sys.setrecursionlimit(10*6)
def is_possible(sequence):
    """
    현재 수열이 가능한 수열인지 확인합니다.
    새로 추가된 마지막 문자를 기준으로 인접한 두 부분 수열을 비교합니다.
    """
    length = len(sequence)
    # 비교할 부분 수열의 길이를 1부터 전체 길이의 절반까지 늘려가며 확인
    for i in range(1, length // 2 + 1):
        # 인접한 두 부분 수열 추출
        right = sequence[length - i:]
        left = sequence[length - 2*i : length - i]
        
        if left == right:
            return False
    return True

def solve(current_seq, n):
    # 목표 길이에 도달하면 해당 수열을 출력하고 프로그램 종료
    if len(current_seq) == n:
        print(current_seq)
        sys.exit(0) # 가장 사전순으로 앞선 것을 찾았으므로 즉시 종료

    # 사전순으로 앞선 것부터 시도 (4 -> 5 -> 6)
    for next_digit in ["4", "5", "6"]:
        candidate = current_seq + next_digit
        if is_possible(candidate):
            solve(candidate, n)
    

if __name__ == "__main__":
    n = int(input())
    solve("", n)