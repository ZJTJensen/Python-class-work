class MathDojo(object):
    def __init__(self):
        self.all = 0
    def add(self, *y):

        sum = 0
        for i in range (0, len(y)):
            if (type(y[i])==list or type(y[i])==tuple):
                for j in range(0, len(y[i])):
                    sum = sum + y[i][j]
                    # self.all += sum
            else:
                sum = sum + y[i]
        self.all += sum 
        
        return self

    def subtract(self, *y):
        sum = 0
        for i in range (0, len(y)):
            if (type(y[i])==list or type(y[i])==tuple):
                    for j in range(0, len(y[i])):
                        sum = sum + y[j][j]
                    # self.all -= sum
            else:
                sum = sum + y[i]
        self.all -= sum
        return self






md = MathDojo()

print md.add(2).add(2,5).subtract(3,2).all
# print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2]).all