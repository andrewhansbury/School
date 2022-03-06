

from expr import *
from tokentypes import TokenType


class AstPrinter:

    def printTree(self, expr) -> str:

        return expr.accept(self)

    # MAY NEED TO ADJUST FOR THE .LEXEME

    def visitBinaryExpr(self, expr: Binary) -> str:

        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visitGroupingExpr(self, expr: Grouping) -> str:
        return self.parenthesize("group", expr.expression)

    def visitLiteralExpr(self, expr: Literal):

        if expr.value == None:
            return None

        return str(expr.value)

    def visitUnaryExpr(self, expr: Unary):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name, *exprs):
        str = ""
        str += "("
        str += name
        for expr in exprs:
            str += " "
            str += expr.accept(self)
        str += ")"

        return str


def main():
    expression = Binary(
        Unary(
            Token(TokenType.MINUS, "-", None, 1),
            Literal(123)),
        Token(TokenType.STAR, "*", None, 1),
        Grouping(Literal(45.67)))

    printer = AstPrinter()

    print(printer.printTree(expression))


if __name__ == "__main__":

    main()
