def calculate_bmi(weight, height): # Function to calculate BMI
    bmi = weight / (height / 100) ** 2
    return round(bmi, 2)

def main(): # Main function
    while True:
        try:
            weight = float(input('Enter your weight in kg: '))
            if weight > 0:
                break
            else:
                print('Weight must be greater than zero.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    while True:
        try:
            height = float(input('Enter your height in cm: '))
            if height > 0:
                break
            else:
                print('Height must be greater than zero.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    bmi = calculate_bmi(weight, height)
    print(f'Your BMI is {bmi}')

if __name__ == '__main__':
    main()