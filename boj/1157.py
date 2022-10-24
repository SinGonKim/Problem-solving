word = input().lower() #주어진 문자 소문자로 변환
word_list = list(set(word)) #주어진 문자에 들어간 알파벳 모음(중복제외)
cnt = []
for i in word_list: #중복되지 않게 알파벳을 하나씩 뽑아
    count = word.count(i) #word_list에 있는 한 문자가 word에 몇개가 있는지 count해서
    cnt.append(count) #cnt 리스트에 집어 넣는다.
if cnt.count(max(cnt)) >=2: #max가 2개 이상이면 ?을 출력
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper()) #아니면 대문자로 그 알파벳 출력
