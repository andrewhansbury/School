import sys
from scanner import Scanner


class Lox:

    def __init__(self):
        self.hadError = False

    # This probably needs work... 4.1.1 system.err.print.ln

    def report(self, line: int, where: str, message: str) -> None:
        print("[line " + line + "] Error" + where + ": " + message)
        self.hadError = True

    def error(self, line: int, message: str) -> None:
        self.report(line, "", message)

    def runPrompt(self):
        while True:
            try:
                line = input("> ")
                self.run(line)
                self.hadError = False
            except (EOFError, KeyboardInterrupt) as e:
                print()
                break

    # Is this what pylox should do when one file is passed?
    # how to make the equivalent System.exit(65)... what is
    # the 65?

    def runFile(self, path):
        print(type(path))
        exec(path)
        # Indicate an error in the exit code
        if (self.hadError):
            exit()

    def run(self, source: str):

        scanner = Scanner(source, self)
        scanner.scanTokens()
        tokens = scanner.tokens

        for token in tokens:
            print(str(token))

    def main(self):
        if len(sys.argv) > 2:
            print("Usage: pylox [path]")
        elif len(sys.argv) == 2:
            print(sys.argv[1])
            self.runFile(sys.argv[1])
        else:
            self.runPrompt()


if __name__ == "__main__":
    Lox().main()
