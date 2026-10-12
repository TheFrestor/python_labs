import re 

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    text = text.replace("\\t", " ").replace("\\r", " ").replace("\\n", " ").split()

    return " ".join(text)

#print(normalize(input("Введите текст:")))

def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+(?:-\w+)*", text)

#print(tokenize(input("Введите текст: ")))

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

#print(count_freq(tokenize(input("Введите текст: "))))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]

print(top_n(count_freq(tokenize(input("Введите текст: ")))))