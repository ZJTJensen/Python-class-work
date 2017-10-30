
print "x 1 2 3 4 5 6 7 8 9 10 11 12"

for i in range (1, 13):
    mathbox ="{} ".format(i)
    for j in range(1,13):
        mathbox +="{} ".format(i*j)
    print mathbox


# i = 0
# l =0
# q =0
# row = 1
# while i< len(row1):
#     for q in row1:
#         print row * row1[l]
#         l=l+1
#     i=i+1
#     row = row+1


