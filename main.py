from math import inf


def edit_distance(x, y):
    m = len(x)
    n = len(y)
    c = []
    op = []
    for i in range(m + 1):
        c.append([])
        op.append([])
        for j in range(n + 1):
            c[i].append(None)
            op[i].append(None)
    for i in range(m + 1):
        c[i][0] = i * delete
        op[i][0] = "delete"
    for i in range(n + 1):
        c[0][i] = i * insert
        op[0][i] = "insert"
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            c[i][j] = inf
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + copy
                op[i][j] = "copy"
            if x[i-1] != y[j-1] and c[i-1][j-1] + replace < c[i][j]:
                c[i][j] = c[i-1][j-1] + replace
                op[i][j] = "replace by " + y[j-1]
            if i >= 2 and j >= 2 and x[i-1] == y[j-1-1] and x[i-1-1] == y[j-1] and c[i-2][j-2] + swap < c[i][j]:
                c[i][j] = c[i-2][j-2] + swap
                op[i][j] = "swap"
            if c[i-1][j] + delete < c[i][j]:
                c[i][j] = c[i-1][j] + delete
                op[i][j] = "delete"
            if c[i][j-1] + insert < c[i][j]:
                c[i][j] = c[i][j-1] + insert
                op[i][j] = "insert " + y[j - 1]
    return c, op


def op_sequence(op, i, j):
    if i == 0 and j == 0:
        return
    if op[i][j] == "copy" or op[i][j][0:7] == "replace":
        i1 = i - 1
        j1 = j - 1
    elif op[i][j] == "swap":
        i1 = i - 2
        j1 = j - 2
    elif op[i][j] == "delete":
        i1 = i - 1
        j1 = j
    else:
        i1 = i
        j1 = j - 1
    op_sequence(op, i1, j1)
    print(op[i][j])


if __name__ == '__main__':
    x = "algori"
    y = "argom"
    delete = 1
    insert = 1
    copy = 0
    replace = 1
    swap = 2
    c, op = edit_distance(x, y)
    print(c[len(x) - 1][len(y) - 1])
    op_sequence(op, len(x), len(y))

