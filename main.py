
import os
import panasiuk_files


directory = os.path.join(os.path.expanduser("~"), "Documents")

print("1. Список файлів:")
try:
    files = panasiuk_files.list_files(directory)
    print(files)
except OSError as error:
    print("Помилка:", error)


print("\n2. Пошук файлів зі словом 'практична':")
try:
    found = panasiuk_files.find_files(directory, "практична")
    print(found)
except OSError as error:
    print("Помилка:", error)


print("\n3. Створення файлу:")
path = os.path.join(directory, "Panasiuk_Vlad.txt")

panasiuk_files.create_file(
    path,
    "Ім'я: Влад\nПрізвище: Панасюк\nГрупа: ІТ-31"
)

print("Файл створено:", path)
