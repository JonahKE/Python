class Call(object):
    def __init__(self, caller_id, caller_name, caller_number, time, reason):
        self.call = [
            caller_id,
            caller_name,
            caller_number,
            time,
            reason
        ]
    # display: prints all Call attributes.
    def display(self):
        print self.call

class CallCenter(Call):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
    # add: adds a new call to the end of the call list
    def add(self, caller_id, caller_name, caller_number, time, reason):
        super(CallCenter, self).__init__(caller_id, caller_name, caller_number, time, reason)
        self.calls.append(self.call)
        self.queue_size += 1
        return self
    # remove: removes the call from the beginning of the list (index 0)
    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self
    #info: prints the name and phone number for each call in the queue as well as the length of the queue
    def info(self):
        for i in self.calls:
            print i[1], i[2]
        print "Queue size: ", self.queue_size
    # removePhone: find and remove a call from the queue according to the phone number of the caller
    def removePhone(self, phone_number):
        for i in range(self.queue_size-1):
            if self.calls[i][2] == phone_number:
                self.calls.pop(i)
                self.queue_size -= 1
                i -= 1
        return self
    # sortQueue: sorts the calls in the queue according to time of call in ascending order
    def sortQueue(self):
        self.calls = sorted(self.calls, key=lambda x:x[3])
        return self

callcenter = CallCenter()
callcenter.add(1,"Isaac","802-380-3564","05:56","blah blah")
callcenter.add(2,"Helen","Helen's Number","02:57","IT struggles")
callcenter.add(3,"Amanda","Amanda's Number","12:57","Python not working")
callcenter.add(4,"Rob","Rob's Number","01:57","just sad")
callcenter.add(5,"Isadsafac","089-asdf-3564","10:57","who knows")
callcenter.remove().removePhone("Rob's Number").sortQueue().info()