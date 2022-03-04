from ast import parse
from cmath import exp
import sys
from astPrinter import AstPrinter
from interpreter import Interpreter
from parser import Parser
from tokens import Token
from tokentypes import TokenType
from scanner import Scanner


class Lox:

    def __init__(self):
        self.interpreter = Interpreter(self)
        self.hadError = False
        self.hadRuntimeError = False

    # This probably needs work... 4.1.1 system.err.print.ln

    def report(self, line: int, where: str, message: str) -> None:
        print("[line " + str(line) + "] Error" + where + ": " + message)
        self.hadError = True

    def error(self, token: Token, message: str):
        if token.tok_type == TokenType.EOF:
            self.report(token.line, " at end", message)
        else:
            self.report(token.line, " at end", message)

    # def error(self, line: int, message: str) -> None:
    #     self.report(line, "", message)

    def runtimeError(self, error: RuntimeError):
        print(str(error) + "\n[line " + str(error.token.line) + "]")
        self.hadRuntimeError = True

    def runPrompt(self):
        while True:
            try:
                line = input("")
                self.run(line)
                self.hadError = False
            except (EOFError, KeyboardInterrupt) as e:
                print()
                break

    # Is this what pylox should do when one file is passed?
    def runFile(self, path):
        f = open(path, "r")
        lines = f.readlines()

        for line in lines:
            self.run(line)

        # self.run(path)

        # Indicate an error in the exit code
        if (self.hadError):
            exit()
        if self.hadRuntimeError:
            exit()

    def run(self, source: str):
        self.hadError = False
        scanner = Scanner(source, self)
        scanner.scanTokens()
        tokens = scanner.tokens

        parser: Parser = Parser(tokens, self)
        statements = parser.parse()

        # expression = parser.parse()

        if self.hadError:
            return
        self.interpreter.interpret(statements)

        printer = AstPrinter()
        # print(expression)
        # print(printer.printTree(expression))
        # print(AstPrinter().printTree(expression))

        # PREVIOUS TOKEN PRINTING
        # for token in tokens:
        #     print(str(token))

    def main(self):
        if len(sys.argv) > 2:
            print("Usage: pylox [path]")
        elif len(sys.argv) == 2:
            # print(sys.argv[1])
            self.runFile(sys.argv[1])
        else:
            self.runPrompt()


if __name__ == "__main__":
    Lox().main()
