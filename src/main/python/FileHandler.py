class FileHandler:
    def __init__(self, name):
        self.name = name
        
    def __enter__(self):
        self.name = open(self.name, 'a')
        return self.name
    
    def __exit__(self, exceptionType, exceptionValue, trace):
        if self.name:
            self.name.close()
            
    