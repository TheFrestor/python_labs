from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv


def main():
    text = read_text("src/data/lab04/input.txt", encoding="utf-8")
    words = tokenize(normalize(text))
    freq = count_freq(words)

    rows = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    write_csv(rows, "data/lab04/report.csv", header=("word", "count"))

    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    for word, count in top_n(freq):
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()