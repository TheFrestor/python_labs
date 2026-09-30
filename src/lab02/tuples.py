def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec) is not tuple:
        raise TypeError("Входные данные должны быть кортежем")
    if len(rec)!= 3 :
        raise ValueError ("Некорректный ввод")
    if not rec[0].strip():
        raise ValueError("ФИО не может быть пустым")

    if not rec[1].strip():
        raise ValueError("Группа не может быть пустой")

    if not isinstance(rec[2], (int, float)):
        raise TypeError("GPA должен быть числом")

    fio = rec[0].split()

    if len(fio) == 3:
        name = fio[0].capitalize() + " " + fio[1][0].upper() + "." + fio[2][0].upper() + "."
    elif len(fio) == 2:
        name = fio[0].capitalize() + " " + fio[1][0].upper() + "."
    else:
        raise ValueError("Некорректное ФИО")

    return f"{name}, гр. {rec[1]}, GPA {rec[2]:.2f}"

rec = eval(input())
print(format_record(rec))