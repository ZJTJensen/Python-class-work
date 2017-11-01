import random
def grader(add):
    for add in range (0, add):
        grade= random.randint(60, 101)
        if grade >= 60 and grade <=69:
            print "Score: ", grade,"; Your grade is D"
        elif grade >= 70 and grade <=67:
            print "Score: ", grade,"; Your grade is C"
        elif grade >= 80 and grade <=89:
            print "Score: ",grade,"; Your grade is B"
        elif grade >= 90 and grade <=100:
            print "Score: ",grade,"; Your grade is A"

print grader(10)