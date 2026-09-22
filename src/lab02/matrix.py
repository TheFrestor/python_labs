def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0 : raise ValueError
    if len(mat) == 1: return [list(i) for i in zip(*mat)]
    if len(mat) > 1:
        for i in mat:
            if len(i) != len(mat[0]):
                raise ValueError
    return [list(i) for i in zip(*mat)]
print(transpose(eval(input())))