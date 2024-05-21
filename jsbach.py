import sys
import os
import copy
from collections import defaultdict
from queue import LifoQueue
from itertools import takewhile, dropwhile  # let's get haskelly
from functools import reduce

from antlr4 import FileStream, CommonTokenStream
from JSBachVisitor import JSBachVisitor
from JSBachLexer import JSBachLexer
from JSBachParser import JSBachParser

# Visitor class to execute the .jsb program:


def get_note(note_octave: str) -> int:
    """This function parses a note like C4 into its number representation."""
    if len(note_octave) == 1:
        note = note_octave
        octave = 4
    else:
        note, octave = note_octave
    notes = {n: i for i, n in enumerate("CDEFGAB")}
    result = (int(octave)-1)*7 + notes[note] + 2
    if result > 51 or result < 0:
        raise TypeError("Notes should be in the range [A0, C8].")
    return result


def perform_int_op(x: int, op: str, y: int) -> int:
    """This function executes the operation op between x and y and returns its result."""
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        if y == 0:
            raise ZeroDivisionError
        return x / y
    elif op == "^":
        return x ** y
    elif op == "%":
        return x % y


def perform_comparison(x: int, op: str, y: int) -> int:
    """This function evaluates the comparison op between x and y and returns
    a 0 if it is flse, and a one if it is false.
    """
    if op == "=":
        return int(x == y)
    elif op == "/=":
        return int(x != y)
    elif op == "<":
        return int(x < y)
    elif op == ">":
        return int(x > y)
    elif op == "<=":
        return int(x <= y)
    elif op == ">=":
        return int(x >= y)
    else:
        print("Condition Failed")
        return None


class JSBachVisitorExecutor(JSBachVisitor):
    """This class defines a complete generic visitor and executor for a parse
    tree produced by JSBachParser.
    """

    def __init__(self, main_function):
        super(JSBachVisitorExecutor, self).__init__()
        self.notes = list()  # the output notes of the executed program
        self.main_function = main_function
        self.states = LifoQueue()  #  only saves states in the queue at higher levels
        # remember that if a variable is not defined, by default is a 0
        self.current_state = defaultdict(lambda: 0)
        self.procedures = dict()

    def prepare_state_for_proc(self, proc_id, arguments_passed):
        """This functtion prepares a new state
        """
        # first we put a copy of the current state in the stack
        self.states.put(copy.copy(self.current_state))

        new_prepared_state = dict(zip(self.procedures[proc_id]["arguments"],
                                      self.eval_list_of_expr(arguments_passed)))

        self.current_state = new_prepared_state

    def resolve_state_post_proc(self, proc_id: str, arguments_passed: list):
        """This function restores the last state in the states queues and
        updates the lists accordingly
        """
        argument_ids = self.procedures[proc_id]["arguments"]
        passed_text = list(map(lambda x: x.getText(), arguments_passed))
        id2old = dict(zip(passed_text, argument_ids))
        proc_lists = dict(filter(lambda tup: isinstance(tup[1], list) and tup[0] in id2old.keys(),
                                 self.current_state.items()))

        updater = dict(
            map(lambda kv: (id2old[kv[0]], kv[1]), proc_lists.items()))

        self.current_state = self.states.get()
        self.current_state.update(updater)

    def execute_list_of_instructions(self, list_of_instructions: list):
        """This function executes (visits) a list of instructions."""
        for instruction in list_of_instructions:
            self.visit(instruction)

    def eval_list_of_expr(self, list_of_expr: list):
        """This functions takes a list of expresions and evaluates (visits)
        each element returning a list with the result of the evaluation.
        """
        return list(map(lambda expr: self.visit(expr), list_of_expr))

    def check_type_for_lists(self, elements: list, specific_type=None) -> bool:
        """This function returns true if the type of all the elements is the same."""
        if len(elements) == 0:
            return True
        if specific_type is None:
            specific_type = type(elements[0])

        return (not isinstance(specific_type, list)) and reduce(lambda x, y: x and y, map(lambda x: isinstance(x, specific_type), elements))

    def visitRoot(self, ctx: JSBachParser.RootContext):
        """Visit a parse tree produced by JSBachParser#root."""
        for procedure in ctx.getChildren():
            self.visit(procedure)

        main_instructions = self.procedures[self.main_function]["instructions"]
        self.execute_list_of_instructions(main_instructions)
        return self.notes

    def visitProcediment(self, ctx: JSBachParser.ProcedimentContext):
        """Visit a parse tree produced by JSBachParser#procediment."""
        children = list(ctx.getChildren())
        proc_name = children[0].getText()
        if proc_name in self.procedures.keys():
            raise Exception(f"Procedure {proc_name} is already implemented.")

        text_of_children = list(map(lambda x: x.getText(), children))
        self.procedures[proc_name] = {
            "arguments": list(takewhile(lambda x: x != "|:", text_of_children[1:])),
            "instructions": list(dropwhile(lambda x: x.getText() != "|:", children))[1:-1]
        }

    def visitAssig(self, ctx: JSBachParser.AssigContext):
        """Visit a parse tree produced by JSBachParser#assig."""
        varname, _, expr = list(ctx.getChildren())
        self.current_state[varname.getText()] = self.visit(expr)

    def visitWrite(self, ctx: JSBachParser.WriteContext):
        """Visit a parse tree produced by JSBachParser#write."""
        children = list(ctx.getChildren())
        to_write = list(map(lambda x: str(self.visit(x)), children[1:]))
        print(" ".join(to_write))

    def visitRead(self, ctx: JSBachParser.ReadContext):
        """Visit a parse tree produced by JSBachParser#read."""
        _, varname = list(ctx.getChildren())
        value = input()
        self.current_state[varname.getText()] = int(value)

    def visitRepr(self, ctx: JSBachParser.ReprContext):
        """Visit a parse tree produced by JSBachParser#repr."""
        children = list(ctx.getChildren())

        if len(children) == 2:
            to_add = self.visit(children[1])
            if isinstance(to_add, list):
                if not self.check_type_for_lists(to_add, specific_type=tuple):
                    raise TypeError(
                        "Reproduction instruction <:> can only play notes.")
                self.notes.extend(to_add)
            else:
                self.notes.append(to_add)
        else:  # len(children) == 3
            notes_with_duration = self.visit(children[1])
            if not self.check_type_for_lists(notes_with_duration, specific_type=tuple):
                raise TypeError(
                    "Reproduction instruction <:> can only play notes.")
            notes = list(
                map(lambda note_dur: note_dur[0], notes_with_duration))
            lengths = self.visit(children[2])
            if not (isinstance(notes, list) or isinstance(lengths, list)):
                raise TypeError(
                    "If two arguments are passed to <:> both need to be lists.")
            if not self.check_type_for_lists(lengths, specific_type=int):
                raise TypeError(
                    "Duration of notes must be specified by integers")

            self.notes.extend(zip(notes, lengths))

    def visitWhile(self, ctx: JSBachParser.WhileContext):
        """Visit a parse tree produced by JSBachParser#while."""
        children = list(ctx.getChildren())
        condition = children[1]
        while_body = children[3:-1]
        while self.visit(condition):
            print(self.current_state)
            self.execute_list_of_instructions(while_body)

    def visitIfelse(self, ctx: JSBachParser.IfelseContext):
        """Visit a parse tree produced by JSBachParser#ifelse."""
        children = list(ctx.getChildren())
        condition = children[1]
        if self.visit(condition):
            if_body = list(
                takewhile(lambda x: x.getText() != ":|", children[3:]))
            self.execute_list_of_instructions(if_body)
        else:
            else_body = list(dropwhile(lambda x: x.getText()
                                       != "else", children))[1:-1]
            self.execute_list_of_instructions(else_body)

    def visitFuncall(self, ctx: JSBachParser.FuncallContext):
        """Visit a parse tree produced by JSBachParser#funcall."""
        children = list(ctx.getChildren())
        proc_id = children[0].getText()
        if proc_id not in self.procedures.keys():
            raise NotImplementedError(
                f"{proc_id} hasn't been implemented yet.")

        arguments_id = self.procedures[proc_id]["arguments"]
        arguments_passed = children[1:]
        if len(arguments_passed) != len(arguments_id):
            raise TypeError(
                "Expected n arguments recieved m in funcall {proc_id}")

        self.prepare_state_for_proc(proc_id, arguments_passed)

        self.execute_list_of_instructions(
            self.procedures[proc_id]["instructions"])

        self.resolve_state_post_proc(proc_id, arguments_passed)

    def visitAppend(self, ctx: JSBachParser.AppendContext):
        """Visit a parse tree produced by JSBachParser#append."""
        list_id, _, expr2 = list(ctx.getChildren())
        list_ = self.current_state[list_id.getText()]
        element = self.visit(expr2)
        if isinstance(list_, list):
            return list_.append(element)
        else:
            raise TypeError(
                "Append operation can only be performed over lists")

    def visitCut(self, ctx: JSBachParser.CutContext):
        """Visit a parse tree produced by JSBachParser#cut."""
        _, list_id, _, expr2, _ = list(ctx.getChildren())
        try:
            list_ = self.current_state[list_id.getText()]
            index = self.visit(expr2)
            if not isinstance(list_, list):
                raise TypeError("Can only 8< cut >8 elements from lists")
            if not isinstance(index, int):
                raise TypeError("The index of a list must be an integer.")
            if index <= 0 or len(list_) < index:
                raise TypeError(
                    f"List index {index} out of range. remember that JSB indices start at 1.")
            del list_[index-1]  #  remember that JSB is 1 indexed
            self.current_state[list_id.getText()] = list_

        except:
            raise

    def visitNotexpr(self, ctx: JSBachParser.NoteContext):
        """Visit a parse tree produced by JSBachParser#note."""
        children = list(ctx.getChildren())
        return self.visit(children[0])

    def visitOp(self, ctx: JSBachParser.OpContext):
        """Visit a parse tree produced by JSBachParser#op."""
        expr1, op, expr2 = list(ctx.getChildren())
        op = op.getText()
        x, y = self.visit(expr1), self.visit(expr2)

        if isinstance(x, list) or isinstance(y, list):
            raise TypeError("Unsupported operation for lists.")

        if isinstance(y, tuple):
            raise TypeError("Notes can't be operated that way")

        if isinstance(x, tuple):
            # if x is a note we return the result of the operation on the first
            # component of the tuple.
            # The duration of the note is maintained.
            xx = perform_int_op(x[0], op, y)
            if xx > 51 or xx < 0:
                raise TypeError("Notes should be in the range [A0, C8].")
            return (xx, x[1])
        else:
            return perform_int_op(x, op, y)

    def visitString(self, ctx: JSBachParser.StringContext):
        """Visit a parse tree produced by JSBachParser#string."""
        string_ = list(ctx.getChildren())[0]
        return str(string_.getText().strip("\""))

    def visitNum(self, ctx: JSBachParser.NumContext):
        """Visit a parse tree produced by JSBachParser#num."""
        num = list(ctx.getChildren())[0]
        return int(num.getText())

    def visitIndexlist(self, ctx: JSBachParser.IndexlistContext):
        """Visit a parse tree produced by JSBachParser#indexlist."""
        expr1, _, expr2, _ = list(ctx.getChildren())
        try:
            list_ = self.visit(expr1)  # this is very ugly
            index = self.visit(expr2)
            if not isinstance(list_, list):
                raise TypeError("Indexing is only allowed over lists.")
            if not isinstance(index, int):
                raise TypeError("The index of a list must be an integer.")
            if index <= 0 or len(list_) < index:
                raise TypeError(
                    f"List index {index} out of range. remember that JSB indices start at 1.")

            return list_[index-1]  # remember that JSB is 1 indexed

        except:
            print(ctx.getText())
            raise

    def visitId(self, ctx: JSBachParser.IdContext):
        """Visit a parse tree produced by JSBachParser#id."""
        id_ = list(ctx.getChildren())[0]
        return self.current_state[id_.getText()]

    # Visit a parse tree produced by JSBachParser#list.
    def visitList(self, ctx: JSBachParser.ListContext):
        children = list(ctx.getChildren())
        # the first and last children are tokens'{' and '}' respectively
        list_content = children[1:-1]
        content = self.eval_list_of_expr(list_content)
        if not self.check_type_for_lists(content):
            raise TypeError(
                "List can only be formed by integers or notes homogeneously")
        return content

    # Visit a parse tree produced by JSBachParser#parenthesis.
    def visitParenthesis(self, ctx: JSBachParser.ParenthesisContext):
        _, expr, _ = list(ctx.getChildren())
        return self.visit(expr)

    # Visit a parse tree produced by JSBachParser#listlen.
    def visitListlen(self, ctx: JSBachParser.ListlenContext):
        _, expr = list(ctx.getChildren())
        list_ = self.visit(expr)
        if isinstance(list_, list):
            return len(list_)
        else:
            raise TypeError(f"{type(list_)} object has no lenght")

    # Visit a parse tree produced by JSBachParser#condition.
    def visitCondition(self, ctx: JSBachParser.ConditionContext):
        # =, /=, <, >, <=, >=)
        expr1, op, expr2 = list(ctx.getChildren())
        op = op.getText()
        x = self.visit(expr1)
        y = self.visit(expr2)
        if not type(x) == type(y):
            raise TypeError("Only elements of the same type can be compared.")
        if isinstance(x, list) or isinstance(y, list):
            raise TypeError("Only notes and integers can be compared.")

        if isinstance(x, tuple) and isinstance(y, tuple):
            x = x[0]
            y = y[0]

        return perform_comparison(x, op, y)

    def visitBasenote(self, ctx: JSBachParser.BasenoteContext):
        """Visit a parse tree produced by JSBachParser#basenote."""
        base_note = list(ctx.getChildren())[0]
        # by default the duration is 4
        return (get_note(base_note.getText()), 4)

    def visitNoteDuration(self, ctx: JSBachParser.NoteDurationContext):
        """Visit a parse tree produced by JSBachParser#noteDuration."""
        note, duration = list(ctx.getChildren())
        return (get_note(note.getText()), int(duration.getText()))


def get_main_function(args: list) -> str:
    if len(args) >= 3:
        return args[2]
    else:
        return "Main"


def get_note_inverse(note_num: int) -> str:
    """This function transforms a note in {0,...,51} into its representation in
    lilypond using the note and the commas to determine the octave.
    """
    note = note_num % 7
    notes = {i: n for i, n in enumerate("abcdefg")}
    octave = int((note_num+5) / 7)
    commas = ("," if octave < 3 else "\'") * abs(octave-3)
    return notes[note] + commas


def print_notes(note_list):
    result = " "*8
    result = reduce(
        lambda x, tup: x+get_note_inverse(tup[0])+str(tup[1])+" ", note_list, result)
    return result + "\n"


def generate_lilypond(note_list: list, dest: str):
    """This function generates the lilypond file in the specified dest directory."""
    with open(dest, "w") as f:
        f.write("\\version \"2.22.1\"\n")
        f.write("\\score {\n")
        f.write("    \\absolute {\n")
        f.write("        \\tempo 4 = 120\n")
        f.write(print_notes(note_list))
        f.write("    }\n")
        f.write("    \\layout { }\n")
        f.write("    \\midi { }\n")
        f.write("}\n")


def compile_output_music(note_list: list, dest: str):
    # the run_id eliminates the possible prefix in the case the script is in a folder
    run_id = dest.split("/")[-1][:-4]
    lilypond_filename = run_id + ".lily"
    generate_lilypond(note_list, lilypond_filename)

    os.system(f"lilypond {lilypond_filename}")

    os.system(f"timidity -Ow -o {run_id}.wav {run_id}.midi")

    os.system(
        f"ffmpeg -i {run_id}.wav -codec:a libmp3lame -qscale:a 4 {run_id}.mp3")


def main(args):
    program_input_stream = FileStream(args[1])
    lexer = JSBachLexer(program_input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = JSBachParser(token_stream)
    tree = parser.root()
    main_function = get_main_function(args)
    visitor = JSBachVisitorExecutor(main_function)
    notes = visitor.visit(tree)
    if len(notes) > 0:
        compile_output_music(notes, args[1])


if __name__ == "__main__":
    main(sys.argv)
