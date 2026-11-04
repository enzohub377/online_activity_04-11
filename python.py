def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    return a / b
def menu():
    print("\n--- CALCULADORA ---")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")
while True:
    menu()
    opcao = input("Escolha uma opção (1-5): ")
    if opcao == '5':
        print("Saindo da calculadora. Até logo!")
        break
    if opcao in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, digite apenas números válidos.")
            continue
        if opcao == '1':
            print(Resultados: f"{num1} + {num2} = {somar(num1, num2)}")
        elif opcao == '2':
            print(Resultados: f"{num1} - {num2} = {subtrair(num1, num2)}")
        elif opcao == '3':
            print(Resultados: f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif opcao == '4':
            print(Resultados: f"{num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Opção inválida! Tente novamente.")