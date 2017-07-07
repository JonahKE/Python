class Patient(object):
    def __init__(self, id_num, name, bed_num, *allergies):
        self.bed = bed_num
        self.id = id_num
        self.name = name
        self.allergies = allergies

class Hospital(Patient):
    def __init__(self, hospital_name, capacity):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity
    def admit(self, id, name, *allergies):
        super(Hospital, self).__init__(id, name, 0, *allergies)
        if len(self.patients) >= self.capacity:
            print "The hospital is full"
        else:
            if len(self.patients) == 0:
                self.bed_num = 1
            else:
                self.bed_num = 1
                for i in range(len(self.patients)):
                    if self.patients[i][3] != self.bed_num:
                        pass
                    else:
                        self.bed_num += 1
            print self.name, "admitted to", self.hospital_name, "in bed: ", self.bed_num
            self.patients.append([self.id,self.name,self.allergies,self.bed_num])
        return self
    def discharge(self, patient_name):
        for i in range(len(self.patients)-1):
            if self.patients[i][1] == patient_name:
                print self.patients[i][1], "discharged from bed ", self.patients[i][3]
                self.patients.pop(i)
        return self
    def info(self):
        print self.patients

hospital1 = Hospital("Holy Cross", 1000)
hospital1.admit(1,"Helen","Bee Stings")
hospital1.admit(2,"Isaac","Bee Stings")
hospital1.admit(3,"Ashley","Bee Stings")
hospital1.admit(4,"Bob","Bee Stings")
hospital1.discharge("Isaac")
hospital1.admit(5,"Alex","Bee Stings")
hospital1.admit(6,"Jess","Bee Stings")
hospital1.info()