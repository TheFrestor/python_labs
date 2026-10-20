import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает всё содержимое файла и возвращает одной строкой.

    По умолчанию используется UTF-8. Для другой кодировки надо передать её явно,
    например: read_text(path, encoding="cp1251").
    """
    try:
        file_path = Path(path)
        return file_path.read_text(encoding=encoding)
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return ""
    except UnicodeDecodeError:
        print(f"Ошибка декодирования файла {path} с кодировкой {encoding}")
        return ""


def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории для path, если их ещё нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True) 
    
def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """Записывает строки в CSV с разделителем-запятой.

    Если передан header, он записывается первой строкой.
    Все строки данных должны иметь одинаковую длину.
    """
    if header is not None:
        expected_length = len(header)
    else:
        expected_length = None
    for row in rows:
        if expected_length is None:
            expected_length = len(row)
        elif len(row) != expected_length:
            raise ValueError("Все строки CSV должны иметь одинаковую длину")

    ensure_parent_dir(path)
    with Path(path).open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")

        if header is not None:
            writer.writerow(header)

        writer.writerows(rows)


text = read_text("src/data/lab04/input.txt") 
write_csv([("word", "count"), ("test", 3)], "src/data/lab04/test.csv")
print(text)