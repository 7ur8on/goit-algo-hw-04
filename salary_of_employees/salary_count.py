def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            count = 0
            total = 0
            for line in file:
                new_line = line.split(",")
                total += int(new_line[1])
                count += 1
            average = total // count
            return total, average
    except FileNotFoundError:
        print("File not found")

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")