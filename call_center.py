

class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def display(self):
        print(self.id)
        print(self.name)
        print(self.number)
        print(self.time)
        print(self.reason)


class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.size = len(self.calls)
    def add(self, call):
        self.calls.append(call)
    def remove(self):
        del self.calls[0]
    def info(self):
        print(len(self.calls))
        for c in self.calls:
            print(c.name)
            print(c.number)






