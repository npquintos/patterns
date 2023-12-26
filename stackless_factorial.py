# This version will not result to stack overflow no
# matter how large 'n' is. It has a bug by design.
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
