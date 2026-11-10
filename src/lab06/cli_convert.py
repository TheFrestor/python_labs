import argparse
from pathlib import Path

from src.lab05.ex01 import json_to_csv, csv_to_json
from src.lab05.ex02 import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры JSON, CSV и XLSX")
    subparsers = parser.add_subparsers(dest="command", required=True)

    json_parser = subparsers.add_parser("json2csv", help="Преобразовать JSON в CSV")
    csv_parser = subparsers.add_parser("csv2json", help="Преобразовать CSV в JSON")
    xlsx_parser = subparsers.add_parser("csv2xlsx", help="Преобразовать CSV в XLSX")

    for command_parser in (json_parser, csv_parser, xlsx_parser):
        command_parser.add_argument("--in", dest="input", required=True, help="Путь к входному файлу")
        command_parser.add_argument("--out", dest="output", required=True, help="Путь к выходному файлу")

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    try:
        if not input_path.is_file():
            raise FileNotFoundError(f"входной файл не найден: {input_path}")

        if input_path.resolve() == output_path.resolve():
            parser.error("входной и выходной файлы должны различаться")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        if args.command == "json2csv":
            json_to_csv(args.input, args.output)

        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)

        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)

    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()