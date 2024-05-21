grammar JSBach;

root :  procediment+ EOF;

procediment : PROC_ID VAR_ID* OPENKEY instruction+ CLOSEKEY;

instruction : VAR_ID ASSIG expr # assig
    | WRITE expr+ # write
    | READ VAR_ID # read
    | REPR expr expr? # repr
    | WHILE condition OPENKEY instruction+ CLOSEKEY # while
    | IF condition OPENKEY instruction+ CLOSEKEY (ELSE OPENKEY instruction+ CLOSEKEY)? # ifelse
    | PROC_ID expr*  # funcall
    | VAR_ID APPEND expr  # append
    | CUT VAR_ID OPENBRACKET expr CLOSEBRACKET  # cut
    ;

expr : OPENPARENTHESIS expr CLOSEPARENTHESIS  # parenthesis
    | <assoc=right> expr '^' expr  # op
    | expr (STAR | DIV | MOD) expr  # op
    | expr (PLUS | MINUS) expr # op
    | NUM  # num
    | note  # notexpr
    | STRING  # string
    | OPENLIST expr* CLOSELIST  # list
    | VAR_ID  # id
    | LEN expr  # listlen
    | expr OPENBRACKET expr CLOSEBRACKET  # indexlist
    ;

condition : expr RELATION expr ;

LINE_COMMENT: '~~~' .*? '~~~'  -> skip ;

/** Claus d'obertura i tancament */
OPENKEY: '|:' ;
CLOSEKEY: ':|' ;
OPENLIST : '{' ;
CLOSELIST : '}' ;
OPENPARENTHESIS : '(' ;
CLOSEPARENTHESIS : ')' ;
OPENBRACKET : '[' ;
CLOSEBRACKET : ']' ;

/** Instructions */
ASSIG : '<-' ;
WRITE : '<!>' ;
READ : '<?>' ;
REPR : '<:>' ; 
WHILE : 'while' ;
IF : 'if' ;
ELSE : 'else' ;
APPEND : '<<' ;
CUT : '8<' ;

/** Operacions d'enters, condicions i operador len (#) */
NUM : DIGIT+ ;
POWER : '^' ;
STAR : '*' ;
DIV : '/' ;
PLUS : '+' ;
MINUS : '-' ;
MOD : '%' ;
RELATION : '=' | '/=' | '<' | '>' | '<=' | '>=' ;
LEN : '#' ;


/** Notes musicals */
BASE_NOTE: [A-G];
NOTE_OCTAVE: [A-G][0-8];
note : NOTE_OCTAVE NUM # noteDuration
    | BASE_NOTE NUM # noteDuration
    | BASE_NOTE # basenote
    | NOTE_OCTAVE # basenote
    ;


/** Identificadors
Les variables comencen amb una lletra minuscula i poden tenir lletres i guions baixos.
Els noms de procediments comencen amb lletra majuscula i tambe poden tenir lletres i guions baixos tot seguit
*/
VAR_ID : [a-z](LETTER|DIGIT|'_')*;
PROC_ID: [A-Z](LETTER|DIGIT|'_')*;
STRING: '"' .*? '"';


/** Altres */
LETTER : [a-zA-Z];
DIGIT : [0-9];


WS : [ \n]+ -> skip ;