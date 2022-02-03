from expr import *
from tokentypes import TokenType
from tokens import Token


class ParseError(Exception):
    pass


class Parser:
    def __init__(self, tokens: list[Token], Lox) -> None:
        self.Lox = Lox
        self.tokens = tokens
        self.current = 0

    def parse(self):
        try:
            return self.expression()
        # This line may need work
        except ParseError:
            return None

    def expression(self) -> Expr:
        return self.equality()

    def equality(self) -> Expr:
        expr: Expr = self.comparison()

        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator: Token = self.previous()
            right: Expr = self.comparison()
            expr = Binary(expr, operator, right)

        return expr

    def comparison(self) -> Expr:
        expr: Expr = self.term()

        while self.match(TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL):
            operator: Token = self.previous()
            right: Expr = self.term()
            expr = Binary(expr, operator, right)

        return expr

    def term(self) -> Expr:
        expr: Expr = self.factor()

        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator: Token = self.previous()
            right: Expr = self.factor()
            expr = Binary(expr, operator, right)

        return expr

    def factor(self) -> Expr:
        expr: Expr = self.unary()

        while self.match(TokenType.SLASH, TokenType.STAR):
            operator: Token = self.previous()
            right: Expr = self.unary()
            expr = Binary(expr, operator, right)

        return expr

    def unary(self) -> Expr:
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator: Token = self.previous()
            right: Expr = self.unary()

            return Unary(operator, right)

        return self.primary()

    def primary(self) -> Expr:
        if self.match(TokenType.FALSE):
            return Literal(False)
        if self.match(TokenType.TRUE):
            return Literal(True)
        if self.match(TokenType.NIL):
            return Literal(None)

        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Literal(self.previous().literal)

        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Literal(self.previous().literal)

        if self.match(TokenType.LEFT_PAREN):
            expr: Expr = self.expression()
            self.consume(TokenType, "Expect ')' after expression.")
            return Grouping(expr)

        raise self.error(self.peek(), "Expect expression.")

    def match(self, *types) -> bool:
        for tok_type in types:
            if self.check(tok_type):
                self.advance()
                return True
        return False

    def consume(self, tok_type: TokenType, message: str) -> Token:
        try:
            if self.check(tok_type):
                return self.advance()
        except:
            self.error(self.peek, message)

    # MAY NEED SOME WORK!
    # THE LOX MAY NEED TO BE PASSED AS PARAMETER OR SOMETHING
    def error(self, token: Token, message: str):
        self.Lox.error(token, message)
        return ParseError()

    def synchronize(self) -> None:
        self.advance()

        while not self.isAtEnd():
            if self.previous().tok_type == TokenType.SEMICOLON:
                return

            if self.peek().tok_type == \
                    TokenType.CLASS or \
                    TokenType.FUN or \
                    TokenType.VAR or \
                    TokenType.FOR or \
                    TokenType.IF or \
                    TokenType.WHILE or \
                    TokenType.PRINT or \
                    TokenType.RETURN:
                return

            self.advance()

    def check(self, tok_type: TokenType) -> bool:
        if self.isAtEnd():
            return False

        return self.peek().tok_type == tok_type

    def advance(self) -> Token:
        if self.isAtEnd():
            self.current += 1

        return self.previous()

    def isAtEnd(self) -> bool:
        return self.peek().tok_type == TokenType.EOF

    def peek(self) -> Token:
        print(self.tokens[self.current])
        return self.tokens[self.current]

    def previous(self) -> Token:
        index = self.current - 1
        return self.tokens[index]
