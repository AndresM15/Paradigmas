# Generated from GramTaticBoard.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GramTaticBoardParser import GramTaticBoardParser
else:
    from GramTaticBoardParser import GramTaticBoardParser

# This class defines a complete listener for a parse tree produced by GramTaticBoardParser.
class GramTaticBoardListener(ParseTreeListener):

    # Enter a parse tree produced by GramTaticBoardParser#tactic.
    def enterTactic(self, ctx:GramTaticBoardParser.TacticContext):
        pass

    # Exit a parse tree produced by GramTaticBoardParser#tactic.
    def exitTactic(self, ctx:GramTaticBoardParser.TacticContext):
        pass


    # Enter a parse tree produced by GramTaticBoardParser#statement.
    def enterStatement(self, ctx:GramTaticBoardParser.StatementContext):
        pass

    # Exit a parse tree produced by GramTaticBoardParser#statement.
    def exitStatement(self, ctx:GramTaticBoardParser.StatementContext):
        pass


    # Enter a parse tree produced by GramTaticBoardParser#playerAction.
    def enterPlayerAction(self, ctx:GramTaticBoardParser.PlayerActionContext):
        pass

    # Exit a parse tree produced by GramTaticBoardParser#playerAction.
    def exitPlayerAction(self, ctx:GramTaticBoardParser.PlayerActionContext):
        pass


    # Enter a parse tree produced by GramTaticBoardParser#action.
    def enterAction(self, ctx:GramTaticBoardParser.ActionContext):
        pass

    # Exit a parse tree produced by GramTaticBoardParser#action.
    def exitAction(self, ctx:GramTaticBoardParser.ActionContext):
        pass


    # Enter a parse tree produced by GramTaticBoardParser#moveAction.
    def enterMoveAction(self, ctx:GramTaticBoardParser.MoveActionContext):
        pass

    # Exit a parse tree produced by GramTaticBoardParser#moveAction.
    def exitMoveAction(self, ctx:GramTaticBoardParser.MoveActionContext):
        pass


    # Enter a parse tree produced by GramTaticBoardParser#passAction.
    def enterPassAction(self, ctx:GramTaticBoardParser.PassActionContext):
        pass

    # Exit a parse tree produced by GramTaticBoardParser#passAction.
    def exitPassAction(self, ctx:GramTaticBoardParser.PassActionContext):
        pass


    # Enter a parse tree produced by GramTaticBoardParser#shootAction.
    def enterShootAction(self, ctx:GramTaticBoardParser.ShootActionContext):
        pass

    # Exit a parse tree produced by GramTaticBoardParser#shootAction.
    def exitShootAction(self, ctx:GramTaticBoardParser.ShootActionContext):
        pass



del GramTaticBoardParser