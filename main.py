from token_array_analyser import is_valid_math_expression
from token_class import Token


def main():
    token_arr = [
        Token("INT", "5").__str__(),
        Token("PLUS", "+").__str__(),
        Token("INT", "-").__str__(),
        Token("MINUS", "-").__str__(),
        Token("INT", "8").__str__(),
    ]
    print(is_valid_math_expression(token_arr))


if __name__ == "__main__":
    main()
