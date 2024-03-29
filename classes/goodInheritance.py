class InvalidOperationError(Exception):
    #This is a custom exception that inherits from the general class exception
    pass

class Stream:
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

class FileStream(Stream):
    def read(self):
        print("Reading Data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading Data from a network")