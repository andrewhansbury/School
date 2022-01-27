
from tokentypes import TokenType
from tokens import Token
from pylox import Lox

# may need to create the ENUMS (tokentype file)


class Scanner:
    def __init__(self, source):
        self.source: str = source
        self.tokens = [Token]

        self.start = 0
        self.current = 0
        self.line = 1

    def scanTokens(self) -> list[Token]:
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

            case _:
                Lox.error(self.line, "Unexpected character.")

    def advance(self):
        self.current += 1
        return self.source[self.current]

    def addToken(self, type: TokenType):
        self.addToken(type, None)

    def addToken(self, type: TokenType, literal: object):
        text: str = self.source[self.start, self.current]
        self.tokens.append(Token(type, text, literal, self.line))

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
