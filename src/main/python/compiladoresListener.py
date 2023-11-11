# Generated from /home/curso/proyectoDHS/src/main/python/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class compiladoresListener(ParseTreeListener):

    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#definicion.
    def enterDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#definicion.
    def exitDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lista_var.
    def enterLista_var(self, ctx:compiladoresParser.Lista_varContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lista_var.
    def exitLista_var(self, ctx:compiladoresParser.Lista_varContext):
        pass


    # Enter a parse tree produced by compiladoresParser#while_stmt.
    def enterWhile_stmt(self, ctx:compiladoresParser.While_stmtContext):
        pass

    # Exit a parse tree produced by compiladoresParser#while_stmt.
    def exitWhile_stmt(self, ctx:compiladoresParser.While_stmtContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ret.
    def enterRet(self, ctx:compiladoresParser.RetContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ret.
    def exitRet(self, ctx:compiladoresParser.RetContext):
        pass


    # Enter a parse tree produced by compiladoresParser#if_stmt.
    def enterIf_stmt(self, ctx:compiladoresParser.If_stmtContext):
        pass

    # Exit a parse tree produced by compiladoresParser#if_stmt.
    def exitIf_stmt(self, ctx:compiladoresParser.If_stmtContext):
        pass


    # Enter a parse tree produced by compiladoresParser#for_stmt.
    def enterFor_stmt(self, ctx:compiladoresParser.For_stmtContext):
        pass

    # Exit a parse tree produced by compiladoresParser#for_stmt.
    def exitFor_stmt(self, ctx:compiladoresParser.For_stmtContext):
        pass


    # Enter a parse tree produced by compiladoresParser#opar.
    def enterOpar(self, ctx:compiladoresParser.OparContext):
        pass

    # Exit a parse tree produced by compiladoresParser#opar.
    def exitOpar(self, ctx:compiladoresParser.OparContext):
        pass


    # Enter a parse tree produced by compiladoresParser#logicoperators.
    def enterLogicoperators(self, ctx:compiladoresParser.LogicoperatorsContext):
        pass

    # Exit a parse tree produced by compiladoresParser#logicoperators.
    def exitLogicoperators(self, ctx:compiladoresParser.LogicoperatorsContext):
        pass


    # Enter a parse tree produced by compiladoresParser#oplo.
    def enterOplo(self, ctx:compiladoresParser.OploContext):
        pass

    # Exit a parse tree produced by compiladoresParser#oplo.
    def exitOplo(self, ctx:compiladoresParser.OploContext):
        pass


    # Enter a parse tree produced by compiladoresParser#logexpression.
    def enterLogexpression(self, ctx:compiladoresParser.LogexpressionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#logexpression.
    def exitLogexpression(self, ctx:compiladoresParser.LogexpressionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#primelogexp.
    def enterPrimelogexp(self, ctx:compiladoresParser.PrimelogexpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#primelogexp.
    def exitPrimelogexp(self, ctx:compiladoresParser.PrimelogexpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#logterm.
    def enterLogterm(self, ctx:compiladoresParser.LogtermContext):
        pass

    # Exit a parse tree produced by compiladoresParser#logterm.
    def exitLogterm(self, ctx:compiladoresParser.LogtermContext):
        pass


    # Enter a parse tree produced by compiladoresParser#primelogterm.
    def enterPrimelogterm(self, ctx:compiladoresParser.PrimelogtermContext):
        pass

    # Exit a parse tree produced by compiladoresParser#primelogterm.
    def exitPrimelogterm(self, ctx:compiladoresParser.PrimelogtermContext):
        pass


    # Enter a parse tree produced by compiladoresParser#logfactor.
    def enterLogfactor(self, ctx:compiladoresParser.LogfactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#logfactor.
    def exitLogfactor(self, ctx:compiladoresParser.LogfactorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#comp.
    def enterComp(self, ctx:compiladoresParser.CompContext):
        pass

    # Exit a parse tree produced by compiladoresParser#comp.
    def exitComp(self, ctx:compiladoresParser.CompContext):
        pass


    # Enter a parse tree produced by compiladoresParser#expression.
    def enterExpression(self, ctx:compiladoresParser.ExpressionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#expression.
    def exitExpression(self, ctx:compiladoresParser.ExpressionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#primeexp.
    def enterPrimeexp(self, ctx:compiladoresParser.PrimeexpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#primeexp.
    def exitPrimeexp(self, ctx:compiladoresParser.PrimeexpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#term.
    def enterTerm(self, ctx:compiladoresParser.TermContext):
        pass

    # Exit a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        pass


    # Enter a parse tree produced by compiladoresParser#primeterm.
    def enterPrimeterm(self, ctx:compiladoresParser.PrimetermContext):
        pass

    # Exit a parse tree produced by compiladoresParser#primeterm.
    def exitPrimeterm(self, ctx:compiladoresParser.PrimetermContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#functcall.
    def enterFunctcall(self, ctx:compiladoresParser.FunctcallContext):
        pass

    # Exit a parse tree produced by compiladoresParser#functcall.
    def exitFunctcall(self, ctx:compiladoresParser.FunctcallContext):
        pass


    # Enter a parse tree produced by compiladoresParser#tdata.
    def enterTdata(self, ctx:compiladoresParser.TdataContext):
        pass

    # Exit a parse tree produced by compiladoresParser#tdata.
    def exitTdata(self, ctx:compiladoresParser.TdataContext):
        pass


    # Enter a parse tree produced by compiladoresParser#functprototype.
    def enterFunctprototype(self, ctx:compiladoresParser.FunctprototypeContext):
        pass

    # Exit a parse tree produced by compiladoresParser#functprototype.
    def exitFunctprototype(self, ctx:compiladoresParser.FunctprototypeContext):
        pass


    # Enter a parse tree produced by compiladoresParser#args.
    def enterArgs(self, ctx:compiladoresParser.ArgsContext):
        pass

    # Exit a parse tree produced by compiladoresParser#args.
    def exitArgs(self, ctx:compiladoresParser.ArgsContext):
        pass


    # Enter a parse tree produced by compiladoresParser#list_args.
    def enterList_args(self, ctx:compiladoresParser.List_argsContext):
        pass

    # Exit a parse tree produced by compiladoresParser#list_args.
    def exitList_args(self, ctx:compiladoresParser.List_argsContext):
        pass


    # Enter a parse tree produced by compiladoresParser#functdef.
    def enterFunctdef(self, ctx:compiladoresParser.FunctdefContext):
        pass

    # Exit a parse tree produced by compiladoresParser#functdef.
    def exitFunctdef(self, ctx:compiladoresParser.FunctdefContext):
        pass



del compiladoresParser