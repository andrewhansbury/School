from tokentypes import TokenType


class Token:
    def __init__(self, tok_type: TokenType, lexeme: str, literal: object, line: int):
        self.tok_type = tok_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self) -> str:
        return str(self.tok_type) + " " + str(self.lexeme) + " " + str(self.literal)
