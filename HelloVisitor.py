# Generated from Hello.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete generic visitor for a parse tree produced by HelloParser.

class HelloVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HelloParser#r0.
    def visitR0(self, ctx:HelloParser.R0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#r1.
    def visitR1(self, ctx:HelloParser.R1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#r2.
    def visitR2(self, ctx:HelloParser.R2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#r3.
    def visitR3(self, ctx:HelloParser.R3Context):
        return self.visitChildren(ctx)



del HelloParser