grammar GramTaticBoard;

tactic
    : 'Tactic' '{' statement+ '}'
    ;

statement
    : playerAction
    ;

playerAction
    : 'player' '(' INT ')' action
    ;

action
    : moveAction
    | passAction
    | shootAction
    ;

moveAction
    : 'move' '(' INT ',' INT ')'
    ;

passAction
    : 'pass' '(' INT ')'
    ;

shootAction
    : 'shoot' '(' 'goal' ')'
    ;

// Tokens
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
