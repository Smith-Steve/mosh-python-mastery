from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    #This is a custom exception that inherits from the general class exception
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False
    
    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.") 
        self.opened = True
    
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False
    
    @abstractmethod #This enforces this body of code across all inheritors of this class.
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading Data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading Data from a network")

class MemoryStream(Stream):
    pass
#We cannot instantiate a base class.
# stream = Stream()



#There is no way to enforce a common interface across all of these streams.
#An abstract base class has the purpose of providing common code to all objects that inherit for it.