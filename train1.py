# создайте переменную
my_heigh = 175
print(my_heigh)

# перезапишите переменную
my_name = "Вика"
my_name = "Виктория"
print(my_name)

# получите пользовательский ввод
pet_name = input("Как зовут вашего питомца? ")
print("Ваш любимчик - " + pet_name)

# создание функции
def print_python():
    print("Учу Python!")


print_python()

# параметризация функций
def print_letter(let):
    print(let, end='')


print_letter('М')
print_letter('у')
print_letter('р')
