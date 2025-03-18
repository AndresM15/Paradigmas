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


    # Visit a parse tree produced by GramTaticBoardParser#playerAction.
    def visitPlayerAction(self, ctx:GramTaticBoardParser.PlayerActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramTaticBoardParser#action.
    def visitAction(self, ctx:GramTaticBoardParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramTaticBoardParser#move.
    def visitMove(self, ctx:GramTaticBoardParser.MoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramTaticBoardParser#pass.
    def visitPass(self, ctx:GramTaticBoardParser.PassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramTaticBoardParser#shoot.
    def visitShootAction(self, ctx: GramTaticBoardParser.ShootActionContext):
        ...




del GramTaticBoardParser