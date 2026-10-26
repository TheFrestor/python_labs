import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    text = text.replace("\\t", " ").replace("\\r", " ").replace("\\n", " ").split()

    return " ".join(text)


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]


import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает всё содержимое файла и возвращает одной строкой.

    По умолчанию используется UTF-8. Для другой кодировки передайте её явно,
    например: read_text(path, encoding="cp1251").
    """
    file_path = Path(path)
    return file_path.read_text(encoding=encoding)


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

    with Path(path).open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")

        if header is not None:
            writer.writerow(header)

        writer.writerows(rows)
