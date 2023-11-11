from abc import ABC,abstractclassmethod

class ID(ABC):
    
    @property
    def __init__(self, name, dataType, initialized, accessed):
        self._name = name
        self._dataType = dataType
        self._initialized = initialized
        self._accessed = accessed
    
    @property    
    def getName(self):
        return self._name
    
    @property
    def getDataType(self):
        return self._dataType
    
    @property
    def getInitialized(self):
        return self._initialized
    
    @property
    def getAccessed(self):
        return self._accessed
    
    def setName(self, name):
        self._name = name
    
    def setDataType(self, dataType):
        self._dataType = dataType
    
    def setInitialized(self, initialized):
        self._initialized = initialized
    
    def setAccessed(self, accessed):
        self._accessed = accessed
        
    def __eq__(self, other) -> bool:
        if isinstance(other, ID):
            return other._name == self._name and other._dataType == self._dataType
    

class Variable(ID):
    pass

class Function(ID):
    def __init__(self, name, dataType, args, initialized=False, accessed=False):
        super().__init__(name, dataType, initialized, accessed)
        self._args = list(args)
        
    def __eq__(self, other) -> bool:
        return super().__eq__(other) and other.args == self.args
    
    @property
    def args(self):
        return self._args
    