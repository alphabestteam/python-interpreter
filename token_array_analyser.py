import ast


def is_valid_math_expression(tokens) -> bool:
    code = " ".join(str(token.value) for token in tokens)

    try:
        ast.parse(code)
        return True
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
        print("The provided token array is not valid Python code.")
    except Exception as e:
        print(f"Error: {e}")
        print(
            "The provided token array is syntactically correct but not mathematically correct."
        )
    return False
