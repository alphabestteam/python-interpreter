

from run_class import run


while True:
    text = input('basic > ')
    result, error = run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)