def fibonacci(n):
    fib_sequence = []
    a , b = 0 ,1
    for _ in range(n):
        fib_sequence.append(a)
        a , b = b , a+b
    return fib_sequence
n = int(input("enter the number of terms="))
num_list = fibonacci(n)
print(num_list)