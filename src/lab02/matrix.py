def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0 : return []
    if len(mat) == 1: return [list(i) for i in zip(*mat)]
    if len(mat) > 1:
        for i in mat:
            if len(i) != len(mat[0]):
                raise ValueError("рваная матрица")
    return [list(i) for i in zip(*mat)]

print(transpose(eval(input())))

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0: raise ValueError
    if len(mat) > 0:
        for i in mat:
            if len(i) != len(mat[0]):
                raise ValueError("рваная матрица")
    return [sum(i) for i in mat]

print(row_sums(eval(input())))

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0: raise ValueError
    if len(mat) > 0:
        for i in mat:
            if len(i) != len(mat[0]):
                raise ValueError("рваная матрица")
    return [sum(i) for i in zip(*mat)]

print(col_sums(eval(input())))