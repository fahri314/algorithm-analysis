def reduce(matris):
    for i in range(min(len(matris), len(matris[0]))):
        for r in range(i, len(matris)):
            row = matris[r][i] == 0
            if row:
                continue
            matris[i], matris[r] = matris[r], matris[i]
            first_r_first_c = matris[i][i]
            for r in range(i + 1, len(matris)):
                row_first = matris[r][i]
                multiple = -1 * row_first / first_r_first_c
                for c in range(i, len(matris[0])):
                    matris[r][c] += matris[i][c] * multiple
            break
    print(matris)
    for i in range(min(len(matris), len(matris[0])) - 1, -1, -1):
        first_e_col = -1
        first_e = -1
        for c in range(len(matris[0])):
            if matris[i][c] == 0:
                continue
            if first_e_col == -1:
                first_e_col = c
                first_e = matris[i][c]
            matris[i][c] /= first_e
        for r in range(i):
            row_a = matris[r][first_e_col]
            multiple = -1 * row_a
            for c in range(len(matris[0])):
                matris[r][c] += matris[i][c] * multiple
    print(matris)
    
a = [[1, 2, 5, 4], [4, 5, 7, 3], [3, 6, 8, 2],[6, 8, 4, 3]]
reduce(a)

b = [[1],[1],[1],[1]]

from scipy import linalg

print linalg.solve(a,b)

# https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/null-column-space/v/null-space-2-calculating-the-null-space-of-a-matrix