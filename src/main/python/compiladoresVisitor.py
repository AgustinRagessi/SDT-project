# Generated from /home/curso/proyectoDHS/src/main/python/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#definicion.
    def visitDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#lista_var.
    def visitLista_var(self, ctx:compiladoresParser.Lista_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#while_stmt.
    def visitWhile_stmt(self, ctx:compiladoresParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#ret.
    def visitRet(self, ctx:compiladoresParser.RetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#if_stmt.
    def visitIf_stmt(self, ctx:compiladoresParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#for_stmt.
    def visitFor_stmt(self, ctx:compiladoresParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#opar.
    def visitOpar(self, ctx:compiladoresParser.OparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#logicoperators.
    def visitLogicoperators(self, ctx:compiladoresParser.LogicoperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#oplo.
    def visitOplo(self, ctx:compiladoresParser.OploContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#logexpression.
    def visitLogexpression(self, ctx:compiladoresParser.LogexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#primelogexp.
    def visitPrimelogexp(self, ctx:compiladoresParser.PrimelogexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#logterm.
    def visitLogterm(self, ctx:compiladoresParser.LogtermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#primelogterm.
    def visitPrimelogterm(self, ctx:compiladoresParser.PrimelogtermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#logfactor.
    def visitLogfactor(self, ctx:compiladoresParser.LogfactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#comp.
    def visitComp(self, ctx:compiladoresParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expression.
    def visitExpression(self, ctx:compiladoresParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#primeexp.
    def visitPrimeexp(self, ctx:compiladoresParser.PrimeexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#term.
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#primeterm.
    def visitPrimeterm(self, ctx:compiladoresParser.PrimetermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#functcall.
    def visitFunctcall(self, ctx:compiladoresParser.FunctcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tdata.
    def visitTdata(self, ctx:compiladoresParser.TdataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#functprototype.
    def visitFunctprototype(self, ctx:compiladoresParser.FunctprototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#args.
    def visitArgs(self, ctx:compiladoresParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#list_args.
    def visitList_args(self, ctx:compiladoresParser.List_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#functdef.
    def visitFunctdef(self, ctx:compiladoresParser.FunctdefContext):
        return self.visitChildren(ctx)



del compiladoresParser