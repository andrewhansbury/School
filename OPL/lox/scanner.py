
from lox.tokentypes import TokenType
from tokens import Token

#may need to create the ENUMS (tokentype file)

class Scanner:
    def __init__(self, source):
        self.source:str = source
        self.tokens = [Token]
        
        self.start = 0
        self.current = 0
        self.line = 1
        

    def scanTokens(self) -> list[Token]:
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()
        
        self.tokens.append(Token(Token.EOF,"", None, self.line))
        return self.tokens
    
    def isAtEnd(self):
        return self.current >= len(self.source)
    
    def scanToken(self):
        c = self.advance()
        match c:
            case '(': self.addToken(Token.LEFT_PAREN)
            case ')': self.addToken(Token.RIGHT_PAREN)
            case '{': self.addToken(Token.LEFT_BRACE)
            case '}': self.addToken(Token.RIGHT_BRACE)
            case ',': self.addToken(Token.COMMA)
            case '.': self.addToken(Token.DOT)
            case '-': self.addToken(Token.MINUS)
            case '+': self.addToken(Token.PLUS)            
            case ';': self.addToken(Token.SEMICOLON) 
            case '*': self.addToken(Token.STAR)
            
            
    def advance(self):
        self.current +=1
        return self.source[self.current]

    def addToken(self, type:TokenType):
        self.addToken(type, None)
        
    def addToken(self, type:TokenType, literal:object ):
        
        text:str = self.source[self.start, self.current]
        self.tokens.append(Token(type, text, literal, self.line))
        
    
        
            