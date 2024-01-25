def pattern_search(P, I):
    def rotate_matrix(matrix):
        result = []
        wanted = []
        for col in reversed(range(len(matrix[0]))):
            row = ""
            for row_str in matrix:
                row += row_str[col]
            result.insert(0, row)
        for a in result:
            k = a[::-1]
            wanted.append(k)
        return wanted

    u = rotate_matrix(P)
    y = rotate_matrix(u)
    t = rotate_matrix(y)
    patterns = [P, u, y, t]

    for pattern in patterns:
        for j in range(len(I[0]) - len(pattern[0]) + 1):
            for i in range(len(I) - len(pattern)+1):
                w = pattern[0]
                if w == I[i][j:j+len(w)]:
                    o = 1
                    check = 1
                    if o == len(pattern) and o == len(pattern[0]):
                        return (i,j,0)
                    else:
                        while o < len(pattern):
                            if pattern[o] == I[i+o][j:j+len(w)]:
                                o+=1
                                check+=1
                                if check == len(pattern):
                                    if patterns.index(pattern) == 0:
                                        Theta = 0
                                        return (i, j, Theta)
                                    if patterns.index(pattern) == 1:
                                        Theta = 90
                                        return (i, j, Theta)
                                    if patterns.index(pattern) == 2:
                                        Theta = 180
                                        return (i, j, Theta)
                                    if patterns.index(pattern) == 3:
                                        Theta = 270
                                        return (i, j, Theta)
                            else:
                                o = len(pattern)
    return False
