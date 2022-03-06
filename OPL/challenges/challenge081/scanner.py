from tokentypes import TokenType
from tokens import Token


class Scanner:
    def __init__(self, source, Lox):
        self.Lox = Lox
        self.source: str = source
        self.tokens = []

        self.start = 0
        self.current = 0
        self.line = 1

        self.keywords = {

            "and": TokenType.AND,
            "class": TokenType.CLASS,
            "else": TokenType.ELSE,
            "false": TokenType.FALSE,
            "for": TokenType.FOR,
            "fun": TokenType.FUN,
            "if": TokenType.IF,
            "nil": TokenType.NIL,
            "or": TokenType.OR,
            "print": TokenType.PRINT,
            "return": TokenType.RETURN,
            "super": TokenType.SUPER,
            "this": TokenType.THIS,
            "true": TokenType.TRUE,
            "var": TokenType.VAR,
            "while": TokenType.WHILE,
        }

    def scanTokens(self) -> 'list[Token]':
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def isAtEnd(self):
        return self.current >= len(self.source)

    def scanToken(self):
        case = self.advance()

        if case == '(':
            self.addToken(TokenType.LEFT_PAREN)
        elif case == ')':
            self.addToken(TokenType.RIGHT_PAREN)
        elif case == '{':
            self.addToken(TokenType.LEFT_BRACE)
        elif case == '}':
            self.addToken(TokenType.RIGHT_BRACE)
        elif case == ',':
            self.addToken(TokenType.COMMA)
        elif case == '.':
            self.addToken(TokenType.DOT)
        elif case == '-':
            self.addToken(TokenType.MINUS)
        elif case == '+':
            self.addToken(TokenType.PLUS)
        elif case == ';':
            self.addToken(TokenType.SEMICOLON)
        elif case == '*':
            self.addToken(TokenType.STAR)

        elif case == '!':
            value = TokenType.BANG_EQUAL if self.match(
                '=') else TokenType.BANG
            self.addToken(value)
        elif case == '=':
            value = TokenType.EQUAL_EQUAL if self.match(
                '=') else TokenType.EQUAL
            self.addToken(value)
        elif case == '<':
            value = TokenType.LESS_EQUAL if self.match(
                '=') else TokenType.LESS
            self.addToken(value)
        elif case == '>':
            value = TokenType.GREATER_EQUAL if self.match(
                '=') else TokenType.GREATER
            self.addToken(value)

        elif case == '/':
            if self.match('/'):
                while self.peek() != '\n' and not self.isAtEnd():
                    self.advance()
            else:
                self.addToken(TokenType.SLASH)

        # // Ignore whitespace.
        elif case == ' ':
            None
        elif case == '\r':
            None
        elif case == '\t':
            None

        elif case == '\n':
            self.line += 1

        elif case == '"':
            self.string()

        else:
            if self.isDigit(case):
                self.number()
            elif self.isAlpha(case):
                self.identifier()

            else:
                self.Lox.error(self.line, "Unexpected character.")

    def identifier(self):
        while self.isAlphaNumeric(self.peek()):
            self.advance()

        text = self.source[self.start:self.current]
        # tok_type is replacement for type (reserved word )

        tok_type = None
        if text in self.keywords:
            tok_type = self.keywords[text]

        elif tok_type == None:
            tok_type = TokenType.IDENTIFIER

        self.addToken(tok_type)

    def isAlpha(self, c):
        return (c >= 'a' and c <= 'z') or \
            (c >= 'A' and c <= 'Z') or c == '_'

    def isAlphaNumeric(self, c):
        return self.isAlpha(c) or self.isDigit(c)

    def isDigit(self, c) -> bool:
        return c >= '0' and c <= '9'

    def number(self) -> None:
        while self.isDigit(self.peek()):
            self.advance()

        if self.peek() == '.' and self.isDigit(self.peekNext()):
            self.advance()
            while self.isDigit(self.peek()):
                self.advance()

        self.addToken(TokenType.NUMBER, float(
            self.source[self.start:self.current]))

    def string(self):
        while self.peek() != '"' and not self.isAtEnd():
            if self.peek() == '\n':
                self.line += 1
            self.advance()

        if self.isAtEnd():
            self.Lox.error(self.line, "Unterminated string")
            return

        self.advance()

        value = self.source[self.start + 1: self.current - 1]
        self.addToken(TokenType.STRING, value)

    def peekNext(self):
        if self.current + 1 >= len(self.source):
            return '\0'
        return self.source[self.current + 1]

    def advance(self):
        self.current += 1
        return self.source[self.current-1]

    def addToken(self, tok_type, literal="ahh"):
        if literal == "ahh":
            self.addToken(tok_type, None)
        else:
            text = self.source[self.start: self.current]
            self.tokens.append(Token(tok_type, text, literal, self.line))

    def match(self, expected):
        if self.isAtEnd():
            return False
        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def peek(self):
        if self.isAtEnd():
            return '\0'
        return self.source[self.current]
