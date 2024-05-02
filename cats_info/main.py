def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                cat_info = {"id": data[0], "name": data[1], "age": data[2]}
                cats_info.append(cat_info)
    except FileNotFoundError:
        print("Файл не знайдено!")
    except Exception as e:
        print("Сталася помилка:", e)
    return cats_info
cats_info = get_cats_info("cats_info/cats_file.txt")
print(cats_info)