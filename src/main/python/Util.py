from SymbolTable import *
from ID import *

class Util:
    @staticmethod
    def getIDAmount(data):
        assign = data.find('=')
        if assign > 0:
            data = data[:assign]
        return data.split(',')
    
    @staticmethod
    def verifyInit(data):
        if data.find('=') > 0:
            if data[data.index('=') + 1:] != '':
                return True
        return False
    
    @staticmethod
    def getFunctName(data):
        indexPA = data.index('(')
        return data[:indexPA]
    
    @staticmethod
    def getFunctArgs(data):
        argsList = []
        indexPA = data.index('(')
        indexPC = data.index(')')
        arg = data[indexPA +1:indexPC].split(',')
        
        for i in arg:
            if i[:3] == 'int':
                name = i[3:]
                datType = 'int'
                argsList.append(Variable(name, datType))
                
            elif i[:6] == 'double':
                name = i[6:]
                datType = 'double'
                argsList.append(Variable(name, datType))
            
            elif i == '':
                print("No arguments found.")
                
        return argsList

    @staticmethod
    def getFunctParam(data):
        argsList = []
        indexPA = data.index('(')
        indexPC = data.index(')')
        return data[indexPA + 1: indexPC].split(',')
    
    @staticmethod
    def compareWithPrototype(identifier):
        globalCtx = SymbolTable._stackCtx[0].symbols
        for i in globalCtx:
            if (identifier.name == 1):
                id = globalCtx[i]
                break
        if identifier == id:
            return True
        
        else:
            if identifier.dataType != id.dataType:
                print("Tipos de dato no concuerdan!")
                return False
            if identifier.args != id.args:
                print("Argumento no concuerda!")
                return False
            
    @staticmethod
    def getID(context, param) -> ID:
        for key,value in context.symbols.items():
            if key == param:
                return value
        
    @staticmethod
    def compareParamAmounts(identifier, params) -> bool:
        if len(identifier.args) > len(params):
            print("Mas argumentos en prototipo que en funcion.")
            return False
        if len(identifier.args) < len(params):
            print("Mas parametros de funcion que en prototipo.")
            return False
        return True
        
    
    