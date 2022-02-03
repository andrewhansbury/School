
from expr import Expr
from lox.expr import Binary
from tokentypes import TokenType
from tokens import Token


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.current = 0

    def expression(self) -> Expr:
        return self.equality()

    def equality(self) -> Expr:
        expr: Expr = self.comparison()

        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator: Token = self.previous()
            right: Expr = self.comparison()
            expr = Binary(expr, operator, right)

        return expr

    def match(self, *types) -> bool:
        for tok_type in types:
            if self.check(tok_type):
                self.advance()
                return True
        return False
