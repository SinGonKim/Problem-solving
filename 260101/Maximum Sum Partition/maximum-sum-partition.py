n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

total_sum = sum(arr)

offset = total_sum

dp = [-1] * (2*total_sum + 1)
dp[total_sum] = 0
current_limit = 0
for x in arr:
    # Create a copy to ensure we use values from the previous iteration only
    next_dp = dp[:]
    
    # We only need to iterate through the range of differences possible so far
    for diff in range(-current_limit, current_limit + 1):
        prev_sum_a = dp[diff + offset]
        
        if prev_sum_a == -1:
            continue
        
        # Case 1: Add x to Group A
        # New diff: (sumA + x) - sumB = diff + x
        if next_dp[diff + x + offset] < prev_sum_a + x:
            next_dp[diff + x + offset] = prev_sum_a + x
        
        # Case 2: Add x to Group B
        # New diff: sumA - (sumB + x) = diff - x
        if next_dp[diff - x + offset] < prev_sum_a:
            next_dp[diff - x + offset] = prev_sum_a
            
        # Case 3: Add x to Group C
        # Difference and sumA don't change (already handled by next_dp = dp[:])
    
    dp = next_dp
    current_limit += x
    
# The answer is the max sum of A when the difference (sumA - sumB) is 0
print(dp[offset])