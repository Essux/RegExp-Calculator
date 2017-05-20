grammar RegExpGrammar;
r0 : r1 | r1 '*';
r1 : r1 '|' r1 | r2;
r2 : r2 r3 | r3;
r3 : '(' r0 ')' | ID;
ID : [A-z]+ ;             // match lower-case identifiers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines, \r (Windows)