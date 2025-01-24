from math import pow

print('\033[1;32;31m Attention! Enter your height in centimeters and without punctuation. \033[m')
print('=' * 50)

while True:
    genre = input('Enter your gender (male/female): ').strip().lower()
    if genre not in ['male', 'female']:
        print("Invalid input! Please enter 'male' or 'female'.")
        continue

    try:
        age = int(input('Enter your age: '))
        if age <= 0:
            print("Invalid age! Please enter a positive number.")
            continue
    except ValueError:
        print("Invalid input! Please enter an integer for age.")
        continue

    try:
        height = int(input('Enter your height in centimeters: '))
        if height <= 0:
            print("Invalid height! Please enter a positive number.")
            continue
    except ValueError:
        print("Invalid input! Please enter an integer for height.")
        continue
    try:
        weight = float(input('Enter your weight in kilograms: '))
        if weight <= 0:
            print("Invalid weight! Please enter a positive number.")
            continue
    except ValueError:
        print("Invalid input! Please enter a valid number for weight.")
        continue

    break
print('=' * 50)

# Height conversion to meters
height_in_metro = height / 100

# BMI calculation
calculate_imc = weight / pow(height_in_metro, 2)

# IDR calculation for men and women
calculate_idr_man = (13.75 * weight) + (5 * height) - (6.76 * age)
calculate_idr_woman = (9.56 * weight) + (1.85 * height) - (4.68 * age) + 665

print("""\n \033[1m BMI Calculation \033[m
BMI (Body Mass Index) is used to calculate the ideal weight by dividing weight by height squared. 
A BMI between 18.5 and 24.9 indicates normal weight.""")

# Displaying BMI classification
print('\033[1;37m \n Body Mass Index Data: \033[m')

if calculate_imc < 18.5:
    print(f'Your BMI: {calculate_imc:.1f} \nClassification: Underweight')
elif 18.5 <= calculate_imc <= 24.9:
    print(f'Your BMI: {calculate_imc:.1f} \nClassification: Normal')
elif 25.0 <= calculate_imc <= 29.9:
    print(f'Your BMI: {calculate_imc:.1f} \nClassification: Overweight \nObesity Degree: 1')
elif 30.0 <= calculate_imc <= 39.9:
    print(f'Your BMI: {calculate_imc:.1f} \nClassification: Obesity \nObesity Degree: 2')
else:
    print(f'Your BMI: {calculate_imc:.1f} \nClassification: Severe Obesity \nObesity Degree: 3')

# Activity level selection
print('\n \033[1m Activity Level:\033[m')
print('A - Sedentary \nB - Light Activity \nC - Moderate Activity \nD - Intense Activity \nE - Extreme Activity')

frequency = input('\n \033[1;30m Enter the frequency corresponding to the letter: \033[m').strip().upper()

# IDR calculation based on activity level
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
    print('Invalid input for activity level.')
    multiplier = 0

if multiplier > 0:
    if genre == 'male':
        idr = calculate_idr_man * multiplier
    elif genre == 'female':
        idr = calculate_idr_woman * multiplier
    print(f'Your Recommended Daily Intake is {idr:.2f} calories per day.')
else:
    print('Unable to calculate your IDR.')
      