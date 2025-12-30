N = int(input())

# Please write your code here.N = int(input())
numbers = list(map(int, input().split()))

# 1. 짝수와 홀수의 개수를 카운트합니다.
even = 0
odd = 0
for x in numbers:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

# 2. 규칙에 따라 계산합니다.
# odd > even 인 경우와 even >= odd 인 경우로 나누어 생각하면 간단합니다.

if even > odd:
    # 짝수가 훨씬 많은 경우: 짝, 홀, 짝, 홀 ... 짝 순서로 배치하고
    # 남은 짝수들은 기존의 짝수 그룹에 다 몰아넣어도 합의 성질이 변하지 않습니다.
    # 최대 그룹 수는 (홀수 개수 * 2 + 1)이 됩니다.
    print(odd * 2 + 1)

elif even == odd:
    # 개수가 같으면 짝, 홀, 짝, 홀... 순서로 모두 1개씩 묶을 수 있습니다.
    print(even + odd)

else: # odd > even
    # 홀수가 더 많은 경우: 짝수들을 먼저 짝수 그룹으로 다 쓰고 남은 홀수들로 처리합니다.
    ans = even * 2 # (짝, 홀) 쌍을 even만큼 만듦
    rem_odd = odd - even # 남은 홀수 개수
    
    # 남은 홀수들은 [짝(홀+홀), 홀(홀)] 세트로 묶어야 패턴이 유지됩니다.
    # 즉, 홀수 3개가 모여야 '짝, 홀' 그룹 2개를 추가할 수 있습니다.
    ans += (rem_odd // 3) * 2
    
    # 3개로 나누고 남은 홀수 처리
    if rem_odd % 3 == 1:
        # 홀수가 1개 남으면, 앞의 홀수 그룹에 합쳐야 하므로 그룹 수가 1개 줄어듭니다.
        ans -= 1
    elif rem_odd % 3 == 2:
        # 홀수가 2개 남으면, 두 개를 합쳐서 하나의 짝수 그룹을 더 만들 수 있습니다.
        ans += 1
        
    print(ans)