t = '(5+3)*(2-(1+4)))'
queue_ = []
for i in t:
    if i == '(': queue_.append('(')
    elif i == ')': queue_.pop()
    print(queue_)

print(queue_)