
from tokens import Token


class Environment:

    def __init__(self, enclosing=None) -> None:
        self.values = {}
        self.enclosing = enclosing

    def get(self, name: Token):
        if name.lexeme in self.values:
            return self.values[name.lexeme]

        if self.enclosing != None:
            return self.enclosing.get(name)

        raise RuntimeError(name, "Undefined variable '" + name.lexeme + "'.")

    def define(self, name: str, value):
        self.values[name] = value

    def assign(self, name: Token, value):
        if name.lexeme in self.values:
            self.values[name.lexeme] = value
            return

        if self.enclosing != None:
            self.enclosing.assign(name, value)
            return

        raise RuntimeError(name, "Undefined variable '" + name.lexeme + "'.")
