expression = input()

# Please write your code here.
variables = tuple(set(expression[::2]))
calculations = expression[1::2]
terms = expression[::2]

cases = []

numbers = [1, 2, 3, 4]*len(variables)
from itertools import combinations
import sys
answer = -sys.maxsize
for comb in combinations(numbers, len(variables)):
    Z = dict(zip(variables, comb))
    prev_term = Z[terms[0]]
    for idx, cal in enumerate(calculations):
        if cal == '-':
            prev_term -= Z[terms[idx+1]]
        elif cal == '+':
            prev_term += Z[terms[idx+1]]
        elif cal == '*':
            prev_term *= Z[terms[idx+1]]
    answer = max(answer, prev_term)
print(answer)
        
