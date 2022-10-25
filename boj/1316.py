import sys
input = sys.stdin.readline
n = int(input())
group_word = 0 #그룹월드 개수 세기
for _ in range(n):
    word = str(input())
    error = 0
    for index in range(len(word)-1):
        if word[index] != word[index+1]:#그룹월드 연속알파벳이 끝나는 순간
            new_word = word[index+1:] #앞에 알파벳을 지워버렸을 때 뒤에 그 알파벳이 나오면 안된다.
            if new_word.count(word[index])>0: #나오게 되면
                error += 1 #에러가 증가해 그룹단어가 될 수 없다.
    if error == 0:
        group_word += 1
print(group_word)
