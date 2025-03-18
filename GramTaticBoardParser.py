# Generated from GramTaticBoard.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,39,8,3,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,
        1,7,1,7,4,7,61,8,7,11,7,12,7,62,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,
        14,0,0,63,0,16,1,0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,6,38,1,0,0,0,8,
        40,1,0,0,0,10,47,1,0,0,0,12,52,1,0,0,0,14,57,1,0,0,0,16,17,5,1,0,
        0,17,19,5,2,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,
        1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,24,5,3,0,0,24,1,1,0,0,0,25,
        28,3,4,2,0,26,28,3,14,7,0,27,25,1,0,0,0,27,26,1,0,0,0,28,3,1,0,0,
        0,29,30,5,4,0,0,30,31,5,5,0,0,31,32,5,13,0,0,32,33,5,6,0,0,33,34,
        3,6,3,0,34,5,1,0,0,0,35,39,3,8,4,0,36,39,3,10,5,0,37,39,3,12,6,0,
        38,35,1,0,0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,7,1,0,0,0,40,41,5,7,
        0,0,41,42,5,5,0,0,42,43,5,13,0,0,43,44,5,8,0,0,44,45,5,13,0,0,45,
        46,5,6,0,0,46,9,1,0,0,0,47,48,5,9,0,0,48,49,5,5,0,0,49,50,5,13,0,
        0,50,51,5,6,0,0,51,11,1,0,0,0,52,53,5,10,0,0,53,54,5,5,0,0,54,55,
        5,11,0,0,55,56,5,6,0,0,56,13,1,0,0,0,57,58,5,12,0,0,58,60,5,2,0,
        0,59,61,5,14,0,0,60,59,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,0,62,63,
        1,0,0,0,63,64,1,0,0,0,64,65,5,3,0,0,65,15,1,0,0,0,4,21,27,38,62
    ]

class GramTaticBoardParser ( Parser ):

    grammarFileName = "GramTaticBoard.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Tactic'", "'{'", "'}'", "'player'", 
                     "'('", "')'", "'move'", "','", "'pass'", "'shoot'", 
                     "'goal'", "'[:]'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "ID", "WS" ]

    RULE_tactic = 0
    RULE_statement = 1
    RULE_playerAction = 2
    RULE_action = 3
    RULE_moveAction = 4
    RULE_passAction = 5
    RULE_shootAction = 6
    RULE_instructionSet = 7

    ruleNames =  [ "tactic", "statement", "playerAction", "action", "moveAction", 
                   "passAction", "shootAction", "instructionSet" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    INT=13
    ID=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TacticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramTaticBoardParser.StatementContext)
            else:
                return self.getTypedRuleContext(GramTaticBoardParser.StatementContext,i)


        def getRuleIndex(self):
            return GramTaticBoardParser.RULE_tactic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTactic" ):
                listener.enterTactic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTactic" ):
                listener.exitTactic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTactic" ):
                return visitor.visitTactic(self)
            else:
                return visitor.visitChildren(self)




    def tactic(self):

        localctx = GramTaticBoardParser.TacticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_tactic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(GramTaticBoardParser.T__0)
            self.state = 17
            self.match(GramTaticBoardParser.T__1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4 or _la==12):
                    break

            self.state = 23
            self.match(GramTaticBoardParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def playerAction(self):
            return self.getTypedRuleContext(GramTaticBoardParser.PlayerActionContext,0)


        def instructionSet(self):
            return self.getTypedRuleContext(GramTaticBoardParser.InstructionSetContext,0)


        def getRuleIndex(self):
            return GramTaticBoardParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = GramTaticBoardParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.playerAction()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.instructionSet()
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


    class PlayerActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GramTaticBoardParser.INT, 0)

        def action(self):
            return self.getTypedRuleContext(GramTaticBoardParser.ActionContext,0)


        def getRuleIndex(self):
            return GramTaticBoardParser.RULE_playerAction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayerAction" ):
                listener.enterPlayerAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayerAction" ):
                listener.exitPlayerAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlayerAction" ):
                return visitor.visitPlayerAction(self)
            else:
                return visitor.visitChildren(self)




    def playerAction(self):

        localctx = GramTaticBoardParser.PlayerActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_playerAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(GramTaticBoardParser.T__3)
            self.state = 30
            self.match(GramTaticBoardParser.T__4)
            self.state = 31
            self.match(GramTaticBoardParser.INT)
            self.state = 32
            self.match(GramTaticBoardParser.T__5)
            self.state = 33
            self.action()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moveAction(self):
            return self.getTypedRuleContext(GramTaticBoardParser.MoveActionContext,0)


        def passAction(self):
            return self.getTypedRuleContext(GramTaticBoardParser.PassActionContext,0)


        def shootAction(self):
            return self.getTypedRuleContext(GramTaticBoardParser.ShootActionContext,0)


        def getRuleIndex(self):
            return GramTaticBoardParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = GramTaticBoardParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_action)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.moveAction()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.passAction()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.shootAction()
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


    class MoveActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GramTaticBoardParser.INT)
            else:
                return self.getToken(GramTaticBoardParser.INT, i)

        def getRuleIndex(self):
            return GramTaticBoardParser.RULE_moveAction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveAction" ):
                listener.enterMoveAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveAction" ):
                listener.exitMoveAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveAction" ):
                return visitor.visitMoveAction(self)
            else:
                return visitor.visitChildren(self)




    def moveAction(self):

        localctx = GramTaticBoardParser.MoveActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_moveAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(GramTaticBoardParser.T__6)
            self.state = 41
            self.match(GramTaticBoardParser.T__4)
            self.state = 42
            self.match(GramTaticBoardParser.INT)
            self.state = 43
            self.match(GramTaticBoardParser.T__7)
            self.state = 44
            self.match(GramTaticBoardParser.INT)
            self.state = 45
            self.match(GramTaticBoardParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PassActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GramTaticBoardParser.INT, 0)

        def getRuleIndex(self):
            return GramTaticBoardParser.RULE_passAction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassAction" ):
                listener.enterPassAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassAction" ):
                listener.exitPassAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPassAction" ):
                return visitor.visitPassAction(self)
            else:
                return visitor.visitChildren(self)




    def passAction(self):

        localctx = GramTaticBoardParser.PassActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_passAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(GramTaticBoardParser.T__8)
            self.state = 48
            self.match(GramTaticBoardParser.T__4)
            self.state = 49
            self.match(GramTaticBoardParser.INT)
            self.state = 50
            self.match(GramTaticBoardParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShootActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramTaticBoardParser.RULE_shootAction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShootAction" ):
                listener.enterShootAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShootAction" ):
                listener.exitShootAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShootAction" ):
                return visitor.visitShootAction(self)
            else:
                return visitor.visitChildren(self)




    def shootAction(self):

        localctx = GramTaticBoardParser.ShootActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_shootAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(GramTaticBoardParser.T__9)
            self.state = 53
            self.match(GramTaticBoardParser.T__4)
            self.state = 54
            self.match(GramTaticBoardParser.T__10)
            self.state = 55
            self.match(GramTaticBoardParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionSetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(GramTaticBoardParser.ID)
            else:
                return self.getToken(GramTaticBoardParser.ID, i)

        def getRuleIndex(self):
            return GramTaticBoardParser.RULE_instructionSet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstructionSet" ):
                listener.enterInstructionSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstructionSet" ):
                listener.exitInstructionSet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructionSet" ):
                return visitor.visitInstructionSet(self)
            else:
                return visitor.visitChildren(self)




    def instructionSet(self):

        localctx = GramTaticBoardParser.InstructionSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_instructionSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(GramTaticBoardParser.T__11)
            self.state = 58
            self.match(GramTaticBoardParser.T__1)
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.match(GramTaticBoardParser.ID)
                self.state = 62 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

            self.state = 64
            self.match(GramTaticBoardParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





