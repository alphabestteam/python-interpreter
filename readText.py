import os
from token_array_analyser import is_valid_math_expression
from token_class import Token
file_path = 'code.txt'

with open(file_path, 'r') as file:
        for line in file:
            print(line.strip()) 


def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            # Handle multi-digit numbers
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            tokens.append(Token('number', int(expression[i:j])))
            i = j
        elif expression[i] in "+-*/":
            tokens.append(Token('operator', expression[i]))
            i += 1
        elif expression[i] == '(' or expression[i] == ')':
            tokens.append(Token('parenthesis', expression[i]))
            i += 1
        else:
            # Ignore spaces or handle other cases as needed
            i += 1

    return tokens


def shunting_yard(tokens):
    output = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in tokens:
        if token.type == 'number':
            output.append(token.value)
        elif token.type == 'parenthesis' and token.value == '(':
            operators.append(token)
        elif token.type == 'parenthesis' and token.value == ')':
            while operators and operators[-1].type != 'parenthesis':
                output.append(operators.pop().value)
            operators.pop()  # Discard the '('
        elif token.type == 'operator':
            while operators and precedence.get(token.value, 0) <= precedence.get(operators[-1].value, 0):
                output.append(operators.pop().value)
            operators.append(token)

    while operators:
        output.append(operators.pop().value)

    return output


def evaluate_postfix(postfix):
    stack = []

    for token in postfix:
        if isinstance(token, int):
            stack.append(token)
        elif token in {'+', '-', '*', '/'}:
            if len(stack) < 2:
                raise ValueError("Not enough operands for operator.")
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                if operand2 == 0:
                    raise ValueError("Division by zero.")
                stack.append(operand1 / operand2)

    if len(stack) != 1:
        raise ValueError("Invalid expression: too many operands.")

    return stack[0]


def read_equations(file_path):
    with open(file_path, 'r') as file:
        equations = [line.strip() for line in file]
    return equations



def main():
    file_path = 'code.txt'
    equations = read_equations(file_path)

    for equation in equations:
        print(f"Equation: {equation}")
        
        tokens = tokenize(equation)
        print(f"Tokens: {tokens}")

        if is_valid_math_expression(tokens):
            postfix_expression = shunting_yard(tokens)
            print(f"Postfix Expression: {' '.join(map(str, postfix_expression))}")

            result = evaluate_postfix(postfix_expression)
            print(f"Result: {result}")

            print("------")

if __name__ == "__main__":
    main()
