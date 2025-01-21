from math import pow

print('\033[1;32;31m Atenção! Coloque a sua altura em Centímetros e sem Pontuação. \033[m')
print('='*50)


genre = str(input('Digite seu sexo: ')).strip()
age = int(input('Digite sua idade: '))
height = float(input('Digite sua altura: '))
weight = float(input('Digite seu peso: '))

print('='*50)

height_in_metro = height / 100
calculate_imc = weight / (pow(height_in_metro, 2))

calculate_idr_man = ( 13.75 * weight ) + ( 5 * height_in_metro ) - (6.76 * age)
calculate_idr_woman = (9.56 * weight) + (1.85* height_in_metro) - (4.68 * age) + 665



from time import sleep



if genre.lower() == 'masculino':
    print('Prosseguindo...')
elif genre.lower() == 'feminino':
    print('Prosseguindo...')
else:
    print('Sexo inválido. Tente novamente.')

sleep(3)

print("""\n \033[1m Cálculo IMC \033[m
O IMC (Índice de Massa Corpórea) é utilizado para calcular o peso ideal, dividindo o peso pela altura ao quadrado. Um IMC entre 18,5 e 24,9 indica peso normal.""")




print('\033[1;37m \n Dados Índice de Massa Corpórea: \033[m')

if calculate_imc < 18.5:
    print(' Seu IMC: {:.1f} \n Classificação: Magreza'.format(calculate_imc))
elif 18.5 <= calculate_imc <= 24.9:
    print('Seu IMC: {:.1f} \n Classificação: Normal'.format(calculate_imc))
elif 25.0 <= calculate_imc <= 29.0:
    print('Seu IMC: {:.1f} \n Classificação: Sobrepeso \n Grau de Obesidade: 1'.format(calculate_imc))
elif 30.0 <= calculate_imc <= 39.9:
    print('Seu IMC: {:.1f} \n Classificação: Obesidade \n Grau de Obesidade: 2'.format(calculate_imc))
else:
    print('Seu IMC: {:.1f} \n Classificação: Obesidade Grave \n Grau de Obesidade: 3'.format(calculate_imc))



print('\n \033[1m Nível de Atividade:\033[m')
print('A - Sedentário \nB - Atividade leve \nC - Atividade moderada \nD - Atividade intensa \nE - Atividade extrema')

frequency = str(input('\n \033[1;30m Digite a frequência correspondente a Letra: \033[m')).strip()

print('='*50)

if genre.lower() == 'masculino':
    if frequency.upper() == 'A':
        idr = calculate_idr_man * 1.2
    elif frequency.upper() == 'B':
        idr = calculate_idr_man * 1.375
    elif frequency.upper() == 'C':
        idr = calculate_idr_man * 1.55
    elif frequency.upper() == 'D':
        idr = calculate_idr_man * 1.725
    elif frequency.upper() == 'E':
        idr = calculate_idr_man * 1.9
    else:
        print('Entrada inválida para nível de atividade.')
        idr = 0
    print(f'Sua Ingestão Diária Recomendada é de {idr:.2f} calorias por dia.')
elif genre.lower() == 'feminino':
    if frequency.upper() == 'A':
        idr = calculate_idr_woman * 1.2
    elif frequency.upper() == 'B':
        idr = calculate_idr_woman * 1.375
    elif frequency.upper() == 'C':
        idr = calculate_idr_woman * 1.55
    elif frequency.upper() == 'D':
        idr = calculate_idr_woman * 1.725
    elif frequency.upper() == 'E':
        idr = calculate_idr_woman * 1.9
    else:
        print('Entrada inválida para nível de atividade.')
        idr = 0
    print(f'Sua Ingestão Diária Recomendada é de {idr:.2f} calorias por dia.')
else:
    print('Confira se não há nada de errado nos dados acima.')
