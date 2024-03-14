def sequencia_fibonacci(n):
    sequencia_fib = [0, 1]
    while sequencia_fib[-1] < n:
        sequencia_fib.append(sequencia_fib[-1] + sequencia_fib[-2])
    return sequencia_fib

def checar_fibonacci(num):
    sequencia_fib = sequencia_fibonacci(num)
    if num in sequencia_fib:
        return f"{num} pertence à sequência de Fibonacci."
    else:
        return f"{num} não pertence à sequência de Fibonacci."

num = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))
print(checar_fibonacci(num))