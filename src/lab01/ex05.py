name = input("ФИО: ").split()
print(f"Инициалы: {''.join(i[0] for i in name)}.\nДлина (символов):{len(name[0])+len(name[1])+len(name[2])+2}")

