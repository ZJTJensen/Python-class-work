class Call(object):
    def __init__(self, u_id, name, p_number, time_of_call, reason):
        self.u_id = u_id
        self.name = name
        self.p_number=p_number
        self.time_of_call=time_of_call
        self.reason=reason
    def display_all(self):
        print self.u_id  
        print self.name  
        print self.p_number 
        print self.time_of_call
        print self.reason
        return self


class CallCenter(object):
    def __init__(self):
        self.calls=[]
        self.total = 0
    def add(self, u_id, name, p_number, time_of_call, reason):
        self.total +=1 
        new_call = Call(self.total, name, p_number, time_of_call, reason)
        self.calls.append(new_call)
        return self   
    def remove(self):
        del self.calls[:1]
        return self
    def info(self):
        for i in range(len(self.calls)):
            print self.calls[i].name
            print self.calls[i].p_number
            print self.calls[i].time_of_call
            print self.calls[i].reason
        print len(self.calls)  
        return self
    def flipflop(self):
        for i in range(len(self.calls)):
            j = len(self.calls)-1
            while j>i:
                if self.calls[j].time_of_call>self.calls[i].time_of_call:
                    temp = self.calls[j]
                    self.calls[j]=self.calls[i]
                    self.calls[i]=temp
                j = j - 1

    def splice(self, splice):
        for num in range (len(self.calls)):
            if self.calls[num].p_number == splice:
                del self.calls[num]
                break

call= CallCenter()
call.add("1", "John herman", "555-555-5555", 1251, "Wants to be burried with his money").add("2", "John herman", "311-346-3515", 1252, "Wants to be burried with his money").add("2", "John herman", "311-346-3515", 955, "Wants to be burried with his money").info()
# call.splice("555-555-5555")

call.flipflop()
call.info()






# class CallCenter(Call):
#     def __init__(self, name, p_number, time_of_call):
#         super(CallCenter, self).__init__( u_id, name, p_number, time_of_call, reason)
#         self.calls = []
#         self.queue = len(calls)
        
#     def add(self, u_id, name, p_number, time_of_call, reason):
#         self.calls.append(Call)
#         return self   
#     def remove(self):
#         del self.calls[:1]
#         return self
#     def info(self):
#         print self.name
#         print self.p_number
#         print self.queue
#         return self


