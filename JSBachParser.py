# Generated from JSBach.g4 by ANTLR 4.10.1
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
        4,1,35,151,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,
        1,1,1,1,1,4,1,29,8,1,11,1,12,1,30,1,1,1,1,1,2,1,2,1,2,1,2,1,2,4,
        2,40,8,2,11,2,12,2,41,1,2,1,2,1,2,1,2,1,2,3,2,49,8,2,1,2,1,2,1,2,
        1,2,4,2,55,8,2,11,2,12,2,56,1,2,1,2,1,2,1,2,1,2,1,2,4,2,65,8,2,11,
        2,12,2,66,1,2,1,2,1,2,1,2,4,2,73,8,2,11,2,12,2,74,1,2,1,2,3,2,79,
        8,2,1,2,1,2,5,2,83,8,2,10,2,12,2,86,9,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,97,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,
        3,109,8,3,10,3,12,3,112,9,3,1,3,1,3,1,3,1,3,3,3,118,8,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,134,8,3,10,3,
        12,3,137,9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,149,8,5,
        1,5,0,1,6,6,0,2,4,6,8,10,0,2,2,0,21,22,25,25,1,0,23,24,176,0,13,
        1,0,0,0,2,19,1,0,0,0,4,96,1,0,0,0,6,117,1,0,0,0,8,138,1,0,0,0,10,
        148,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,
        0,0,15,16,1,0,0,0,16,17,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,23,
        5,31,0,0,20,22,5,30,0,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,
        0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,28,5,2,0,0,27,29,
        3,4,2,0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,
        31,32,1,0,0,0,32,33,5,3,0,0,33,3,1,0,0,0,34,35,5,30,0,0,35,36,5,
        10,0,0,36,97,3,6,3,0,37,39,5,11,0,0,38,40,3,6,3,0,39,38,1,0,0,0,
        40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,97,1,0,0,0,43,44,5,
        12,0,0,44,97,5,30,0,0,45,46,5,13,0,0,46,48,3,6,3,0,47,49,3,6,3,0,
        48,47,1,0,0,0,48,49,1,0,0,0,49,97,1,0,0,0,50,51,5,14,0,0,51,52,3,
        8,4,0,52,54,5,2,0,0,53,55,3,4,2,0,54,53,1,0,0,0,55,56,1,0,0,0,56,
        54,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,5,3,0,0,59,97,1,0,0,
        0,60,61,5,15,0,0,61,62,3,8,4,0,62,64,5,2,0,0,63,65,3,4,2,0,64,63,
        1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,
        68,78,5,3,0,0,69,70,5,16,0,0,70,72,5,2,0,0,71,73,3,4,2,0,72,71,1,
        0,0,0,73,74,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,76,
        77,5,3,0,0,77,79,1,0,0,0,78,69,1,0,0,0,78,79,1,0,0,0,79,97,1,0,0,
        0,80,84,5,31,0,0,81,83,3,6,3,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,
        1,0,0,0,84,85,1,0,0,0,85,97,1,0,0,0,86,84,1,0,0,0,87,88,5,30,0,0,
        88,89,5,17,0,0,89,97,3,6,3,0,90,91,5,18,0,0,91,92,5,30,0,0,92,93,
        5,8,0,0,93,94,3,6,3,0,94,95,5,9,0,0,95,97,1,0,0,0,96,34,1,0,0,0,
        96,37,1,0,0,0,96,43,1,0,0,0,96,45,1,0,0,0,96,50,1,0,0,0,96,60,1,
        0,0,0,96,80,1,0,0,0,96,87,1,0,0,0,96,90,1,0,0,0,97,5,1,0,0,0,98,
        99,6,3,-1,0,99,100,5,6,0,0,100,101,3,6,3,0,101,102,5,7,0,0,102,118,
        1,0,0,0,103,118,5,19,0,0,104,118,3,10,5,0,105,118,5,32,0,0,106,110,
        5,4,0,0,107,109,3,6,3,0,108,107,1,0,0,0,109,112,1,0,0,0,110,108,
        1,0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,110,1,0,0,0,113,118,
        5,5,0,0,114,118,5,30,0,0,115,116,5,27,0,0,116,118,3,6,3,2,117,98,
        1,0,0,0,117,103,1,0,0,0,117,104,1,0,0,0,117,105,1,0,0,0,117,106,
        1,0,0,0,117,114,1,0,0,0,117,115,1,0,0,0,118,135,1,0,0,0,119,120,
        10,10,0,0,120,121,5,20,0,0,121,134,3,6,3,10,122,123,10,9,0,0,123,
        124,7,0,0,0,124,134,3,6,3,10,125,126,10,8,0,0,126,127,7,1,0,0,127,
        134,3,6,3,9,128,129,10,1,0,0,129,130,5,8,0,0,130,131,3,6,3,0,131,
        132,5,9,0,0,132,134,1,0,0,0,133,119,1,0,0,0,133,122,1,0,0,0,133,
        125,1,0,0,0,133,128,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,
        136,1,0,0,0,136,7,1,0,0,0,137,135,1,0,0,0,138,139,3,6,3,0,139,140,
        5,26,0,0,140,141,3,6,3,0,141,9,1,0,0,0,142,143,5,29,0,0,143,149,
        5,19,0,0,144,145,5,28,0,0,145,149,5,19,0,0,146,149,5,28,0,0,147,
        149,5,29,0,0,148,142,1,0,0,0,148,144,1,0,0,0,148,146,1,0,0,0,148,
        147,1,0,0,0,149,11,1,0,0,0,16,15,23,30,41,48,56,66,74,78,84,96,110,
        117,133,135,148
    ]

class JSBachParser ( Parser ):

    grammarFileName = "JSBach.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'|:'", "':|'", "'{'", "'}'", 
                     "'('", "')'", "'['", "']'", "'<-'", "'<!>'", "'<?>'", 
                     "'<:>'", "'while'", "'if'", "'else'", "'<<'", "'8<'", 
                     "<INVALID>", "'^'", "'*'", "'/'", "'+'", "'-'", "'%'", 
                     "<INVALID>", "'#'" ]

    symbolicNames = [ "<INVALID>", "LINE_COMMENT", "OPENKEY", "CLOSEKEY", 
                      "OPENLIST", "CLOSELIST", "OPENPARENTHESIS", "CLOSEPARENTHESIS", 
                      "OPENBRACKET", "CLOSEBRACKET", "ASSIG", "WRITE", "READ", 
                      "REPR", "WHILE", "IF", "ELSE", "APPEND", "CUT", "NUM", 
                      "POWER", "STAR", "DIV", "PLUS", "MINUS", "MOD", "RELATION", 
                      "LEN", "BASE_NOTE", "NOTE_OCTAVE", "VAR_ID", "PROC_ID", 
                      "STRING", "LETTER", "DIGIT", "WS" ]

    RULE_root = 0
    RULE_procediment = 1
    RULE_instruction = 2
    RULE_expr = 3
    RULE_condition = 4
    RULE_note = 5

    ruleNames =  [ "root", "procediment", "instruction", "expr", "condition", 
                   "note" ]

    EOF = Token.EOF
    LINE_COMMENT=1
    OPENKEY=2
    CLOSEKEY=3
    OPENLIST=4
    CLOSELIST=5
    OPENPARENTHESIS=6
    CLOSEPARENTHESIS=7
    OPENBRACKET=8
    CLOSEBRACKET=9
    ASSIG=10
    WRITE=11
    READ=12
    REPR=13
    WHILE=14
    IF=15
    ELSE=16
    APPEND=17
    CUT=18
    NUM=19
    POWER=20
    STAR=21
    DIV=22
    PLUS=23
    MINUS=24
    MOD=25
    RELATION=26
    LEN=27
    BASE_NOTE=28
    NOTE_OCTAVE=29
    VAR_ID=30
    PROC_ID=31
    STRING=32
    LETTER=33
    DIGIT=34
    WS=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(JSBachParser.EOF, 0)

        def procediment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSBachParser.ProcedimentContext)
            else:
                return self.getTypedRuleContext(JSBachParser.ProcedimentContext,i)


        def getRuleIndex(self):
            return JSBachParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = JSBachParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.procediment()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==JSBachParser.PROC_ID):
                    break

            self.state = 17
            self.match(JSBachParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedimentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROC_ID(self):
            return self.getToken(JSBachParser.PROC_ID, 0)

        def OPENKEY(self):
            return self.getToken(JSBachParser.OPENKEY, 0)

        def CLOSEKEY(self):
            return self.getToken(JSBachParser.CLOSEKEY, 0)

        def VAR_ID(self, i:int=None):
            if i is None:
                return self.getTokens(JSBachParser.VAR_ID)
            else:
                return self.getToken(JSBachParser.VAR_ID, i)

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSBachParser.InstructionContext)
            else:
                return self.getTypedRuleContext(JSBachParser.InstructionContext,i)


        def getRuleIndex(self):
            return JSBachParser.RULE_procediment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcediment" ):
                return visitor.visitProcediment(self)
            else:
                return visitor.visitChildren(self)




    def procediment(self):

        localctx = JSBachParser.ProcedimentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_procediment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(JSBachParser.PROC_ID)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JSBachParser.VAR_ID:
                self.state = 20
                self.match(JSBachParser.VAR_ID)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(JSBachParser.OPENKEY)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.instruction()
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSBachParser.WRITE) | (1 << JSBachParser.READ) | (1 << JSBachParser.REPR) | (1 << JSBachParser.WHILE) | (1 << JSBachParser.IF) | (1 << JSBachParser.CUT) | (1 << JSBachParser.VAR_ID) | (1 << JSBachParser.PROC_ID))) != 0)):
                    break

            self.state = 32
            self.match(JSBachParser.CLOSEKEY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSBachParser.RULE_instruction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReprContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REPR(self):
            return self.getToken(JSBachParser.REPR, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSBachParser.ExprContext)
            else:
                return self.getTypedRuleContext(JSBachParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepr" ):
                return visitor.visitRepr(self)
            else:
                return visitor.visitChildren(self)


    class FuncallContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PROC_ID(self):
            return self.getToken(JSBachParser.PROC_ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSBachParser.ExprContext)
            else:
                return self.getTypedRuleContext(JSBachParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)


    class AssigContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR_ID(self):
            return self.getToken(JSBachParser.VAR_ID, 0)
        def ASSIG(self):
            return self.getToken(JSBachParser.ASSIG, 0)
        def expr(self):
            return self.getTypedRuleContext(JSBachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)


    class ReadContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(JSBachParser.READ, 0)
        def VAR_ID(self):
            return self.getToken(JSBachParser.VAR_ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)


    class CutContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CUT(self):
            return self.getToken(JSBachParser.CUT, 0)
        def VAR_ID(self):
            return self.getToken(JSBachParser.VAR_ID, 0)
        def OPENBRACKET(self):
            return self.getToken(JSBachParser.OPENBRACKET, 0)
        def expr(self):
            return self.getTypedRuleContext(JSBachParser.ExprContext,0)

        def CLOSEBRACKET(self):
            return self.getToken(JSBachParser.CLOSEBRACKET, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCut" ):
                return visitor.visitCut(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(JSBachParser.WHILE, 0)
        def condition(self):
            return self.getTypedRuleContext(JSBachParser.ConditionContext,0)

        def OPENKEY(self):
            return self.getToken(JSBachParser.OPENKEY, 0)
        def CLOSEKEY(self):
            return self.getToken(JSBachParser.CLOSEKEY, 0)
        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSBachParser.InstructionContext)
            else:
                return self.getTypedRuleContext(JSBachParser.InstructionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class WriteContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(JSBachParser.WRITE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSBachParser.ExprContext)
            else:
                return self.getTypedRuleContext(JSBachParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


    class AppendContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR_ID(self):
            return self.getToken(JSBachParser.VAR_ID, 0)
        def APPEND(self):
            return self.getToken(JSBachParser.APPEND, 0)
        def expr(self):
            return self.getTypedRuleContext(JSBachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAppend" ):
                return visitor.visitAppend(self)
            else:
                return visitor.visitChildren(self)


    class IfelseContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(JSBachParser.IF, 0)
        def condition(self):
            return self.getTypedRuleContext(JSBachParser.ConditionContext,0)

        def OPENKEY(self, i:int=None):
            if i is None:
                return self.getTokens(JSBachParser.OPENKEY)
            else:
                return self.getToken(JSBachParser.OPENKEY, i)
        def CLOSEKEY(self, i:int=None):
            if i is None:
                return self.getTokens(JSBachParser.CLOSEKEY)
            else:
                return self.getToken(JSBachParser.CLOSEKEY, i)
        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSBachParser.InstructionContext)
            else:
                return self.getTypedRuleContext(JSBachParser.InstructionContext,i)

        def ELSE(self):
            return self.getToken(JSBachParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse" ):
                return visitor.visitIfelse(self)
            else:
                return visitor.visitChildren(self)



    def instruction(self):

        localctx = JSBachParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruction)
        self._la = 0 # Token type
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = JSBachParser.AssigContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(JSBachParser.VAR_ID)
                self.state = 35
                self.match(JSBachParser.ASSIG)
                self.state = 36
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = JSBachParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(JSBachParser.WRITE)
                self.state = 39 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 38
                        self.expr(0)

                    else:
                        raise NoViableAltException(self)
                    self.state = 41 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass

            elif la_ == 3:
                localctx = JSBachParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(JSBachParser.READ)
                self.state = 44
                self.match(JSBachParser.VAR_ID)
                pass

            elif la_ == 4:
                localctx = JSBachParser.ReprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(JSBachParser.REPR)
                self.state = 46
                self.expr(0)
                self.state = 48
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 47
                    self.expr(0)


                pass

            elif la_ == 5:
                localctx = JSBachParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.match(JSBachParser.WHILE)
                self.state = 51
                self.condition()
                self.state = 52
                self.match(JSBachParser.OPENKEY)
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 53
                    self.instruction()
                    self.state = 56 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSBachParser.WRITE) | (1 << JSBachParser.READ) | (1 << JSBachParser.REPR) | (1 << JSBachParser.WHILE) | (1 << JSBachParser.IF) | (1 << JSBachParser.CUT) | (1 << JSBachParser.VAR_ID) | (1 << JSBachParser.PROC_ID))) != 0)):
                        break

                self.state = 58
                self.match(JSBachParser.CLOSEKEY)
                pass

            elif la_ == 6:
                localctx = JSBachParser.IfelseContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 60
                self.match(JSBachParser.IF)
                self.state = 61
                self.condition()
                self.state = 62
                self.match(JSBachParser.OPENKEY)
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 63
                    self.instruction()
                    self.state = 66 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSBachParser.WRITE) | (1 << JSBachParser.READ) | (1 << JSBachParser.REPR) | (1 << JSBachParser.WHILE) | (1 << JSBachParser.IF) | (1 << JSBachParser.CUT) | (1 << JSBachParser.VAR_ID) | (1 << JSBachParser.PROC_ID))) != 0)):
                        break

                self.state = 68
                self.match(JSBachParser.CLOSEKEY)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JSBachParser.ELSE:
                    self.state = 69
                    self.match(JSBachParser.ELSE)
                    self.state = 70
                    self.match(JSBachParser.OPENKEY)
                    self.state = 72 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 71
                        self.instruction()
                        self.state = 74 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSBachParser.WRITE) | (1 << JSBachParser.READ) | (1 << JSBachParser.REPR) | (1 << JSBachParser.WHILE) | (1 << JSBachParser.IF) | (1 << JSBachParser.CUT) | (1 << JSBachParser.VAR_ID) | (1 << JSBachParser.PROC_ID))) != 0)):
                            break

                    self.state = 76
                    self.match(JSBachParser.CLOSEKEY)


                pass

            elif la_ == 7:
                localctx = JSBachParser.FuncallContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.match(JSBachParser.PROC_ID)
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 81
                        self.expr(0) 
                    self.state = 86
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass

            elif la_ == 8:
                localctx = JSBachParser.AppendContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 87
                self.match(JSBachParser.VAR_ID)
                self.state = 88
                self.match(JSBachParser.APPEND)
                self.state = 89
                self.expr(0)
                pass

            elif la_ == 9:
                localctx = JSBachParser.CutContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 90
                self.match(JSBachParser.CUT)
                self.state = 91
                self.match(JSBachParser.VAR_ID)
                self.state = 92
                self.match(JSBachParser.OPENBRACKET)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.match(JSBachParser.CLOSEBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSBachParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NotexprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def note(self):
            return self.getTypedRuleContext(JSBachParser.NoteContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotexpr" ):
                return visitor.visitNotexpr(self)
            else:
                return visitor.visitChildren(self)


    class OpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSBachParser.ExprContext)
            else:
                return self.getTypedRuleContext(JSBachParser.ExprContext,i)

        def POWER(self):
            return self.getToken(JSBachParser.POWER, 0)
        def STAR(self):
            return self.getToken(JSBachParser.STAR, 0)
        def DIV(self):
            return self.getToken(JSBachParser.DIV, 0)
        def MOD(self):
            return self.getToken(JSBachParser.MOD, 0)
        def PLUS(self):
            return self.getToken(JSBachParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(JSBachParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(JSBachParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(JSBachParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class IndexlistContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSBachParser.ExprContext)
            else:
                return self.getTypedRuleContext(JSBachParser.ExprContext,i)

        def OPENBRACKET(self):
            return self.getToken(JSBachParser.OPENBRACKET, 0)
        def CLOSEBRACKET(self):
            return self.getToken(JSBachParser.CLOSEBRACKET, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexlist" ):
                return visitor.visitIndexlist(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR_ID(self):
            return self.getToken(JSBachParser.VAR_ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class ListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPENLIST(self):
            return self.getToken(JSBachParser.OPENLIST, 0)
        def CLOSELIST(self):
            return self.getToken(JSBachParser.CLOSELIST, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSBachParser.ExprContext)
            else:
                return self.getTypedRuleContext(JSBachParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPENPARENTHESIS(self):
            return self.getToken(JSBachParser.OPENPARENTHESIS, 0)
        def expr(self):
            return self.getTypedRuleContext(JSBachParser.ExprContext,0)

        def CLOSEPARENTHESIS(self):
            return self.getToken(JSBachParser.CLOSEPARENTHESIS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class ListlenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEN(self):
            return self.getToken(JSBachParser.LEN, 0)
        def expr(self):
            return self.getTypedRuleContext(JSBachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListlen" ):
                return visitor.visitListlen(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = JSBachParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSBachParser.OPENPARENTHESIS]:
                localctx = JSBachParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 99
                self.match(JSBachParser.OPENPARENTHESIS)
                self.state = 100
                self.expr(0)
                self.state = 101
                self.match(JSBachParser.CLOSEPARENTHESIS)
                pass
            elif token in [JSBachParser.NUM]:
                localctx = JSBachParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 103
                self.match(JSBachParser.NUM)
                pass
            elif token in [JSBachParser.BASE_NOTE, JSBachParser.NOTE_OCTAVE]:
                localctx = JSBachParser.NotexprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 104
                self.note()
                pass
            elif token in [JSBachParser.STRING]:
                localctx = JSBachParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 105
                self.match(JSBachParser.STRING)
                pass
            elif token in [JSBachParser.OPENLIST]:
                localctx = JSBachParser.ListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(JSBachParser.OPENLIST)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSBachParser.OPENLIST) | (1 << JSBachParser.OPENPARENTHESIS) | (1 << JSBachParser.NUM) | (1 << JSBachParser.LEN) | (1 << JSBachParser.BASE_NOTE) | (1 << JSBachParser.NOTE_OCTAVE) | (1 << JSBachParser.VAR_ID) | (1 << JSBachParser.STRING))) != 0):
                    self.state = 107
                    self.expr(0)
                    self.state = 112
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 113
                self.match(JSBachParser.CLOSELIST)
                pass
            elif token in [JSBachParser.VAR_ID]:
                localctx = JSBachParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 114
                self.match(JSBachParser.VAR_ID)
                pass
            elif token in [JSBachParser.LEN]:
                localctx = JSBachParser.ListlenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(JSBachParser.LEN)
                self.state = 116
                self.expr(2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 133
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = JSBachParser.OpContext(self, JSBachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 119
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 120
                        self.match(JSBachParser.POWER)
                        self.state = 121
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = JSBachParser.OpContext(self, JSBachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 123
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSBachParser.STAR) | (1 << JSBachParser.DIV) | (1 << JSBachParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 124
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = JSBachParser.OpContext(self, JSBachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 125
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 126
                        _la = self._input.LA(1)
                        if not(_la==JSBachParser.PLUS or _la==JSBachParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 127
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = JSBachParser.IndexlistContext(self, JSBachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 128
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 129
                        self.match(JSBachParser.OPENBRACKET)
                        self.state = 130
                        self.expr(0)
                        self.state = 131
                        self.match(JSBachParser.CLOSEBRACKET)
                        pass

             
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSBachParser.ExprContext)
            else:
                return self.getTypedRuleContext(JSBachParser.ExprContext,i)


        def RELATION(self):
            return self.getToken(JSBachParser.RELATION, 0)

        def getRuleIndex(self):
            return JSBachParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = JSBachParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.expr(0)
            self.state = 139
            self.match(JSBachParser.RELATION)
            self.state = 140
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSBachParser.RULE_note

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NoteDurationContext(NoteContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.NoteContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOTE_OCTAVE(self):
            return self.getToken(JSBachParser.NOTE_OCTAVE, 0)
        def NUM(self):
            return self.getToken(JSBachParser.NUM, 0)
        def BASE_NOTE(self):
            return self.getToken(JSBachParser.BASE_NOTE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoteDuration" ):
                return visitor.visitNoteDuration(self)
            else:
                return visitor.visitChildren(self)


    class BasenoteContext(NoteContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSBachParser.NoteContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BASE_NOTE(self):
            return self.getToken(JSBachParser.BASE_NOTE, 0)
        def NOTE_OCTAVE(self):
            return self.getToken(JSBachParser.NOTE_OCTAVE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasenote" ):
                return visitor.visitBasenote(self)
            else:
                return visitor.visitChildren(self)



    def note(self):

        localctx = JSBachParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_note)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = JSBachParser.NoteDurationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(JSBachParser.NOTE_OCTAVE)
                self.state = 143
                self.match(JSBachParser.NUM)
                pass

            elif la_ == 2:
                localctx = JSBachParser.NoteDurationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(JSBachParser.BASE_NOTE)
                self.state = 145
                self.match(JSBachParser.NUM)
                pass

            elif la_ == 3:
                localctx = JSBachParser.BasenoteContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.match(JSBachParser.BASE_NOTE)
                pass

            elif la_ == 4:
                localctx = JSBachParser.BasenoteContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.match(JSBachParser.NOTE_OCTAVE)
                pass


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
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




