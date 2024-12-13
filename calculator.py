def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y




print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")


while True:
    choice = input("Введите номер операции (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        

        # Спрашиваем пользователя, хочет ли он продолжить
        next_calculation = input("Хотите выполнить еще один расчет? (да/нет): ")
        if next_calculation.lower() != 'да':
            break
    else:
        print("Неверный ввод. Пожалуйста, выберите номер операции от 1 до 4.")
