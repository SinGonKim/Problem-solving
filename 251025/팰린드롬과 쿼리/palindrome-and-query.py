import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 1. 입력 받기
n, q = map(int, input().split())
# 문자열 s를 0-based 인덱스로 사용하기 위해 앞에 공백 추가
s = " " + input().strip() 

# 해싱을 위한 설정
P = 31  # 해시 베이스 (소수)
M = 10**9 + 9  # 모듈러 (큰 소수)

# 2. 전처리 (O(N) 시간, O(N) 메모리)

# 2-1. 해시 계산에 필요한 P의 거듭제곱 미리 계산
powers = [1] * (n + 1)
for i in range(1, n + 1):
    powers[i] = (powers[i - 1] * P) % M

# 2-2. 정방향(prefix) 해시 계산
# pre_hash[i] = s[1...i]의 해시값
pre_hash = [0] * (n + 1)
for i in range(1, n + 1):
    pre_hash[i] = (pre_hash[i - 1] * P + ord(s[i])) % M

# 2-3. 역방향(suffix, reversed prefix) 해시 계산
# rev_hash[i] = s[n...n-i+1]의 해시값 (즉, 뒤집은 문자열의 1...i 해시)
rev_hash = [0] * (n + 1)
for i in range(1, n + 1):
    # s[n-i+1]이 뒤에서 i번째 문자 (s[n], s[n-1], ...)
    rev_hash[i] = (rev_hash[i - 1] * P + ord(s[n - i + 1])) % M

# 3. 해시값 추출 함수 (O(1))

def get_pre_hash(a, b):
    """ s[a...b]의 정방향 해시값을 반환 (1-based 인덱스) """
    hash_val = (pre_hash[b] - (pre_hash[a - 1] * powers[b - a + 1]) % M + M) % M
    return hash_val

def get_rev_hash(a, b):
    """ s[a...b]의 역방향 해시값을 반환 (1-based 인덱스) """
    # s[a...b]의 역방향은 뒤집은 문자열에서
    # (n-b+1)번째부터 (n-a+1)번째까지의 문자열과 같음
    rev_a = n - b + 1
    rev_b = n - a + 1
    hash_val = (rev_hash[rev_b] - (rev_hash[rev_a - 1] * powers[rev_b - rev_a + 1]) % M + M) % M
    return hash_val

# 4. 쿼리 처리 및 결과 저장
results = []
for _ in range(q):
    a, b = map(int, input().split())
    
    # 정방향 해시와 역방향 해시가 같으면 팰린드롬
    if get_pre_hash(a, b) == get_rev_hash(a, b):
        results.append("Yes")
    else:
        results.append("No")

# 5. 결과 한 번에 출력
print("\n".join(results))