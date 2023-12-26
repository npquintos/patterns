def factorial(n):
    register = [[n, n]]
    while True:
        if not register:
            break
        accum, counter = register.pop()
        counter -= 1
        if counter == 0:
            break
        accum *= counter
        register.append([accum, counter])
    return accum

print(factorial(1500))
