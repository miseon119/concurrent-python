class Event(object):
  
    def __init__(self):
        self.__eventhandlers = []
  
    def __iadd__(self, handler):
        self.__eventhandlers.append(handler)
        return self
  
    def __isub__(self, handler):
        self.__eventhandlers.remove(handler)
        return self
  
    # def __call__(self, *args, **keywargs):
    #     for eventhandler in self.__eventhandlers:
    #         eventhandler(*args, **keywargs)
    def fire(self, *args, **keywargs):
        for eventhandler in self.__eventhandlers:
            eventhandler(*args, **keywargs)            

class AbcEvent(object):
    def __init__(self):
        self.OnChange=Event()
          
    def fire(self, udata):
        self.OnChange.fire(udata)
          
    def AddSubscribersForEvent(self,objMethod):
        self.OnChange += objMethod
          
    def RemoveSubscribersForEvent(self,objMethod):
        self.OnChange -= objMethod            

def test(msg):
    print('msg = ', msg)
def make_something(senderEvent):
    senderEvent.fire('hello')
    
if __name__ == "__main__":
    sender_event = AbcEvent()
    sender_event.AddSubscribersForEvent(test)
    make_something(sender_event)
    
