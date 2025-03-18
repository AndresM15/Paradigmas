grammar GramTaticBoard;

// Regla principal: Definición de una táctica
tactic
    : 'Tactic' '{' statement+ '}'
    ;

// Una instrucción puede ser una acción de jugador o una instrucción del mundo real
statement
    : playerAction
    | instructionSet
    ;

// Acción de un jugador
playerAction
    : 'player' '(' INT ')' action
    ;

// Tipos de acciones
action
    : moveAction
    | passAction
    | shootAction
    ;

// Movimiento del jugador
moveAction
    : 'move' '(' INT ',' INT ')'
    ;

// Pase del balón a otro jugador
passAction
    : 'pass' '(' INT ')'
    ;

// Disparo al arco
shootAction
    : 'shoot' '(' 'goal' ')'
    ;

// Conjunto de instrucciones del mundo real
instructionSet
    : '[:]' '{' ID+ '}'
    ;

// Tokens
INT: [0-9]+;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\r\n]+ -> skip;
