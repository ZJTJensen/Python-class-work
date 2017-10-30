list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
val = 0
yes = 0

while val < len(list_one):
    if list_one[val] == list_two[val]:
        val=val+1
        continue
    elif list_one[val] != list_two[val]:
        print "not the same"
        yes = 1
        break

if yes == 0:
    print "They are the same"
# 111111211
# 111111111