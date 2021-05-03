def divideFn(x, y):
    return x / y

def multiplicaFn(x, y):
    return x * y

def potenciaFn(x, y):
    return x ** y

numeros = [1, 2, 3, 4, 5]

divide = [divideFn(numero, 2) for numero in numeros]
multiplicacao = [multiplicaFn(numero, 2) for numero in numeros]
quadrado  = [potenciaFn(numero, 2) for numero in numeros]

print(numeros)
print(divide)
print(multiplicacao)
print(quadrado)