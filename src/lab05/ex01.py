import json
from pathlib import Path
import csv
from src.lib.func import ensure_parent_dir

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    js = Path(json_path)
    cs = Path(csv_path)
    if js.suffix.lower() != ".json":
        raise ValueError("Ожидается файл .json")
    if cs.suffix.lower() != ".csv":
        raise ValueError("Ожидается файл .csv")
    if not js.exists():
        raise FileNotFoundError("Указанный файл JSON не существует")

    with js.open("r",encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError :
            raise ValueError("Пустой или некорректный JSON") 
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("Ожидается непустой список")

        for row in data:
            if not isinstance(row, dict):
                raise ValueError("Все элементы списка JSON должны быть словарями")
        ensure_parent_dir(cs)
        header = list(data[0].keys())
        for row in data[1:]:
            for key in row:
                if key not in header:
                    header.append(key)
    with cs.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header, restval="")
        writer.writeheader()
        writer.writerows(data)  

json_to_csv("data/lab05/samples/people.json", "data/lab05/out/people_from_json.csv")


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    js = Path(json_path)
    cs = Path(csv_path)
    if js.suffix.lower() != ".json":
        raise ValueError("Ожидается файл .json")
    if cs.suffix.lower() != ".csv":
        raise ValueError("Ожидается файл .csv")
    if not cs.exists():
        raise FileNotFoundError("Указанный файл CSV не существует")

    with cs.open("r",encoding="utf-8",newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("В CSV нет заголовка")
        data = list(reader)
        if not data:
            raise ValueError("В CSV нет строк данных")
        
    ensure_parent_dir(js)
    with js.open("w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False, indent = 2)
    
#csv_to_json("data/lab05/samples/people.csv", "data/lab05/out/people_from_csv.json")

#if __name__ == "__main__":
#    csv_to_json(
#        "data/lab05/samples/people.csv",
#        "data/lab05/out/people_from_csv.json"
#    )
