# работа со списками
employee_list = ["John Snow", "Piter Pen", 
                 "Drakula", "IvanIV", "Moana", "Juilet"]
# sep= ставит символы между элементами
print(employee_list[1], employee_list[-2], sep=', ')

# вариант 2
employee_list = ["John Snow", "Piter Pen",
                 "Drakula", "IvanIV", "Moana", "Juilet"]

print(employee_list[1] + ", " + employee_list[-2])

# деление на три
def dev_by_three(n):
    if n % 3 == 0:
        return 'Да'
    else:
        return 'Нет'

num = 7
res = dev_by_three(num)
print(f"Делится ли на три {num}? - {res}")

# вариант 2
def dev_by_three(number):
    return "Да" if number % 3 == 0 else "Нет"

num = int(input("Введите число: "))
res = dev_by_three(num)
print(f"Делится ли на три {num}? - {res}")
