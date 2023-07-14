print("Este programa realizará a conversão de graus Celsius para graus Fahrenheit!")

opcao = int(input("Digite o número da opcão que queres converter:\n1)Celsius para Fahrenheit\n2)Fahrenheit para Celsius\n:"))

def grausCelsius():
    celsius = float(input("Digite a temperatura em graus Celsius para converter para Fahrenheit: "))
    conversao = (celsius * 9 / 5) + 32
    return f"Você digitou {celsius} graus Celsius e a conversão é {round(conversao, 2)} graus Fahrenheit!"

def grausFahrenheit():
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit para converter para Celsius: "))
    conversao = (fahrenheit - 32) * 5 / 9
    return f"Você digitou {fahrenheit} graus Fahrenheit e a conversão é {round(conversao, 2)} graus Celsius!"

match opcao:
    case 1:
        print(grausCelsius())
    case 2:
        print(grausFahrenheit())
    case other:
        print("Você não digitou uma opção válida!")