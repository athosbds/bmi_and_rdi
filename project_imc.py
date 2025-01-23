from math import pow

print('\033[1;32;31m Atenção! Coloque a sua altura em centímetros e sem pontuação. \033[m')
print('=' * 50)

while True:
    genre = input('Digite seu sexo (masculino/feminino): ').strip().lower()
    if genre not in ['masculino', 'feminino']:
        print("Entrada inválida! Informe 'masculino' ou 'feminino'.")
        continue

    try:
        age = int(input('Digite sua idade: '))
        if age <= 0:
            print("Idade inválida! Digite um número positivo.")
            continue
    except ValueError:
        print("Entrada inválida! Digite um número inteiro para a idade.")
        continue

    try:
        height = int(input('Digite sua altura em centímetros: '))
        if height <= 0:
            print("Altura inválida! Digite um número positivo.")
            continue
    except ValueError:
        print("Entrada inválida! Digite um número inteiro para a altura.")
        continue

    try:
        weight = float(input('Digite seu peso em quilogramas: '))
        if weight <= 0:
            print("Peso inválido! Digite um número positivo.")
            continue
    except ValueError:
        print("Entrada inválida! Digite um número válido para o peso.")
        continue

    break

print('=' * 50)

# Conversão da altura para metros
height_in_metro = height / 100

# Cálculo do IMC
calculate_imc = weight / pow(height_in_metro, 2)

# Cálculo do IDR para homens e mulheres
calculate_idr_man = (13.75 * weight) + (5 * height) - (6.76 * age)
calculate_idr_woman = (9.56 * weight) + (1.85 * height) - (4.68 * age) + 665

print("""\n \033[1m Cálculo IMC \033[m
O IMC (Índice de Massa Corpórea) é utilizado para calcular o peso ideal, dividindo o peso pela altura ao quadrado. 
Um IMC entre 18,5 e 24,9 indica peso normal.""")

# Exibindo a classificação do IMC
print('\033[1;37m \n Dados Índice de Massa Corpórea: \033[m')

if calculate_imc < 18.5:
    print(f'Seu IMC: {calculate_imc:.1f} \nClassificação: Magreza')
elif 18.5 <= calculate_imc <= 24.9:
    print(f'Seu IMC: {calculate_imc:.1f} \nClassificação: Normal')
elif 25.0 <= calculate_imc <= 29.9:
    print(f'Seu IMC: {calculate_imc:.1f} \nClassificação: Sobrepeso \nGrau de Obesidade: 1')
elif 30.0 <= calculate_imc <= 39.9:
    print(f'Seu IMC: {calculate_imc:.1f} \nClassificação: Obesidade \nGrau de Obesidade: 2')
else:
    print(f'Seu IMC: {calculate_imc:.1f} \nClassificação: Obesidade Grave \nGrau de Obesidade: 3')

# Escolha do nível de atividade
print('\n \033[1m Nível de Atividade:\033[m')
print('A - Sedentário \nB - Atividade leve \nC - Atividade moderada \nD - Atividade intensa \nE - Atividade extrema')

frequency = input('\n \033[1;30m Digite a frequência correspondente à letra: \033[m').strip().upper()

# Cálculo do IDR com base no nível de atividade
idr = 0
if frequency == 'A':
    multiplier = 1.2
elif frequency == 'B':
    multiplier = 1.375
elif frequency == 'C':
    multiplier = 1.55
elif frequency == 'D':
    multiplier = 1.725
elif frequency == 'E':
    multiplier = 1.9
else:
    print('Entrada inválida para nível de atividade.')
    multiplier = 0

if multiplier > 0:
    if genre == 'masculino':
        idr = calculate_idr_man * multiplier
    elif genre == 'feminino':
        idr = calculate_idr_woman * multiplier
    print(f'Sua Ingestão Diária Recomendada é de {idr:.2f} calorias por dia.')
else:
    print('Não foi possível calcular o seu IDR.')