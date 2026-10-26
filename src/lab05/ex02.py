import csv
from pathlib import Path
from openpyxl import Workbook

def ensure_parent_dir(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csp = Path(csv_path)
    xlp = Path(xlsx_path)

    if csp.suffix.lower() != ".csv":
        raise ValueError("Ожидается файл .csv")
    if xlp.suffix.lower() != ".xlsx":
        raise ValueError("Ожидается файл .xlsx")
    if not csp.exists():
        raise FileNotFoundError("Указанный файл CSV не существует")

    with csp.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        raise ValueError("Файл CSV пустой")
    if not rows[0] or not any(cell.strip() for cell in rows[0]):
        raise ValueError("В CSV отсутствует заголовок")

    wb = Workbook()
    sheet = wb.active
    sheet.title = "Sheet1"

    for row in rows:
        sheet.append(row)

    for column in sheet.columns:
        max_length = 0

        for cell in column:
            if cell.value is not None:
                text = str(cell.value)
                if len(text) > max_length:
                    max_length = len(text)

        column_letter = column[0].column_letter

        if max_length < 8:
            max_length = 8

        sheet.column_dimensions[column_letter].width = max_length

    ensure_parent_dir(xlp)
    wb.save(xlp)


if __name__ == "__main__":
    csv_to_xlsx(
        "data/lab05/samples/people.csv",
        "data/lab05/out/people.xlsx"
    )