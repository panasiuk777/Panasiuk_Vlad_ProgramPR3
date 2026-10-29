
import os


def list_files(directory):
    """
    Повертає список файлів у вказаній директорії.

    Args:
        directory (str): Шлях до директорії.

    Returns:
        list: Список назв файлів.
    """
    return [
        name for name in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, name))
    ]


def find_files(directory, substring):
    """
    Знаходить файли, у назві яких є вказаний підрядок.

    Args:
        directory (str): Шлях до директорії.
        substring (str): Підрядок для пошуку.

    Returns:
        list: Список знайдених файлів.
    """
    return [
        name for name in list_files(directory)
        if substring.lower() in name.lower()
    ]


def create_file(path, text):
    """
    Створює файл і записує в нього текст.

    Args:
        path (str): Шлях до файлу.
        text (str): Текст для запису.

    Returns:
        str: Шлях до створеного файлу.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)

    return path


if __name__ == "__main__":
    print("Самоперевірка модуля")

    directory = "."

    print("Список файлів:", list_files(directory))
    print("Пошук файлів з 'main':", find_files(directory, "main"))

    create_file(
        "test_file.txt",
        "Тест роботи модуля"
    )
    print("Створено файл test_file.txt")
