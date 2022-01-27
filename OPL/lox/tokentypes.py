from enum import Enum


class TokenType(Enum):
  LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE = None
  COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR = None

#   // One or two character tokens.
  BANG, BANG_EQUAL, EQUAL, EQUAL_EQUAL, GREATER, GREATER_EQUAL, LESS, LESS_EQUAL = None

#   // Literals.
  IDENTIFIER, STRING, NUMBER = None

#   // Keywords.
  AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NIL, OR = None
  PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE = None

  EOF = None