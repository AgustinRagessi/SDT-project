grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

EQ : '=' ;
PA : '(' ;
PC : ')' ;
LLA : '{' ;
LLC : '}' ;
PYC : ';' ;
COMA : ',' ;
EQQ : '==';
UNEQ: '!=';
GE: '>=';
GT: '>';
LE: '<=';
LT: '<';
RET: 'return';
IF: 'if';
OR: '||';
AND: '&&';
FOR: 'for';
PP: '++';
MM: '--';
ADD: '+';
SUB: '-';
MULT: '*';
DIV: '/';
MOD: '%';

INT: 'int';
DOUBLE: 'double';
CHAR: 'char';
STRING: 'string';

NUMERO : DIGITO+ ;

WHILE : 'while' ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \t\r\n] -> skip ;
OTRO : . ;

// HORAPAR : ([01][02468] | '2'[02])':'[0-5]DIGITO ;

// FECHAPAR : ('0'[1-9] | [12] DIGITO | '30') '/' ('0'[2468] | '1'[02])
//                '/' DIGITO DIGITO DIGITO DIGITO ;

// s : ID     {print("ID ->" + $ID.text + "<--") }         s
//   | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
//   | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
//   | HORAPAR {print("Hora par ->" + $HORAPAR.text + "<--") }  s
//   | FECHAPAR {print("Mes par ->" + $FECHAPAR.text + "<--") }  s
//   | EOF
//   ;

// si : s EOF ;

// s : PA s PC s
//   |
//   ;

programa : instrucciones EOF ;

instrucciones : instruccion instrucciones
              |
              ;

instruccion : declaracion PYC
            | asignacion PYC
            | ret PYC
            | if_stmt
            | for_stmt
            | while_stmt
            | bloque
            | functcall PYC
            | functprototype PYC
            | functdef 
            ;

declaracion : tdata ID definicion lista_var ;

definicion : EQ NUMERO
           | EQ opar
           |
           ;

bloque : LLA instrucciones LLC ;

asignacion: ID EQ opar | ID EQ functcall;

lista_var : COMA ID definicion lista_var
          |
          ;

while_stmt : WHILE PA oplo PC instruccion ;

ret: (RET ID | RET NUMERO);

if_stmt: IF PA oplo PC instruccion ;

for_stmt: FOR PA asignacion PYC oplo PYC asignacion PC instruccion ;

opar: expression;

logicoperators: (EQQ | GE | LE | GT | LT);

oplo: logexpression;

logexpression: logterm primelogexp;

primelogexp: OR logterm primelogexp | ;

logterm: logfactor primelogterm;

primelogterm: AND logfactor primelogterm | ;

logfactor: factor | comp | PA logexpression PC ;

comp: opar logicoperators opar | comp logicoperators comp;

expression: term primeexp;

primeexp: ADD term primeexp| SUB term primeexp| ;

term: factor primeterm;

primeterm: MULT factor primeterm| DIV factor primeterm| MOD factor primeterm| ;

factor: NUMERO | ID | functcall | SUB NUMERO | SUB ID | PA expression PC ;

functcall: ID PA ID PC | ID PA NUMERO PC;

tdata : INT|DOUBLE|CHAR|STRING ;

functprototype: tdata ID PA args PC ;

args: tdata ID list_args | tdata list_args |;

list_args: COMA tdata ID list_args | COMA tdata list_args| ;

functdef: tdata ID PA args PC bloque ; 