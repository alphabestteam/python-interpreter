from token_array_analyser import is_valid_math_expression
from token_class import Token, INT, PLUS, MINUS, MUL, DIV, LEFT_PAREN, RIGHT_PAREN
from readText import shunting_yard, evaluate_postfix

def read_equations(file_path):
    with open(file_path, 'r') as file:
        equations = [line.strip() for line in file]
    return equations

def tokenize_equation(equation):
    tokens = []
    current_token = ''

    for char in equation:
        if char.isdigit() or char == '.':
            current_token += char
        elif char in {'+', '-', '*', '/', '(', ')'}:
            if current_token:
                tokens.append(Token(INT, current_token))
                current_token = ''
            tokens.append(Token(char))

    if current_token:
        tokens.append(Token(INT, current_token))

    # Replace tokens with types PLUS and MINUS
    for i in range(len(tokens)):
        if tokens[i].type == '+':
            tokens[i] = Token("PLUS", '+')
        elif tokens[i].type == '-':
            tokens[i] = Token("MINUS", '-')

    return tokens


def main():
    file_path = 'code.txt'
    equations = read_equations(file_path)

    for equation in equations:
        print(f"Equation: {equation}")
        
        tokens = tokenize_equation(equation)
        print(f"Tokens: {tokens}")

        if is_valid_math_expression(tokens):
            postfix_expression = shunting_yard(tokens)
            print(f"Postfix Expression: {' '.join(postfix_expression)}")

            result = evaluate_postfix(postfix_expression)
            print(f"Result: {result}")

            print("------")

if __name__ == "__main__":
    main()
