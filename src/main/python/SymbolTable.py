from ID import *
from Context import Context

class SymbolTable() :
    _instance = None
    _stackCtx = []
    

    def __new__(cls):
        if SymbolTable._instance is None:
            SymbolTable._instance = object.__new__(cls)
            SymbolTable._stackCtx.append(Context())
        return SymbolTable._instance

    def addCtx(self):
        SymbolTable._stackCtx.append(Context())
        
    def delCtx(self):
        SymbolTable._stackCtx.pop()
        
    def allStackCtx(self):
        return SymbolTable._stackCtx
    
    def getLastCtx(self):
        return SymbolTable._stackCtx[-1]
        
    def searchID(self, identifier) -> Context:
        a = SymbolTable.searchLocalID(self, identifier)
        b = SymbolTable.searchGlobalID(self, identifier) 
        if a:
            return a
        if b:
            return b
    
    def searchLocalID(self, identifier) -> Context:
        if identifier in SymbolTable._stackCtx[-1].simbolos:
            return SymbolTable._stackCtx[-1]
    
    
    def searchGlobalID(self, identifier) -> Context:
        for context in SymbolTable._stackCtx[-2::-1]:
            if identifier in context.simbolos:
                return context
    
    def addID(self, identifier):
        SymbolTable._stackCtx[-1].addSym(identifier)

if __name__ == "__main__":
    pass        
        
        
        
            
        
        
        
        
        
    
        
    
    