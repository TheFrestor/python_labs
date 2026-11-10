import argparse

from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(description="Утилиты для работы с текстом")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Показать частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество самых частых слов")

    args = parser.parse_args()

    if args.command == "cat":
        try:
            with open(args.input, encoding="utf-8") as file:
                for number, line in enumerate(file, start=1):
                    line = line.rstrip("\r\n")
                    if args.n:
                        print(f"{number}: {line}")
                    else:
                        print(line)

        except FileNotFoundError:
            parser.error(f"файл не найден: {args.input}")

    elif args.command == "stats":
        if args.top <= 0:
            parser.error("--top должен быть больше нуля")

        try:
            with open(args.input, encoding="utf-8") as file:
                text = file.read()

        except FileNotFoundError:
            parser.error(f"файл не найден: {args.input}")

        normalized = normalize(text)
        tokens = tokenize(normalized)
        freq = count_freq(tokens)
        result = top_n(freq, args.top)

        for word, count in result:
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()