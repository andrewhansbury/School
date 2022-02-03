

from email import message
from pickletools import floatnl
from typing import Literal
from expr import *
from tokentypes import TokenType


class RuntimeErrors (RuntimeError):
    def __init__(self, token, message) -> None:
        super().__init__(message)
        self.token = token


class Interpreter:
    def __init__(self, Lox) -> None:
        self.Lox = Lox

    def interpret(self, expression: Expr):
        try:
            value = self.evaluate(expression)
            print(self.stringify(value))

        except RuntimeErrors as error:
            self.Lox.runtimeError(error)

    def visitLiteralExpr(self, expr: Literal, ):
        return expr.value

    def visitGroupingExpr(self, expr: Grouping):
        return self.evaluate(expr.expression)

    def evaluate(self, expr: Expr):
        return expr.accept(self)

    def visitUnaryExpr(self, expr: Unary):
        right = self.evaluate(expr.right)

        if expr.operator.tok_type == TokenType.MINUS:
            self.checkNumberOperand(expr.operator, right)
            return (-1) * float(right)

        if expr.operator.tok_type == TokenType.BANG:
            return not self.isTruthy(right)

        return None

    def checkNumberOperand(self, operator, operand):
        if type(operand) == float:
            return

        raise RuntimeErrors(operator, "Operand must be a number.")

    def checkNumberOperands(self, operator: Token, left, right="poop"):
        if type(left) == float and type(right) == float:
            return
        raise RuntimeErrors(operator, "Operands must be numbers.")

    def isTruthy(self, object) -> bool:
        if object == None:
            return False
        if type(object) == bool:
            return bool(object)
        return True

    def visitBinaryExpr(self, expr: Binary):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        if expr.operator.tok_type == TokenType.BANG_EQUAL:
            return not self.isEqual(left, right)

        if expr.operator.tok_type == TokenType.EQUAL_EQUAL:
            return self.isEqual(left, right)

        if expr.operator.tok_type == TokenType.GREATER:
            self.checkNumberOperands(expr.operator, left, right)
            return float(left) > float(right)

        if expr.operator.tok_type == TokenType.GREATER_EQUAL:
            self.checkNumberOperands(expr.operator, left, right)
            return float(left) >= float(right)

        if expr.operator.tok_type == TokenType.LESS:
            self.checkNumberOperands(expr.operator, left, right)
            return float(left) < float(right)

        if expr.operator.tok_type == TokenType.LESS_EQUAL:
            self.checkNumberOperands(expr.operator, left, right)
            return float(left) <= float(right)

        if expr.operator.tok_type == TokenType.MINUS:
            self.checkNumberOperands(expr.operator, left, right)
            return float(left) - float(right)

        if expr.operator.tok_type == TokenType.PLUS:
            if (type(left) == float) and (type(right) == float):
                return float(left) + float(right)

            if type(left) == str and type(right) == str:
                return str(left) + str(right)

            raise RuntimeErrors(
                expr.operator, "Operands must be two numbers or two strings.")

        if expr.operator.tok_type == TokenType.SLASH:
            self.checkNumberOperands(expr.operator, left, right)
            return float(left) / float(right)

        if expr.operator.tok_type == TokenType.STAR:
            return float(left) * float(right)

        return None

    def isEqual(self, a, b):
        if a == None and b == None:
            return True
        if a == None:
            return False

        return a == b

    def stringify(self, object):
        if object == None:
            return "None"

        if type(object) == float:
            text = str(object)

            if text.endswith(".0"):
                text = text[0: len(text)-2]

            return text

        return str(object)
