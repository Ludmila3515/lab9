


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
def power(x, y):
    return x ** y


# Эта программа всего лишь учебный пример
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")

print("5. Возведение в степень")


while True:


    choice = input("Введите номер операции (1/2/3/4/5): ")



    if choice in ['1', '2', '3', '4','5']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")


        elif choice == '5':
            print(f"{num1} в степени {num2} = {power(num1, num2)}")

        

        # Спрашиваем пользователя, хочет ли он продолжить
        next_calculation = input("Хотите выполнить еще один расчет? (да/нет): ")
        if next_calculation.lower() != 'да':
            break
    else:
        print("Неверный ввод. Пожалуйста, выберите номер операции от 1 до 5.")
