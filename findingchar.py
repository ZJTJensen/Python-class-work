word_list = ['hello','world','my','name','is','Anna']
new_list=[]
char = 'o'
num = 0
position = 0
for num in range(0, len(word_list)):
    for position in word_list[num]:
        if position == char:
           
            new_list.append(word_list[num])
            break


print new_list