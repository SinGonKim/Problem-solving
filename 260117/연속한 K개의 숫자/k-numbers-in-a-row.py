
class solution:
    def __init__(self, N, K, B, missing):
        self.N = N
        self.K = K
        self.B = B
        self.missing = missing
        self.ps = [0 for _ in range(N+1)]
    
    def build_prefix_sum(self):
        is_broken = [0 for _ in range(self.N+1)]
        for num in self.missing:
            is_broken[num] = 1
        
        # 2. 1번부터 i번까지 '빠진 숫자가 총 몇 개인가'를 저장 (O(N))
        for i in range(1, self.N + 1):
            self.ps[i] = self.ps[i-1] + is_broken[i]

    def find_min(self):
        # 3. 모든 구간(i ~ i+K-1) 중 빠진 숫자의 개수가 가장 적은 구간 찾기 (O(N))
        min_to_add = self.K
        for i in range(self.K, self.N + 1):
            # i번째에서 끝나는 길이 K인 구간의 누락 개수 = (1~i까지 누락) - (1~i-K까지 누락)
            current_missing = self.ps[i] - self.ps[i - self.K]
            if current_missing < min_to_add:
                min_to_add = current_missing
        return min_to_add

# Please write your code here.
if __name__ == "__main__":
    N, K, B = map(int, input().split())
    missing = [int(input()) for _ in range(B)]
    sol = solution(N, K, B, missing)
    sol.build_prefix_sum()
    print(sol.find_min())