from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser
from antlr4 import *
from Temporals import *
from FileHandler import *

class MyVisitor(compiladoresVisitor):
    
    temps = Temporals()
    
    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Now visiting: visitPrograma")
        return None
    
    def visitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        self.visitDeclaracion(ctx.getChild(2))
        return self.visitChildren(ctx)
    
    ##TERIMNAR DESPUES DE TRABAJAR CON LOS INGENIEROS DE GRUPO