class Call(object):
    def __init__(self, caller_id, caller_name, caller_number, time, reason):
        self.id = caller_id
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time = time
        self.reason = reason
        self.call = {
            "Caller ID": self.id,
            "Caller Name": self.caller_name,
            "Caller Number": self.caller_number,
            "Call Time": self.time,
            "Call Reason": self.reason
        }
        return self.call
    def display(self):
        print self.call
class CallCenter(Call):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)
    def add(self, caller_id, caller_name, caller_number, time, reason):
        super(CallCenter, self).__init__(caller_id, caller_name, caller_number, time, reason)
        self.calls.append(self.call)
        self.queue_size += 1
        return self
    def remove(self):
        self.calls.pop(0)
        return self
    def removePhone(self, phone_number):
        for i in range(0, len(self.calls)):
            if self.calls[i]["Caller Number"] == phone_number:
                self.calls.pop(i)
                self.queue_size -= 1
        return self
    def sortByTime(self):
        from operator import itemgetter
        self.calls.sort(key=itemgetter('Caller ID'))
        return self
    def info(self):
        for i in range(0, len(self.calls)):
            print "#" + str(i+1), self.calls[i]["Caller Name"], "-", self.calls[i]["Caller Number"]
        print "Queue Size: " + str(self.queue_size)
callcenter = CallCenter()
callcenter.add(1,"Isaac","802-380-3564","04:57","blah blah")
callcenter.add(4,"Helen","Helen's Number","5:57","IT struggles")
callcenter.add(2,"Amanda","Amanda's Number","12:57","Python not working")
callcenter.add(5,"Rob","Rob's Number","20:57","just sad")
callcenter.add(3,"Isadsafac","089-asdf-3564","14:57","who knows")
callcenter.removePhone("089-asdf-3564")
callcenter.sortByTime().info()