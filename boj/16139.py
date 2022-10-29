import sys
input = sys.stdin.readline

S = input().strip()
size = len(S)
q = int(input())
psum = {} #문자열 분석집합

for _ in range(q):
    spell, start, end = input().split()
    start, end =int(start), int(end)
    if spell not in psum:
        psum[spell] = [0] #0번째를 0으로 만든다음
        [psum[spell].append(psum[spell][i-1] + (spell==S[i-1])) for i in range(1, size+1)] #문자열을 하나씩 뽑아가며 i번째 spelling 리스트칸에 그 전까지 합에 하나를 더해 넣는다.
    print(psum[spell][end+1]-psum[spell][start]) #찾는 스펠 끝번째에서 시작점-1 빼주면 된다.
