
x=['magical unicorn', 19, 'hello', 98.98, 'world']
trueint=0
truestr=1

if isinstance(x,list):
    sum = 0
    string = ''
    concatination =''
    for stuff in x:
        if isinstance(stuff, int):
            sum = sum + stuff 
            trueint=1
        elif isinstance(stuff, str):
            string = string+ ' ' + stuff
            truestr=1


    print sum
    print string
    if truestr==1 and trueint==0:
        print 'The list you entered is of string type'
    elif truestr==0 and trueint==1:
        print 'The list you entered is of interger type'
    else:
        print "It is a combined list"
