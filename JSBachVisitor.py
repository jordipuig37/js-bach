# Generated from JSBach.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JSBachParser import JSBachParser
else:
    from JSBachParser import JSBachParser

# This class defines a complete generic visitor for a parse tree produced by JSBachParser.

class JSBachVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JSBachParser#root.
    def visitRoot(self, ctx:JSBachParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#procediment.
    def visitProcediment(self, ctx:JSBachParser.ProcedimentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#assig.
    def visitAssig(self, ctx:JSBachParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#write.
    def visitWrite(self, ctx:JSBachParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#read.
    def visitRead(self, ctx:JSBachParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#repr.
    def visitRepr(self, ctx:JSBachParser.ReprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#while.
    def visitWhile(self, ctx:JSBachParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#ifelse.
    def visitIfelse(self, ctx:JSBachParser.IfelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#funcall.
    def visitFuncall(self, ctx:JSBachParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#append.
    def visitAppend(self, ctx:JSBachParser.AppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#cut.
    def visitCut(self, ctx:JSBachParser.CutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#notexpr.
    def visitNotexpr(self, ctx:JSBachParser.NotexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#op.
    def visitOp(self, ctx:JSBachParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#string.
    def visitString(self, ctx:JSBachParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#num.
    def visitNum(self, ctx:JSBachParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#indexlist.
    def visitIndexlist(self, ctx:JSBachParser.IndexlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#id.
    def visitId(self, ctx:JSBachParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#list.
    def visitList(self, ctx:JSBachParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#parenthesis.
    def visitParenthesis(self, ctx:JSBachParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#listlen.
    def visitListlen(self, ctx:JSBachParser.ListlenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#condition.
    def visitCondition(self, ctx:JSBachParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#noteDuration.
    def visitNoteDuration(self, ctx:JSBachParser.NoteDurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSBachParser#basenote.
    def visitBasenote(self, ctx:JSBachParser.BasenoteContext):
        return self.visitChildren(ctx)



del JSBachParser