from typing import Literal
from expr import *
from environment import Environment
from stmt import *
from tokentypes import TokenType


class RuntimeErrors (RuntimeError):
    def __init__(self, token, message) -> None:
        super().__init__(message)
        self.token = token


class Interpreter:
    def __init__(self, Lox) -> None:
        self.Lox = Lox
        self.environmnent = Environment()

    def interpret(self, statements):
        try:
            for statement in statements:
                self.execute(statement)

        except RuntimeErrors as error:
            self.Lox.runtimeError(error)

    def execute(self, stmt: Stmt) -> None:
        stmt.accept(self)

    # def interpret(self, expression: Expr):
    #     try:
    #         value = self.evaluate(expression)
    #         print(self.stringify(value))

    #     except RuntimeErrors as error:
    #         self.Lox.runtimeError(error)

    def visitBlockStmt(self, stmt: Block):
        self.executeBlock(stmt.statements, Environment(self.environmnent))
        return None

    def executeBlock(self, statements: 'list[Stmt]', environment: Environment):
        previous = self.environmnent
        try:
            self.environmnent = environment
            for statement in statements:
                self.execute(statement)
        finally:
            self.environmnent = previous

    def visitLiteralExpr(self, expr: Literal):
        return expr.value

    def visitGroupingExpr(self, expr: Grouping):
        return self.evaluate(expr.expression)

    def evaluate(self, expr: Expr):
        return expr.accept(self)

    def visitExpressionStmt(self, stmt: Expression):
        self.evaluate(stmt.expr)
        return None

    def visitPrintStmt(self, stmt: Print):
        value = self.evaluate(stmt.expr)
        print(self.stringify(value))
        return None

    def visitUnaryExpr(self, expr: Unary):
        right = self.evaluate(expr.right)

        if expr.operator.tok_type == TokenType.MINUS:
            self.checkNumberOperand(expr.operator, right)
            return (-1) * float(right)

        if expr.operator.tok_type == TokenType.BANG:
            return not self.isTruthy(right)

        return None

    def visitVarStmt(self, stmt: Var):
        value = None
        if stmt.initializer != None:
            value = self.evaluate(stmt.initializer)

        self.environmnent.define(stmt.name.lexeme, value)
        return None

    def visitAssignExpr(self, expr: Assign):
        value = self.evaluate(expr.value)
        self.environmnent.assign(expr.name, value)
        return value

    def visitVariableExpr(self, expr: Variable):

        return self.environmnent.get(expr.name)

    def checkNumberOperand(self, operator, operand):
        if type(operand) == float:
            return

        raise RuntimeErrors(operator, "Operand must be a number.")

    def checkOperands(self, operator: Token, left, right="poop"):
        if (type(left) == float and type(right) == float) or (type(left == str and type(right) == str)):
            return
        raise RuntimeErrors(operator, "Operands must be numbers or strings")

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
            self.checkOperands(expr.operator, left, right)
            return left > right

        if expr.operator.tok_type == TokenType.GREATER_EQUAL:
            self.checkOperands(expr.operator, left, right)
            return left >= right

        if expr.operator.tok_type == TokenType.LESS:
            self.checkOperands(expr.operator, left, right)
            return left < right

        if expr.operator.tok_type == TokenType.LESS_EQUAL:
            self.checkOperands(expr.operator, left, right)
            return left <= right

        if expr.operator.tok_type == TokenType.MINUS:
            self.checkOperands(expr.operator, left, right)
            return float(left) - float(right)

        if expr.operator.tok_type == TokenType.PLUS:
            if (type(left) == float) and (type(right) == float):
                return float(left) + float(right)

            if type(left) == str and type(right) == str:
                return str(left) + str(right)

            raise RuntimeErrors(
                expr.operator, "Operands must be two numbers or two strings.")

        if expr.operator.tok_type == TokenType.SLASH:
            self.checkOperands(expr.operator, left, right)
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
        if object == False:
            return "false"

        if object == True:
            return "true"

        if object == None:
            return "None"

        if type(object) == float:
            text = str(object)

            if text.endswith(".0"):
                text = text[0: len(text)-2]

            return text

        return str(object)
