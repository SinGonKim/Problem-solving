N = str(input())
F = int(input())
minimum = int(N[:-2]+'00')
r = minimum%F
if r==0:
    answer = 0
else:
    answer = (minimum  + (F-r))%100
if answer <10:
    answer = '0'+str(answer)
print(answer)
