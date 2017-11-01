class Patient(object):
    def __init__(self, p_id, name, Allergies):
        self.p_id = p_id
        self.name = name
        self.Allergies = Allergies
        # self.Bed_Num = Bed_Num

class hospital(object):
    def __init__(self):
        self.patients =[]
        self.hospitalName = "Hells Hospital"
        self.capacity = 100
        self.total = 0
        self.Beds =[]
        for val in range(self.capacity):
            self.Beds.append(False)
    def admit(self, p_id, name, Allergies):
        if len(self.patients) <= self.capacity:
            for Beds in range (len(self.Beds)):
                if not self.Beds[Beds]:
                    self.Beds[Beds]= True
                    New_Bed=Beds
                    break

            self.total +=1 
            new_patients= Patient(self.total, name, Allergies)
            new_patients.Bed_Num = New_Bed
            self.patients.append(new_patients)
            print "Welcome to ", self.hospitalName, "!"
            
        else:
            print "sorry boi you may have health issues"
        return self   
    def info(self):
        print self.Beds
        return self

   
    def discharge(self, pid):
        for num in range(len(self.patients)):
            if str(self.patients[num].p_id) == pid:
                self.Beds[self.patients[num].Bed_Num] = False
                del self.patients[num]


                   
                    
                break
        return self
Pat=hospital()
Pat.admit("1", "Mary Sue", "None").discharge("1").info()