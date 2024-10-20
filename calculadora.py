def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero!"

# Interface simples
print("Selecione a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Recebe a escolha do usuário
escolha = input("Digite o número da operação (1/2/3/4): ")

# Recebe os números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza a operação com base na escolha
if escolha == '1':
    print(f"Resultado da soma: {soma(num1, num2)}")
elif escolha == '2':
    print(f"Resultado da subtração: {subtracao(num1, num2)}")
elif escolha == '3':
    print(f"Resultado da multiplicação: {multiplicacao(num1, num2)}")
elif escolha == '4':
    print(f"Resultado da divisão: {divisao(num1, num2)}")
else:
    print("Opção inválida!")
