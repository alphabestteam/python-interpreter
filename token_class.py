INT = 'INT'
FLOAT = 'FLOAT'
PLUS = '+'
MINUS = '-'
MUL = '*'
DIV = '/'
LEFT_PAREN = '('
RIGHT_PAREN = ')'


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"
        return f"{self.type}"

    def __str__(self) -> str:
        return self.value
