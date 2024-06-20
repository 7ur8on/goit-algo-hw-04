def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats_dict = []
            for line in file:
                new_line = line.strip().split(",")
                cats_dict.append({"id": new_line[0], "name": new_line[1], "age": new_line[2]})
            return cats_dict
    except FileNotFoundError:
        print("File Not Found")

        
cats_info = get_cats_info("cats_file.txt")
print(cats_info)
