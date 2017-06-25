grammar RegExpGrammar;
r1 : r1 '|' r2 | r2;
r2 : r2 r0 | r0;
r0 : r3 '*' | r3 ;
r3 : '(' r1 ')' | ID;
ID : [A-z]+ ;             // match lower-case identifiers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines, \r (Windows)