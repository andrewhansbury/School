

from tokentypes import TokenType
from tokens import Token

# may need to create the ENUMS (tokentype file)

# need to pass Lox otherwise circular dependency


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
        c = self.advance()

        match c:
            case '(': self.addToken(TokenType.LEFT_PAREN)
            case ')': self.addToken(TokenType.RIGHT_PAREN)
            case '{': self.addToken(TokenType.LEFT_BRACE)
            case '}': self.addToken(TokenType.RIGHT_BRACE)
            case ',': self.addToken(TokenType.COMMA)
            case '.': self.addToken(TokenType.DOT)
            case '-': self.addToken(TokenType.MINUS)
            case '+': self.addToken(TokenType.PLUS)
            case ';': self.addToken(TokenType.SEMICOLON)
            case '*': self.addToken(TokenType.STAR)

            case '!':
                value = TokenType.BANG_EQUAL if self.match(
                    '=') else TokenType.BANG
                self.addToken(value)
            case '=':
                value = TokenType.EQUAL_EQUAL if self.match(
                    '=') else TokenType.EQUAL
                self.addToken(value)
            case '<':
                value = TokenType.LESS_EQUAL if self.match(
                    '=') else TokenType.LESS
                self.addToken(value)
            case '>':
                value = TokenType.GREATER_EQUAL if self.match(
                    '=') else TokenType.GREATER
                self.addToken(value)

            case '/':
                if self.match('/'):
                    while self.peek() != '\n' and not self.isAtEnd():
                        self.advance()
                else:
                    self.addToken(TokenType.SLASH)

            # // Ignore whitespace.
            case ' ': None
            case '\r': None
            case '\t': None

            case '\n':
                self.line += 1

            case '"':
                self.string()

            case _:
                if self.isDigit(c):
                    self.number()
                elif self.isAlpha(c):
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
