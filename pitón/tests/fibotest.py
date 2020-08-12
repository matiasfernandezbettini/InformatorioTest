def imprime_fibonacci(n):
    '''escribe la sucesión Fibonacci hasta n'''
    a = 0 
    b = 1
    while b < n:
        print (b, a, b, a + b)

imprime_fibonacci(50)