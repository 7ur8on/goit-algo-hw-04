import pathlib

def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file: # менеджер контексту для читання файлів
            total = 0 # початкова загальна зарплата
            count = 0 # початкова кількість людей
            for line in file: # ітеруєм по рядках
                name, salary = line.strip().split(',') # розділяєм рядок "," на ім'я і зарплатню
                total += int(salary) # додаєм повну зарплатню до загальної сумми
                count += 1 # додаєм до загальної кількості людей
            average = total / count if count > 0 else 0 # середня зарплатня і перевіряєм чи кількість людей = 0
            return total, int(average) # повертаєм загальну суму і середню
    except FileNotFoundError:
        return "Файл не знайдено.", None # повертаєм повідомлення як що файл не найдений

if __name__ == "__main__": # чи є поточний файл головним
    total, average = total_salary("salary_of_employees/salary_file.txt") # викликаєм фунцію із шляхом до файлу
    if isinstance(total, str): # перевіряємо чи загальна сума є рядком
        print(total)
    else:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") # виводим повідомлення
