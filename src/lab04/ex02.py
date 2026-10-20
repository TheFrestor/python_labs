from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv


def main():
    text = read_text("src/data/lab04/input.txt")

    if not text:
        return

    text = normalize(text)
    tokens = tokenize(text)
    freq = count_freq(tokens)

    top_words = top_n(freq)
    top_words = sorted(top_words, key=lambda item: (-item[1], item[0]))
    sorted_words = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

    write_csv(sorted_words, "data/lab04/report.csv", header=("word", "count"))

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for i in top_words:
        print(f"{i[0]}: {i[1]}")


if __name__ == "__main__":
    main()