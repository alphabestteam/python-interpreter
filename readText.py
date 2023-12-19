import os
file_path = 'code.txt'

with open(file_path, 'r') as file:
        for line in file:
            print(line.strip()) 

def shunting_yard(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []

    for token in expression:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Discard the '('
        elif token in precedence:
            while operators and precedence[token] <= precedence.get(operators[-1], 0):
                output.append(operators.pop())
            operators.append(token)

    while operators:
        output.append(operators.pop())

    return output

def evaluate_postfix(postfix):
    stack = []

    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        elif token in {'+', '-', '*', '/'}:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)

    return stack[0]

# Example usage:
infix_expression = "(4+5)*3-2"
tokens = [char for char in infix_expression if char.isalnum() or char in {'+', '-', '*', '/', '(', ')'}]
postfix_expression = shunting_yard(tokens)
result = evaluate_postfix(postfix_expression)

print(f"Infix Expression: {infix_expression}")
print(f"Postfix Expression: {' '.join(postfix_expression)}")
print(f"Result: {result}")
