# Generated from GramTaticBoard.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GramTaticBoardParser import GramTaticBoardParser
else:
    from GramTaticBoardParser import GramTaticBoardParser

# This class defines a complete generic visitor for a parse tree produced by GramTaticBoardParser.

class GramTaticBoardVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramTaticBoardParser#tactic.
    def visitTactic(self, ctx:GramTaticBoardParser.TacticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramTaticBoardParser#statement.
    def visitStatement(self, ctx:GramTaticBoardParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramTaticBoardParser#playerAction.
    def visitPlayerAction(self, ctx:GramTaticBoardParser.PlayerActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramTaticBoardParser#action.
    def visitAction(self, ctx:GramTaticBoardParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramTaticBoardParser#moveAction.
    def visitMoveAction(self, ctx:GramTaticBoardParser.MoveActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramTaticBoardParser#passAction.
    def visitPassAction(self, ctx:GramTaticBoardParser.PassActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramTaticBoardParser#shootAction.
    def visitShootAction(self, ctx:GramTaticBoardParser.ShootActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramTaticBoardParser#instructionSet.
    def visitInstructionSet(self, ctx:GramTaticBoardParser.InstructionSetContext):
        return self.visitChildren(ctx)



del GramTaticBoardParser