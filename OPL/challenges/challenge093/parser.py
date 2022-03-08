
from expr import *
from stmt import *
from tokentypes import TokenType
from tokens import Token


class ParseError(Exception):
    pass


class Parser:
    def __init__(self, tokens: 'list[Token]', Lox) -> None:
        self.Lox = Lox
        self.tokens = tokens
        self.current = 0
        
        self.loopDepth = 0 

    # def parse(self):

    #     try:
    #         return self.expression()
    #     # This line may need work
    #     except ParseError:
    #         return None

    def parse(self):
        statements = []
        while not self.isAtEnd():
            statements.append(self.declaration())

        return statements

    def declaration(self):
        try:
            if self.match(TokenType.VAR):
                return self.varDeclaration()
            return self.statement()
        except ParseError as error:
            self.synchronize()
            return None

    def statement(self) -> Stmt:
        if self.match(TokenType.CONTINUE):
            return self.continueStatement()
        if self.match(TokenType.BREAK):
            return self.breakStatement()
        if self.match(TokenType.FOR):
            return self.forStatement()
        if self.match(TokenType.IF):
            return self.ifStatement()
        if self.match(TokenType.PRINT):
            return self.printStatement()
        if self.match(TokenType.WHILE):
            return self.whileStatement()
        if self.match(TokenType.LEFT_BRACE):
            return Block(self.block())
        return self.expressionStatement()

    def continueStatement(self):
        if self.loopDepth ==0:
            self.error(self.previous(), "'continue' is only allowed in a loop.")
            
        self.consume(TokenType.SEMICOLON, "Expect ';' after 'continue'.")
        return Continue()

    def breakStatement(self):
        if self.loopDepth ==0:
            self.error(self.previous(), "Must be inside a loop to use 'break'.")
            
        self.consume(TokenType.SEMICOLON, "Expect ';' after 'break'.")
        return Break()
    
    def forStatement(self):
        

        self.consume(TokenType.LEFT_PAREN, "Expect '(' after 'for'.")

        initializer = None

        if self.match(TokenType.SEMICOLON):
            initializer = None
        elif self.match(TokenType.VAR):
            initializer = self.varDeclaration()
        else:
            initializer = self.expressionStatement()

        condition = None
        if not self.check(TokenType.SEMICOLON):
            condition = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after loop condition.")

        increment = None
        if not self.check(TokenType.RIGHT_PAREN):
            increment = self.expression()

        self.consume(TokenType.RIGHT_PAREN, "Expect ')' after for clauses.")

        try:
            self.loopDepth +=1
            body = self.statement()

            # print(body.statements)

            # PROBABLY DOESNT WORK
            if increment != None:
                body = Block([body, Expression(increment)])

            if condition == None:
                condition = Literal(True)
            body = While(condition, body, True)

            if initializer != None:
                body = Block([initializer, body])

            return body
        finally:
            self.loopDepth-=1

    def ifStatement(self):
        self.consume(TokenType.LEFT_PAREN, "Expect '(' after 'if'.")
        condition = self.expression()
        self.consume(TokenType.RIGHT_PAREN, "Expect ')' after if condition.")

        thenBranch = self.statement()
        elseBranch = None
        if self.match(TokenType.ELSE):
            elseBranch = self.statement()

        return If(condition, thenBranch, elseBranch)

    def printStatement(self) -> Stmt:
        value = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after value.")
        return Print(value)

    def varDeclaration(self):
        name: Token = self.consume(
            TokenType.IDENTIFIER, "Expect variable name.")

        initializer: Expr = None
        if self.match(TokenType.EQUAL):
            initializer = self.expression()

        self.consume(TokenType.SEMICOLON,
                     "Expect ';' after variable declaration.")
        return Var(name, initializer)

    def whileStatement(self) -> Stmt:
        self.consume(TokenType.LEFT_PAREN, "Expect '(' after 'while'.")
        condition = self.expression()
        self.consume(TokenType.RIGHT_PAREN, "Expect ')' after condition.")
        
        try:
            self.loopDepth +=1
            body = self.statement()

            return While(condition, body, False)
        finally:
            self.loopDepth -=1

    def expressionStatement(self) -> Stmt:
        expr = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after expression.")
        return Expression(expr)

    def block(self) -> 'list[Stmt]':
        statements = []
        while not self.check(TokenType.RIGHT_BRACE) and not self.isAtEnd():
            statements.append(self.declaration())

        self.consume(TokenType.RIGHT_BRACE, "Expect '}' after block.")
        return statements

    def assignment(self) -> Expr:
        expr: Expr = self.orr()

        if self.match(TokenType.EQUAL):
            equals: Token = self.previous()
            value: Expr = self.assignment()

            if isinstance(expr, Variable):
                name: Token = expr.name
                return Assign(name, value)

            self.error(equals, "Invalid assignment target.")

        return expr

    def orr(self) -> Expr:
        expr = self.andd()

        while self.match(TokenType.OR):
            operator = self.previous()
            right = self.andd()
            expr = Logical(expr, operator, right)

        return expr

    def andd(self) -> Expr:
        expr = self.equality()

        while self.match(TokenType.AND):
            operator = self.previous()
            right = self.equality()
            expr = Logical(expr, operator, right)

        return expr

    def expression(self) -> Expr:
        return self.assignment()

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

        if self.match(TokenType.IDENTIFIER):
            return Variable(self.previous())

        # if self.match(TokenType.NUMBER, TokenType.STRING):
        #     return Literal(self.previous().literal)

        if self.match(TokenType.LEFT_PAREN):
            expr: Expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
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
        if not self.isAtEnd():
            self.current += 1

        return self.previous()

    def isAtEnd(self) -> bool:
        return self.peek().tok_type == TokenType.EOF

    def peek(self) -> Token:
        # print(self.tokens[self.current])
        return self.tokens[self.current]

    def previous(self) -> Token:
        index = self.current - 1
        return self.tokens[index]
