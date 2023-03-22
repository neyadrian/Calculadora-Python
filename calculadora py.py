
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        print("Error!")
        return 0
    else:
        return a / b

def menu():
    print("Escolha a operação desejada:")
    print("----------------------------")
    print("+ : Adição")
    print("- : Subtração")
    print("* : Multiplicação")
    print("/ : Divisão")
    print("-----------------------------")

while True:
    menu()
    op = input("Digite uma das opções acima: ")
    
    if op == '0':
        print("Calculadora cancelada.")
        break
    
    if op not in ['+', '-', '*', '/']:
        print("Operação inválida, tente novamente!")
        continue
    
    num1 = float(input("Informe o 1º número: "))
    num2 = float(input("Informe o 2º número: "))
    
    if op == '+':
        result = adicao(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif op == '-':
        result = subtracao(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif op == '*':
        result = multiplicacao(num1, num2)
        print(f"{num1} x {num2} = {result}")
    elif op == '/':
        result = divisao(num1, num2)
        print(f"{num1} / {num2} = {result}")