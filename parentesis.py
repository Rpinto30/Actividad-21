t = input("Ingresa una operación matemática: ")
def valid_expression(expression) -> bool:
    expression = expression.strip()
    try:
        queue_ = []
        for i in expression:
            if i == '(': queue_.append('(')
            elif i == ')': queue_.pop()
        if len(queue_) == 0: return True
        else: return  False
    except IndexError: return False

if valid_expression(t): print(f' 😀 La opereación {t} es \u001b[1mcorrecta!\u001b[0m')
else: print(f' 😞 Verifica tus paréntesis en la operación {t}')