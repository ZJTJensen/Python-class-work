words = "It's thanksgiving day. It's my birthday,too!"
words.find('day')
string = words.replace('day', 'months')
print string

x=[2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x)-1]

new_str=[x[0], x[len(x)-1]]
print new_str

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x

num= len(x)/2
new_list =x[:num]
print new_list

y=0
while y <  num:
    x.pop(0)
    y = y +1

print x

x.insert(0,new_list)
print x