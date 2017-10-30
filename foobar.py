#ok world to day we need to do 2 thinks
#prime numbers=



#perfect squares = math.sqrt()== .00
for val in range(100, 1000):
    checker = False
    counter = 0
    for i in range(2, val):
        
        counter = counter + 1
        if val % i == 0:
            break
        elif counter == (val -2):
            print "Foo" + str(val)
            checker = True

    for j in range(2, val):
        if j*j != val:
            continue
        elif j*j == val:
            print "bar"
            checker = True

    if checker == False:
        print "foo bar"
    else:
        checker  = False
        counter = 0
        
