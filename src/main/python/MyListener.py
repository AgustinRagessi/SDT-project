from antlr4.tree.Tree import TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from SymbolTable import SymbolTable
from ID import *
from Context import *
from Util import *

class MyListener(compiladoresListener) : 
    SymbolTable = SymbolTable()
    
 # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Now entering: enterPrograma")
                
    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print(self.SymbolTable.stackCtx)

    def exitBloque(self, ctx: compiladoresParser.BloqueContext):
        self.SymbolTable.delCtx()
        print("Now leaving: exitBloque")
        
    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        self.SymbolTable.addCtx()
        print("Now entering: enterBloque")
    
    def exitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        dataType = str( ctx.getChild(0).getText() )
        data = ctx.getText()[len(dataType):]
        idList = Util.getIDAmount(data)    
         
        for i in idList:
            identifier = Variable(i, dataType)
            if Util.verifyInit(data) == True:
                identifier._initialized = True
            
            if self.SymbolTable.searchLocalID(identifier.name):
                print("Symbol has not been added")
            else:
                self.SymbolTable.addID(identifier)
                print("Symbol has been added")
    
    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        pass
        #NO OLVIDARSE DE TERMINAR ESTO DESPUES CUANDO HAYAN MENOS MATERIAS 

    def exitFunctprototype(self, ctx: compiladoresParser.FunctprototypeContext):
        pass
        #NO OLVIDARSE DE TERMINAR ESTO DESPUES CUANDO HAYAN MENOS MATERIAS 

    def exitFunctdef(self, ctx: compiladoresParser.FunctdefContext):
        pass
        #NO OLVIDARSE DE TERMINAR ESTO DESPUES CUANDO HAYAN MENOS MATERIAS 
            
    def exitFunctcall(self, ctx: compiladoresParser.FunctcallContext):
        pass
        #NO OLVIDARSE DE TERMINAR ESTO DESPUES CUANDO HAYAN MENOS MATERIAS 
    
        
            
        
    
        

        
