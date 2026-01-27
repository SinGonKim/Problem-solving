m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.   1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_m = sum(num_of_days[:m1])
start = start_m + d1

end_m = sum(num_of_days[:m2])
end = end_m + d2
print(end-start+1)