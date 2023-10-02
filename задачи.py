numbers = input("Введите список чисел через пробел: ").split()
numbers = [float(num) for num in numbers]
max_number = max(numbers)
min_number = min(numbers)
print(f"Наибольшее число: {max_number}, наименьшее число: {min_number}")

words = input("Введите список слов через пробел: ").split()
sorted_words = sorted(words)
print(f"Сортированный список слов: {sorted_words}")

students = {
    "Елизавета": 4,
    "Михаил": 3,
    "Илья": 5
}
students_tuples = list(students.items())
print(f"Список кортежей (имя, оценка): {students_tuples}")

text = input("Введите текст: ")
unique_words = set(text.split())
print(f"Уникальные слова в тексте: {unique_words}")

set1 = {3, 7, 14, 16}
set2 = {2, 3, 4, 5, 6, 7}
intersection = set1.intersection(set2)
print(f"Общие элементы множеств: {intersection}")

employees = {
    "Кузнецов": "Невролог",
    "Данилов": "Педиатр",
    "Бориосва": "Стоматолог"
}

def list_employees():
    for name, position in employees.items():
        print(f"{name}: {position}")

list_employees()

employees["Нестерчук"] = "Офтальмолог"
employees["Павлов"] = "Терапевт"
del employees["Данилов"]
print("\nОбновленный список сотрудников:")
list_employees()