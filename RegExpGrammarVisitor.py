# Generated from RegExpGrammar.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RegExpGrammarParser import RegExpGrammarParser
else:
    from RegExpGrammarParser import RegExpGrammarParser

# This class defines a complete generic visitor for a parse tree produced by RegExpGrammarParser.

class RegExpGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegExpGrammarParser#r1.
    def visitR1(self, ctx:RegExpGrammarParser.R1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpGrammarParser#r2.
    def visitR2(self, ctx:RegExpGrammarParser.R2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpGrammarParser#r0.
    def visitR0(self, ctx:RegExpGrammarParser.R0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpGrammarParser#r3.
    def visitR3(self, ctx:RegExpGrammarParser.R3Context):
        return self.visitChildren(ctx)



del RegExpGrammarParser