t = input("Ingresa una operación matemática: ")
def valid_expression(expression) -> bool:
    expression = expression.strip()
    try:
        queue_ = []
        for i in expression:
            if i == '(': queue_.append('(')
            elif i == ')': queue_.pop()
            print(queue_)
        if len(queue_) == 0: return True
        else: return  False
    except IndexError: return False

print(valid_expression(t))