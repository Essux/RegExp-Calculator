# Generated from RegExpGrammar.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\61\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3")
        buf.write("\2\7\2\20\n\2\f\2\16\2\23\13\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\7\3\33\n\3\f\3\16\3\36\13\3\3\4\3\4\3\4\3\4\3\4\7\4%")
        buf.write("\n\4\f\4\16\4(\13\4\3\5\3\5\3\5\3\5\3\5\5\5/\n\5\3\5\2")
        buf.write("\5\2\4\6\6\2\4\6\b\2\2\2\60\2\n\3\2\2\2\4\24\3\2\2\2\6")
        buf.write("\37\3\2\2\2\b.\3\2\2\2\n\13\b\2\1\2\13\f\5\4\3\2\f\21")
        buf.write("\3\2\2\2\r\16\f\3\2\2\16\20\7\3\2\2\17\r\3\2\2\2\20\23")
        buf.write("\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\21")
        buf.write("\3\2\2\2\24\25\b\3\1\2\25\26\5\6\4\2\26\34\3\2\2\2\27")
        buf.write("\30\f\4\2\2\30\31\7\4\2\2\31\33\5\6\4\2\32\27\3\2\2\2")
        buf.write("\33\36\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\5\3\2\2")
        buf.write("\2\36\34\3\2\2\2\37 \b\4\1\2 !\5\b\5\2!&\3\2\2\2\"#\f")
        buf.write("\4\2\2#%\5\b\5\2$\"\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2")
        buf.write("\2\2\'\7\3\2\2\2(&\3\2\2\2)*\7\5\2\2*+\5\2\2\2+,\7\6\2")
        buf.write("\2,/\3\2\2\2-/\7\7\2\2.)\3\2\2\2.-\3\2\2\2/\t\3\2\2\2")
        buf.write("\6\21\34&.")
        return buf.getvalue()


class RegExpGrammarParser ( Parser ):

    grammarFileName = "RegExpGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'|'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "WS" ]

    RULE_r0 = 0
    RULE_r1 = 1
    RULE_r2 = 2
    RULE_r3 = 3

    ruleNames =  [ "r0", "r1", "r2", "r3" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ID=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class R0Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r1(self):
            return self.getTypedRuleContext(RegExpGrammarParser.R1Context,0)


        def r0(self):
            return self.getTypedRuleContext(RegExpGrammarParser.R0Context,0)


        def getRuleIndex(self):
            return RegExpGrammarParser.RULE_r0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR0" ):
                return visitor.visitR0(self)
            else:
                return visitor.visitChildren(self)



    def r0(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegExpGrammarParser.R0Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_r0, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.r1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 15
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RegExpGrammarParser.R0Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_r0)
                    self.state = 11
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 12
                    self.match(RegExpGrammarParser.T__0) 
                self.state = 17
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class R1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r2(self):
            return self.getTypedRuleContext(RegExpGrammarParser.R2Context,0)


        def r1(self):
            return self.getTypedRuleContext(RegExpGrammarParser.R1Context,0)


        def getRuleIndex(self):
            return RegExpGrammarParser.RULE_r1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR1" ):
                return visitor.visitR1(self)
            else:
                return visitor.visitChildren(self)



    def r1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegExpGrammarParser.R1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_r1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.r2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RegExpGrammarParser.R1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_r1)
                    self.state = 21
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 22
                    self.match(RegExpGrammarParser.T__1)
                    self.state = 23
                    self.r2(0) 
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class R2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r3(self):
            return self.getTypedRuleContext(RegExpGrammarParser.R3Context,0)


        def r2(self):
            return self.getTypedRuleContext(RegExpGrammarParser.R2Context,0)


        def getRuleIndex(self):
            return RegExpGrammarParser.RULE_r2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR2" ):
                return visitor.visitR2(self)
            else:
                return visitor.visitChildren(self)



    def r2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegExpGrammarParser.R2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_r2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.r3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RegExpGrammarParser.R2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_r2)
                    self.state = 32
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 33
                    self.r3() 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class R3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r0(self):
            return self.getTypedRuleContext(RegExpGrammarParser.R0Context,0)


        def ID(self):
            return self.getToken(RegExpGrammarParser.ID, 0)

        def getRuleIndex(self):
            return RegExpGrammarParser.RULE_r3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR3" ):
                return visitor.visitR3(self)
            else:
                return visitor.visitChildren(self)




    def r3(self):

        localctx = RegExpGrammarParser.R3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_r3)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegExpGrammarParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(RegExpGrammarParser.T__2)
                self.state = 40
                self.r0(0)
                self.state = 41
                self.match(RegExpGrammarParser.T__3)
                pass
            elif token in [RegExpGrammarParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(RegExpGrammarParser.ID)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.r0_sempred
        self._predicates[1] = self.r1_sempred
        self._predicates[2] = self.r2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def r0_sempred(self, localctx:R0Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def r1_sempred(self, localctx:R1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def r2_sempred(self, localctx:R2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




