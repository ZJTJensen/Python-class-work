def odd_even(a, b):
    for i in range(a, b):
        if i % 2 == 0 and i != 1:
            print "Number is "+str(i)+". This is an even number."
        else:
             print "Number is "+str(i)+". This is an odd number."
odd_even(1, 2000)

def multiply(listy):
    i=0
    b=[]
    for i in listy:
        b.append(i*5)
    print b


multiply(listy=[2,4,10,16])

def hackerman(arr, num):
    i=0
    z=[]
    while i < len(arr):
        z.append(arr[i]*num)
        i = i+1
    print z

    container = []
    for element in z:
        temp_list=[]

        for i in range (element):
            temp_list.append(1)
        container.append(temp_list) 
    print container


#bad code

    # new_list = []
    # i=0
    # j=0
    # ones=[] 
    # while i < z[j]:  #0 < 5
        
    #     ones.append(1) #[1,1,1,1,1]
    #     if len(ones) == z[j]:
    #         new_list.append(ones)
    #         ones=[]
    #         j=j+1
    #         i=0
    #         continue
    #     i = i+1
        




    # print new_list


hackerman([1,2,3],5)










