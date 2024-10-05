def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Desculpe, não entendi. Por favor, insira um número válido.")

while True:
    P = get_float_input("Por favor, insira o depósito inicial:\n")
    r = get_float_input("Por favor, insira a taxa de juros anual (%):\n")
    n = get_float_input("Por favor, insira o número de anos:\n")
    
    amount = P * (1 + r / 100) ** n
    print(f"Após {n} anos, {P:.2f} EUR crescerão para {amount:.2f} EUR.")
    
    if input("Deseja calcular novamente? (s/n):\n").lower() != 's':
        break
