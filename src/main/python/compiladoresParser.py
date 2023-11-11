# Generated from /home/curso/proyectoDHS/src/main/python/compiladores.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,34,296,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,3,1,72,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,94,8,2,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,106,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,3,6,118,8,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,126,8,7,1,
        8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,138,8,9,1,10,1,10,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,3,16,170,8,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,3,18,
        180,8,18,1,19,1,19,1,19,1,19,1,19,1,19,3,19,188,8,19,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,5,20,199,8,20,10,20,12,20,202,9,
        20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,
        22,216,8,22,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,
        24,1,24,1,24,1,24,1,24,1,24,3,24,234,8,24,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,247,8,25,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,3,26,257,8,26,1,27,1,27,1,28,1,28,1,28,1,
        28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,275,8,
        29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,287,8,
        30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,0,1,40,32,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,0,2,2,0,8,8,10,13,1,0,26,29,298,0,64,1,0,0,0,2,71,1,
        0,0,0,4,93,1,0,0,0,6,95,1,0,0,0,8,105,1,0,0,0,10,107,1,0,0,0,12,
        117,1,0,0,0,14,125,1,0,0,0,16,127,1,0,0,0,18,137,1,0,0,0,20,139,
        1,0,0,0,22,145,1,0,0,0,24,155,1,0,0,0,26,157,1,0,0,0,28,159,1,0,
        0,0,30,161,1,0,0,0,32,169,1,0,0,0,34,171,1,0,0,0,36,179,1,0,0,0,
        38,187,1,0,0,0,40,189,1,0,0,0,42,203,1,0,0,0,44,215,1,0,0,0,46,217,
        1,0,0,0,48,233,1,0,0,0,50,246,1,0,0,0,52,256,1,0,0,0,54,258,1,0,
        0,0,56,260,1,0,0,0,58,274,1,0,0,0,60,286,1,0,0,0,62,288,1,0,0,0,
        64,65,3,2,1,0,65,66,5,0,0,1,66,1,1,0,0,0,67,68,3,4,2,0,68,69,3,2,
        1,0,69,72,1,0,0,0,70,72,1,0,0,0,71,67,1,0,0,0,71,70,1,0,0,0,72,3,
        1,0,0,0,73,74,3,6,3,0,74,75,5,6,0,0,75,94,1,0,0,0,76,77,3,12,6,0,
        77,78,5,6,0,0,78,94,1,0,0,0,79,80,3,18,9,0,80,81,5,6,0,0,81,94,1,
        0,0,0,82,94,3,20,10,0,83,94,3,22,11,0,84,94,3,16,8,0,85,94,3,10,
        5,0,86,87,3,52,26,0,87,88,5,6,0,0,88,94,1,0,0,0,89,90,3,56,28,0,
        90,91,5,6,0,0,91,94,1,0,0,0,92,94,3,62,31,0,93,73,1,0,0,0,93,76,
        1,0,0,0,93,79,1,0,0,0,93,82,1,0,0,0,93,83,1,0,0,0,93,84,1,0,0,0,
        93,85,1,0,0,0,93,86,1,0,0,0,93,89,1,0,0,0,93,92,1,0,0,0,94,5,1,0,
        0,0,95,96,3,54,27,0,96,97,5,32,0,0,97,98,3,8,4,0,98,99,3,14,7,0,
        99,7,1,0,0,0,100,101,5,1,0,0,101,106,5,30,0,0,102,103,5,1,0,0,103,
        106,3,24,12,0,104,106,1,0,0,0,105,100,1,0,0,0,105,102,1,0,0,0,105,
        104,1,0,0,0,106,9,1,0,0,0,107,108,5,4,0,0,108,109,3,2,1,0,109,110,
        5,5,0,0,110,11,1,0,0,0,111,112,5,32,0,0,112,113,5,1,0,0,113,118,
        3,24,12,0,114,115,5,32,0,0,115,116,5,1,0,0,116,118,3,52,26,0,117,
        111,1,0,0,0,117,114,1,0,0,0,118,13,1,0,0,0,119,120,5,7,0,0,120,121,
        5,32,0,0,121,122,3,8,4,0,122,123,3,14,7,0,123,126,1,0,0,0,124,126,
        1,0,0,0,125,119,1,0,0,0,125,124,1,0,0,0,126,15,1,0,0,0,127,128,5,
        31,0,0,128,129,5,2,0,0,129,130,3,28,14,0,130,131,5,3,0,0,131,132,
        3,4,2,0,132,17,1,0,0,0,133,134,5,14,0,0,134,138,5,32,0,0,135,136,
        5,14,0,0,136,138,5,30,0,0,137,133,1,0,0,0,137,135,1,0,0,0,138,19,
        1,0,0,0,139,140,5,15,0,0,140,141,5,2,0,0,141,142,3,28,14,0,142,143,
        5,3,0,0,143,144,3,4,2,0,144,21,1,0,0,0,145,146,5,18,0,0,146,147,
        5,2,0,0,147,148,3,12,6,0,148,149,5,6,0,0,149,150,3,28,14,0,150,151,
        5,6,0,0,151,152,3,12,6,0,152,153,5,3,0,0,153,154,3,4,2,0,154,23,
        1,0,0,0,155,156,3,42,21,0,156,25,1,0,0,0,157,158,7,0,0,0,158,27,
        1,0,0,0,159,160,3,30,15,0,160,29,1,0,0,0,161,162,3,34,17,0,162,163,
        3,32,16,0,163,31,1,0,0,0,164,165,5,16,0,0,165,166,3,34,17,0,166,
        167,3,32,16,0,167,170,1,0,0,0,168,170,1,0,0,0,169,164,1,0,0,0,169,
        168,1,0,0,0,170,33,1,0,0,0,171,172,3,38,19,0,172,173,3,36,18,0,173,
        35,1,0,0,0,174,175,5,17,0,0,175,176,3,38,19,0,176,177,3,36,18,0,
        177,180,1,0,0,0,178,180,1,0,0,0,179,174,1,0,0,0,179,178,1,0,0,0,
        180,37,1,0,0,0,181,188,3,50,25,0,182,188,3,40,20,0,183,184,5,2,0,
        0,184,185,3,30,15,0,185,186,5,3,0,0,186,188,1,0,0,0,187,181,1,0,
        0,0,187,182,1,0,0,0,187,183,1,0,0,0,188,39,1,0,0,0,189,190,6,20,
        -1,0,190,191,3,24,12,0,191,192,3,26,13,0,192,193,3,24,12,0,193,200,
        1,0,0,0,194,195,10,1,0,0,195,196,3,26,13,0,196,197,3,40,20,2,197,
        199,1,0,0,0,198,194,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,
        201,1,0,0,0,201,41,1,0,0,0,202,200,1,0,0,0,203,204,3,46,23,0,204,
        205,3,44,22,0,205,43,1,0,0,0,206,207,5,21,0,0,207,208,3,46,23,0,
        208,209,3,44,22,0,209,216,1,0,0,0,210,211,5,22,0,0,211,212,3,46,
        23,0,212,213,3,44,22,0,213,216,1,0,0,0,214,216,1,0,0,0,215,206,1,
        0,0,0,215,210,1,0,0,0,215,214,1,0,0,0,216,45,1,0,0,0,217,218,3,50,
        25,0,218,219,3,48,24,0,219,47,1,0,0,0,220,221,5,23,0,0,221,222,3,
        50,25,0,222,223,3,48,24,0,223,234,1,0,0,0,224,225,5,24,0,0,225,226,
        3,50,25,0,226,227,3,48,24,0,227,234,1,0,0,0,228,229,5,25,0,0,229,
        230,3,50,25,0,230,231,3,48,24,0,231,234,1,0,0,0,232,234,1,0,0,0,
        233,220,1,0,0,0,233,224,1,0,0,0,233,228,1,0,0,0,233,232,1,0,0,0,
        234,49,1,0,0,0,235,247,5,30,0,0,236,247,5,32,0,0,237,247,3,52,26,
        0,238,239,5,22,0,0,239,247,5,30,0,0,240,241,5,22,0,0,241,247,5,32,
        0,0,242,243,5,2,0,0,243,244,3,42,21,0,244,245,5,3,0,0,245,247,1,
        0,0,0,246,235,1,0,0,0,246,236,1,0,0,0,246,237,1,0,0,0,246,238,1,
        0,0,0,246,240,1,0,0,0,246,242,1,0,0,0,247,51,1,0,0,0,248,249,5,32,
        0,0,249,250,5,2,0,0,250,251,5,32,0,0,251,257,5,3,0,0,252,253,5,32,
        0,0,253,254,5,2,0,0,254,255,5,30,0,0,255,257,5,3,0,0,256,248,1,0,
        0,0,256,252,1,0,0,0,257,53,1,0,0,0,258,259,7,1,0,0,259,55,1,0,0,
        0,260,261,3,54,27,0,261,262,5,32,0,0,262,263,5,2,0,0,263,264,3,58,
        29,0,264,265,5,3,0,0,265,57,1,0,0,0,266,267,3,54,27,0,267,268,5,
        32,0,0,268,269,3,60,30,0,269,275,1,0,0,0,270,271,3,54,27,0,271,272,
        3,60,30,0,272,275,1,0,0,0,273,275,1,0,0,0,274,266,1,0,0,0,274,270,
        1,0,0,0,274,273,1,0,0,0,275,59,1,0,0,0,276,277,5,7,0,0,277,278,3,
        54,27,0,278,279,5,32,0,0,279,280,3,60,30,0,280,287,1,0,0,0,281,282,
        5,7,0,0,282,283,3,54,27,0,283,284,3,60,30,0,284,287,1,0,0,0,285,
        287,1,0,0,0,286,276,1,0,0,0,286,281,1,0,0,0,286,285,1,0,0,0,287,
        61,1,0,0,0,288,289,3,54,27,0,289,290,5,32,0,0,290,291,5,2,0,0,291,
        292,3,58,29,0,292,293,5,3,0,0,293,294,3,10,5,0,294,63,1,0,0,0,16,
        71,93,105,117,125,137,169,179,187,200,215,233,246,256,274,286
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'{'", "'}'", "';'", 
                     "','", "'=='", "'!='", "'>='", "'>'", "'<='", "'<'", 
                     "'return'", "'if'", "'||'", "'&&'", "'for'", "'++'", 
                     "'--'", "'+'", "'-'", "'*'", "'/'", "'%'", "'int'", 
                     "'double'", "'char'", "'string'", "<INVALID>", "'while'" ]

    symbolicNames = [ "<INVALID>", "EQ", "PA", "PC", "LLA", "LLC", "PYC", 
                      "COMA", "EQQ", "UNEQ", "GE", "GT", "LE", "LT", "RET", 
                      "IF", "OR", "AND", "FOR", "PP", "MM", "ADD", "SUB", 
                      "MULT", "DIV", "MOD", "INT", "DOUBLE", "CHAR", "STRING", 
                      "NUMERO", "WHILE", "ID", "WS", "OTRO" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_declaracion = 3
    RULE_definicion = 4
    RULE_bloque = 5
    RULE_asignacion = 6
    RULE_lista_var = 7
    RULE_while_stmt = 8
    RULE_ret = 9
    RULE_if_stmt = 10
    RULE_for_stmt = 11
    RULE_opar = 12
    RULE_logicoperators = 13
    RULE_oplo = 14
    RULE_logexpression = 15
    RULE_primelogexp = 16
    RULE_logterm = 17
    RULE_primelogterm = 18
    RULE_logfactor = 19
    RULE_comp = 20
    RULE_expression = 21
    RULE_primeexp = 22
    RULE_term = 23
    RULE_primeterm = 24
    RULE_factor = 25
    RULE_functcall = 26
    RULE_tdata = 27
    RULE_functprototype = 28
    RULE_args = 29
    RULE_list_args = 30
    RULE_functdef = 31

    ruleNames =  [ "programa", "instrucciones", "instruccion", "declaracion", 
                   "definicion", "bloque", "asignacion", "lista_var", "while_stmt", 
                   "ret", "if_stmt", "for_stmt", "opar", "logicoperators", 
                   "oplo", "logexpression", "primelogexp", "logterm", "primelogterm", 
                   "logfactor", "comp", "expression", "primeexp", "term", 
                   "primeterm", "factor", "functcall", "tdata", "functprototype", 
                   "args", "list_args", "functdef" ]

    EOF = Token.EOF
    EQ=1
    PA=2
    PC=3
    LLA=4
    LLC=5
    PYC=6
    COMA=7
    EQQ=8
    UNEQ=9
    GE=10
    GT=11
    LE=12
    LT=13
    RET=14
    IF=15
    OR=16
    AND=17
    FOR=18
    PP=19
    MM=20
    ADD=21
    SUB=22
    MULT=23
    DIV=24
    MOD=25
    INT=26
    DOUBLE=27
    CHAR=28
    STRING=29
    NUMERO=30
    WHILE=31
    ID=32
    WS=33
    OTRO=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = compiladoresParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.instrucciones()
            self.state = 65
            self.match(compiladoresParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compiladoresParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 14, 15, 18, 26, 27, 28, 29, 31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.instruccion()
                self.state = 68
                self.instrucciones()
                pass
            elif token in [-1, 5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def ret(self):
            return self.getTypedRuleContext(compiladoresParser.RetContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(compiladoresParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(compiladoresParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(compiladoresParser.While_stmtContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def functcall(self):
            return self.getTypedRuleContext(compiladoresParser.FunctcallContext,0)


        def functprototype(self):
            return self.getTypedRuleContext(compiladoresParser.FunctprototypeContext,0)


        def functdef(self):
            return self.getTypedRuleContext(compiladoresParser.FunctdefContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compiladoresParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.declaracion()
                self.state = 74
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.asignacion()
                self.state = 77
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.ret()
                self.state = 80
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 84
                self.while_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 85
                self.bloque()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 86
                self.functcall()
                self.state = 87
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 89
                self.functprototype()
                self.state = 90
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 92
                self.functdef()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdata(self):
            return self.getTypedRuleContext(compiladoresParser.TdataContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def definicion(self):
            return self.getTypedRuleContext(compiladoresParser.DefinicionContext,0)


        def lista_var(self):
            return self.getTypedRuleContext(compiladoresParser.Lista_varContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compiladoresParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.tdata()
            self.state = 96
            self.match(compiladoresParser.ID)
            self.state = 97
            self.definicion()
            self.state = 98
            self.lista_var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(compiladoresParser.EQ, 0)

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def opar(self):
            return self.getTypedRuleContext(compiladoresParser.OparContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_definicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicion" ):
                listener.enterDefinicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicion" ):
                listener.exitDefinicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicion" ):
                return visitor.visitDefinicion(self)
            else:
                return visitor.visitChildren(self)




    def definicion(self):

        localctx = compiladoresParser.DefinicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_definicion)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(compiladoresParser.EQ)
                self.state = 101
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(compiladoresParser.EQ)
                self.state = 103
                self.opar()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compiladoresParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(compiladoresParser.LLA)
            self.state = 108
            self.instrucciones()
            self.state = 109
            self.match(compiladoresParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def EQ(self):
            return self.getToken(compiladoresParser.EQ, 0)

        def opar(self):
            return self.getTypedRuleContext(compiladoresParser.OparContext,0)


        def functcall(self):
            return self.getTypedRuleContext(compiladoresParser.FunctcallContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = compiladoresParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_asignacion)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(compiladoresParser.ID)
                self.state = 112
                self.match(compiladoresParser.EQ)
                self.state = 113
                self.opar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.match(compiladoresParser.ID)
                self.state = 115
                self.match(compiladoresParser.EQ)
                self.state = 116
                self.functcall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def definicion(self):
            return self.getTypedRuleContext(compiladoresParser.DefinicionContext,0)


        def lista_var(self):
            return self.getTypedRuleContext(compiladoresParser.Lista_varContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_lista_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_var" ):
                listener.enterLista_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_var" ):
                listener.exitLista_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_var" ):
                return visitor.visitLista_var(self)
            else:
                return visitor.visitChildren(self)




    def lista_var(self):

        localctx = compiladoresParser.Lista_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lista_var)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(compiladoresParser.COMA)
                self.state = 120
                self.match(compiladoresParser.ID)
                self.state = 121
                self.definicion()
                self.state = 122
                self.lista_var()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladoresParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def oplo(self):
            return self.getTypedRuleContext(compiladoresParser.OploContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = compiladoresParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(compiladoresParser.WHILE)
            self.state = 128
            self.match(compiladoresParser.PA)
            self.state = 129
            self.oplo()
            self.state = 130
            self.match(compiladoresParser.PC)
            self.state = 131
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RET(self):
            return self.getToken(compiladoresParser.RET, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_ret

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRet" ):
                listener.enterRet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRet" ):
                listener.exitRet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet" ):
                return visitor.visitRet(self)
            else:
                return visitor.visitChildren(self)




    def ret(self):

        localctx = compiladoresParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ret)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 133
                self.match(compiladoresParser.RET)
                self.state = 134
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 2:
                self.state = 135
                self.match(compiladoresParser.RET)
                self.state = 136
                self.match(compiladoresParser.NUMERO)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(compiladoresParser.IF, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def oplo(self):
            return self.getTypedRuleContext(compiladoresParser.OploContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = compiladoresParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(compiladoresParser.IF)
            self.state = 140
            self.match(compiladoresParser.PA)
            self.state = 141
            self.oplo()
            self.state = 142
            self.match(compiladoresParser.PC)
            self.state = 143
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(compiladoresParser.FOR, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.AsignacionContext,i)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.PYC)
            else:
                return self.getToken(compiladoresParser.PYC, i)

        def oplo(self):
            return self.getTypedRuleContext(compiladoresParser.OploContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = compiladoresParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(compiladoresParser.FOR)
            self.state = 146
            self.match(compiladoresParser.PA)
            self.state = 147
            self.asignacion()
            self.state = 148
            self.match(compiladoresParser.PYC)
            self.state = 149
            self.oplo()
            self.state = 150
            self.match(compiladoresParser.PYC)
            self.state = 151
            self.asignacion()
            self.state = 152
            self.match(compiladoresParser.PC)
            self.state = 153
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OparContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(compiladoresParser.ExpressionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_opar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpar" ):
                listener.enterOpar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpar" ):
                listener.exitOpar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpar" ):
                return visitor.visitOpar(self)
            else:
                return visitor.visitChildren(self)




    def opar(self):

        localctx = compiladoresParser.OparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_opar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicoperatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQQ(self):
            return self.getToken(compiladoresParser.EQQ, 0)

        def GE(self):
            return self.getToken(compiladoresParser.GE, 0)

        def LE(self):
            return self.getToken(compiladoresParser.LE, 0)

        def GT(self):
            return self.getToken(compiladoresParser.GT, 0)

        def LT(self):
            return self.getToken(compiladoresParser.LT, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_logicoperators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicoperators" ):
                listener.enterLogicoperators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicoperators" ):
                listener.exitLogicoperators(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicoperators" ):
                return visitor.visitLogicoperators(self)
            else:
                return visitor.visitChildren(self)




    def logicoperators(self):

        localctx = compiladoresParser.LogicoperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_logicoperators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15616) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OploContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logexpression(self):
            return self.getTypedRuleContext(compiladoresParser.LogexpressionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_oplo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOplo" ):
                listener.enterOplo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOplo" ):
                listener.exitOplo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOplo" ):
                return visitor.visitOplo(self)
            else:
                return visitor.visitChildren(self)




    def oplo(self):

        localctx = compiladoresParser.OploContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_oplo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.logexpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logterm(self):
            return self.getTypedRuleContext(compiladoresParser.LogtermContext,0)


        def primelogexp(self):
            return self.getTypedRuleContext(compiladoresParser.PrimelogexpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_logexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogexpression" ):
                listener.enterLogexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogexpression" ):
                listener.exitLogexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogexpression" ):
                return visitor.visitLogexpression(self)
            else:
                return visitor.visitChildren(self)




    def logexpression(self):

        localctx = compiladoresParser.LogexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_logexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.logterm()
            self.state = 162
            self.primelogexp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimelogexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(compiladoresParser.OR, 0)

        def logterm(self):
            return self.getTypedRuleContext(compiladoresParser.LogtermContext,0)


        def primelogexp(self):
            return self.getTypedRuleContext(compiladoresParser.PrimelogexpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_primelogexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimelogexp" ):
                listener.enterPrimelogexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimelogexp" ):
                listener.exitPrimelogexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimelogexp" ):
                return visitor.visitPrimelogexp(self)
            else:
                return visitor.visitChildren(self)




    def primelogexp(self):

        localctx = compiladoresParser.PrimelogexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_primelogexp)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(compiladoresParser.OR)
                self.state = 165
                self.logterm()
                self.state = 166
                self.primelogexp()
                pass
            elif token in [3, 6]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogtermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logfactor(self):
            return self.getTypedRuleContext(compiladoresParser.LogfactorContext,0)


        def primelogterm(self):
            return self.getTypedRuleContext(compiladoresParser.PrimelogtermContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_logterm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogterm" ):
                listener.enterLogterm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogterm" ):
                listener.exitLogterm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogterm" ):
                return visitor.visitLogterm(self)
            else:
                return visitor.visitChildren(self)




    def logterm(self):

        localctx = compiladoresParser.LogtermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_logterm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.logfactor()
            self.state = 172
            self.primelogterm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimelogtermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(compiladoresParser.AND, 0)

        def logfactor(self):
            return self.getTypedRuleContext(compiladoresParser.LogfactorContext,0)


        def primelogterm(self):
            return self.getTypedRuleContext(compiladoresParser.PrimelogtermContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_primelogterm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimelogterm" ):
                listener.enterPrimelogterm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimelogterm" ):
                listener.exitPrimelogterm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimelogterm" ):
                return visitor.visitPrimelogterm(self)
            else:
                return visitor.visitChildren(self)




    def primelogterm(self):

        localctx = compiladoresParser.PrimelogtermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primelogterm)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(compiladoresParser.AND)
                self.state = 175
                self.logfactor()
                self.state = 176
                self.primelogterm()
                pass
            elif token in [3, 6, 16]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogfactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def comp(self):
            return self.getTypedRuleContext(compiladoresParser.CompContext,0)


        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def logexpression(self):
            return self.getTypedRuleContext(compiladoresParser.LogexpressionContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_logfactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogfactor" ):
                listener.enterLogfactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogfactor" ):
                listener.exitLogfactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogfactor" ):
                return visitor.visitLogfactor(self)
            else:
                return visitor.visitChildren(self)




    def logfactor(self):

        localctx = compiladoresParser.LogfactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_logfactor)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.comp(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.match(compiladoresParser.PA)
                self.state = 184
                self.logexpression()
                self.state = 185
                self.match(compiladoresParser.PC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.OparContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.OparContext,i)


        def logicoperators(self):
            return self.getTypedRuleContext(compiladoresParser.LogicoperatorsContext,0)


        def comp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.CompContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.CompContext,i)


        def getRuleIndex(self):
            return compiladoresParser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp" ):
                return visitor.visitComp(self)
            else:
                return visitor.visitChildren(self)



    def comp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = compiladoresParser.CompContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_comp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.opar()
            self.state = 191
            self.logicoperators()
            self.state = 192
            self.opar()
            self._ctx.stop = self._input.LT(-1)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = compiladoresParser.CompContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_comp)
                    self.state = 194
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 195
                    self.logicoperators()
                    self.state = 196
                    self.comp(2) 
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def primeexp(self):
            return self.getTypedRuleContext(compiladoresParser.PrimeexpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = compiladoresParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.term()
            self.state = 204
            self.primeexp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimeexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(compiladoresParser.ADD, 0)

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def primeexp(self):
            return self.getTypedRuleContext(compiladoresParser.PrimeexpContext,0)


        def SUB(self):
            return self.getToken(compiladoresParser.SUB, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_primeexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimeexp" ):
                listener.enterPrimeexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimeexp" ):
                listener.exitPrimeexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimeexp" ):
                return visitor.visitPrimeexp(self)
            else:
                return visitor.visitChildren(self)




    def primeexp(self):

        localctx = compiladoresParser.PrimeexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primeexp)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(compiladoresParser.ADD)
                self.state = 207
                self.term()
                self.state = 208
                self.primeexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.match(compiladoresParser.SUB)
                self.state = 211
                self.term()
                self.state = 212
                self.primeexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def primeterm(self):
            return self.getTypedRuleContext(compiladoresParser.PrimetermContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = compiladoresParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.factor()
            self.state = 218
            self.primeterm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimetermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(compiladoresParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def primeterm(self):
            return self.getTypedRuleContext(compiladoresParser.PrimetermContext,0)


        def DIV(self):
            return self.getToken(compiladoresParser.DIV, 0)

        def MOD(self):
            return self.getToken(compiladoresParser.MOD, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_primeterm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimeterm" ):
                listener.enterPrimeterm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimeterm" ):
                listener.exitPrimeterm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimeterm" ):
                return visitor.visitPrimeterm(self)
            else:
                return visitor.visitChildren(self)




    def primeterm(self):

        localctx = compiladoresParser.PrimetermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_primeterm)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(compiladoresParser.MULT)
                self.state = 221
                self.factor()
                self.state = 222
                self.primeterm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(compiladoresParser.DIV)
                self.state = 225
                self.factor()
                self.state = 226
                self.primeterm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.match(compiladoresParser.MOD)
                self.state = 229
                self.factor()
                self.state = 230
                self.primeterm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def functcall(self):
            return self.getTypedRuleContext(compiladoresParser.FunctcallContext,0)


        def SUB(self):
            return self.getToken(compiladoresParser.SUB, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def expression(self):
            return self.getTypedRuleContext(compiladoresParser.ExpressionContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = compiladoresParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_factor)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.functcall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.match(compiladoresParser.SUB)
                self.state = 239
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 240
                self.match(compiladoresParser.SUB)
                self.state = 241
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 242
                self.match(compiladoresParser.PA)
                self.state = 243
                self.expression()
                self.state = 244
                self.match(compiladoresParser.PC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.ID)
            else:
                return self.getToken(compiladoresParser.ID, i)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_functcall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctcall" ):
                listener.enterFunctcall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctcall" ):
                listener.exitFunctcall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctcall" ):
                return visitor.visitFunctcall(self)
            else:
                return visitor.visitChildren(self)




    def functcall(self):

        localctx = compiladoresParser.FunctcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_functcall)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(compiladoresParser.ID)
                self.state = 249
                self.match(compiladoresParser.PA)
                self.state = 250
                self.match(compiladoresParser.ID)
                self.state = 251
                self.match(compiladoresParser.PC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.match(compiladoresParser.ID)
                self.state = 253
                self.match(compiladoresParser.PA)
                self.state = 254
                self.match(compiladoresParser.NUMERO)
                self.state = 255
                self.match(compiladoresParser.PC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TdataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladoresParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(compiladoresParser.DOUBLE, 0)

        def CHAR(self):
            return self.getToken(compiladoresParser.CHAR, 0)

        def STRING(self):
            return self.getToken(compiladoresParser.STRING, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_tdata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTdata" ):
                listener.enterTdata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTdata" ):
                listener.exitTdata(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTdata" ):
                return visitor.visitTdata(self)
            else:
                return visitor.visitChildren(self)




    def tdata(self):

        localctx = compiladoresParser.TdataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_tdata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctprototypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdata(self):
            return self.getTypedRuleContext(compiladoresParser.TdataContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def args(self):
            return self.getTypedRuleContext(compiladoresParser.ArgsContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_functprototype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctprototype" ):
                listener.enterFunctprototype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctprototype" ):
                listener.exitFunctprototype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctprototype" ):
                return visitor.visitFunctprototype(self)
            else:
                return visitor.visitChildren(self)




    def functprototype(self):

        localctx = compiladoresParser.FunctprototypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_functprototype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.tdata()
            self.state = 261
            self.match(compiladoresParser.ID)
            self.state = 262
            self.match(compiladoresParser.PA)
            self.state = 263
            self.args()
            self.state = 264
            self.match(compiladoresParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdata(self):
            return self.getTypedRuleContext(compiladoresParser.TdataContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def list_args(self):
            return self.getTypedRuleContext(compiladoresParser.List_argsContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = compiladoresParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_args)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.tdata()
                self.state = 267
                self.match(compiladoresParser.ID)
                self.state = 268
                self.list_args()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.tdata()
                self.state = 271
                self.list_args()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def tdata(self):
            return self.getTypedRuleContext(compiladoresParser.TdataContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def list_args(self):
            return self.getTypedRuleContext(compiladoresParser.List_argsContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_list_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_args" ):
                listener.enterList_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_args" ):
                listener.exitList_args(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_args" ):
                return visitor.visitList_args(self)
            else:
                return visitor.visitChildren(self)




    def list_args(self):

        localctx = compiladoresParser.List_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_list_args)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(compiladoresParser.COMA)
                self.state = 277
                self.tdata()
                self.state = 278
                self.match(compiladoresParser.ID)
                self.state = 279
                self.list_args()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(compiladoresParser.COMA)
                self.state = 282
                self.tdata()
                self.state = 283
                self.list_args()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctdefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdata(self):
            return self.getTypedRuleContext(compiladoresParser.TdataContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def args(self):
            return self.getTypedRuleContext(compiladoresParser.ArgsContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_functdef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctdef" ):
                listener.enterFunctdef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctdef" ):
                listener.exitFunctdef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctdef" ):
                return visitor.visitFunctdef(self)
            else:
                return visitor.visitChildren(self)




    def functdef(self):

        localctx = compiladoresParser.FunctdefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_functdef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.tdata()
            self.state = 289
            self.match(compiladoresParser.ID)
            self.state = 290
            self.match(compiladoresParser.PA)
            self.state = 291
            self.args()
            self.state = 292
            self.match(compiladoresParser.PC)
            self.state = 293
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[20] = self.comp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def comp_sempred(self, localctx:CompContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




