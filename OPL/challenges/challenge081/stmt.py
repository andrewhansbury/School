from expr import Expr


class Stmt:
    pass


class Block(Stmt):
    def __init__(self, statements: 'list[Stmt]') -> None:
        self.statements = statements

    def accept(self, visitor):
        return visitor.visitBlockStmt(self)


class Expression(Stmt):
    def __init__(self, expr: Expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitExpressionStmt(self)


class Print(Stmt):
    def __init__(self, expr: Expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitPrintStmt(self)


class Var(Stmt):
    def __init__(self, name, initializer: Expr):
        self.name = name
        self.initializer = initializer

    def accept(self, visitor):
        return visitor.visitVarStmt(self)

# class Block(Stmt):
#     def __init__(self, statements: list[Stmt]):
#         self.statements = statements

#     def accept(self, visitor):
#         return visitor.visit_block_stmt(self)

# class If(Stmt):
#     def __init__(self, condition: Expr, then_branch: Stmt, else_branch: Stmt):
#         self.condition = condition
#         self.then_branch = then_branch
#         self.else_branch = else_branch

#     def accept(self, visitor):
#         return visitor.visit_if_stmt(self)

# class Fun(Stmt):
#     def __init__(self, name: Token, function: "Function"):
#         self.name = name
#         self.function = function

#     def accept(self, visitor):
#         return visitor.visit_fun_stmt(self)

# class Return(Stmt):
#     def __init__(self, keyword: Token, value: Expr):
#         self.keyword = keyword
#         self.value = value

#     def accept(self, visitor):
#         return visitor.visit_return_stmt(self)

# class Class(Stmt):
#     def __init__(self, name: Token, super_class :"Class", methods: list[Stmt], class_methods: list[Stmt]):
#         self.name = name
#         self.super_class = super_class
#         self.methods = methods
#         self.class_methods = class_methods

#     def accept(self, visitor):
#         return visitor.visit_class_stmt(self)


# class While(Stmt):
#     def __init__(self, condition: Expr, body: Stmt):
#         self.condition = condition
#         self.body = body

#     def accept(self, visitor):
#         return visitor.visit_while_stmt(self)

# class Break(Stmt):
#     def __init__(self):
#         pass

#     def accept(self, visitor):
#         return visitor.visit_break_stmt(self)
