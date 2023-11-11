
class Context():
    counter = 0
    
    def __init__(self,**kwargs):
        self._symbol = kwargs
        self.numCtx = Context.counter
        Context._addCounter()
    
    @property
    def symbols(self):
        return self._symbol
        
    def addSym(self, identifier):
        self._symbol[identifier.name] = identifier
        
    @classmethod
    def _addCounter(cls):
        Context.counter += 1
        

        