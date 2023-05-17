def step(func_i, matrix_1, matrix_2):
    for m in range(len(matrix_2)):
        for n in range(len(matrix_2[m])):
            if matrix_2[m][n] == func_i:
                if m > 0 and matrix_2[m - 1][n] == 0 and matrix_1[m - 1][n] == 0:
                    matrix_2[m - 1][n] = func_i + 1
                if n > 0 and matrix_2[m][n - 1] == 0 and matrix_1[m][n - 1] == 0:
                    matrix_2[m][n - 1] = func_i + 1
                if m < len(matrix_2) - 1 and matrix_2[m + 1][n] == 0 and matrix_1[m + 1][n] == 0:
                    matrix_2[m + 1][n] = func_i + 1
                if n < len(matrix_2[m]) - 1 and matrix_2[m][n + 1] == 0 and matrix_1[m][n + 1] == 0:
                    matrix_2[m][n + 1] = func_i + 1


def path_maker(end_func, matrix_2, path):
    o, p = end_func
    end_val = matrix_2[o][p]

    path.append((o, p))

    while end_val > 1:

        if o > 0 and matrix_2[o - 1][p] == end_val - 1:
            o, p = o - 1, p
            path.append((o, p))
            end_val -= 1
        elif p > 0 and matrix_2[o][p - 1] == end_val - 1:
            o, p = o, p - 1
            path.append((o, p))
            end_val -= 1
        elif o < len(matrix_2) - 1 and matrix_2[o + 1][p] == end_val - 1:
            o, p = o + 1, p
            path.append((o, p))
            end_val -= 1
        elif p < len(matrix_2[o]) - 1 and matrix_2[o][p + 1] == end_val - 1:
            o, p = o, p + 1
            path.append((o, p))
            end_val -= 1

    return path


def first_message():
    print('**************************************')
    print('Hello! Welcome to my maze solver:)\n')
    print('To get started, tell us how many rows and columns your maze has:\n')
    print('For the second step, write the index of the start and the end point in the following format:\n'
          'Example:')
    print('1,3\n')
    print('Then, place the values in a matrix form like this:')
    print('1, 1, 1, 1, 1, 1, 1, 1, 1, 1, '
          '1, 0, 1, 0, 1, 0, 0, 0, 0, 1\n')
    print('Finally, you will see the path of your maze: ')
    print('**************************************\n')


"""""
This is an example for your better understanding:
Please pay attention that you should only write the values; not the names of the variables!

row, column = 10, 10
start_point = 1, 1
end_point = 2, 5
matrix1 = 
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 0, 1, 0, 1, 0, 0, 0, 0, 1,
         1, 0, 1, 0, 1, 0, 0, 0, 0, 1,
         1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
         1, 0, 1, 0, 0, 0, 0, 1, 0, 1,
         1, 0, 1, 0, 0, 0, 0, 1, 0, 1,
         1, 0, 0, 0, 0, 0, 0, 1, 0, 1,
         1, 0, 1, 0, 0, 0, 0, 0, 0, 1,
         1, 0, 1, 0, 0, 0, 0, 0, 0, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
"""""

if __name__ == '__main__':
    first_message()

    row_column = input().split(',')
    start_point_string = input().split(',')
    start_point = int(start_point_string[0].strip()), int(start_point_string[1].strip())

    end_point_string = input().split(',')
    end_point = int(end_point_string[0].strip()), int(end_point_string[1].strip())

    row, column = int(row_column[0].strip()), int(row_column[1].strip())

    matrix1 = [[0 for i in range(row)] for j in range(column)]

    path_visual = [[' ' for i in range(row)] for j in range(column)]

    for i in range(row):
        line_input = input().split(',')
        for j in range(column):
            int_input = int(line_input[j].strip())
            matrix1[i][j] = int_input
            if int_input == 1:
                path_visual[i][j] = '1'

    matrix2 = []

    for w in range(len(matrix1)):
        matrix2.append([])
        for q in range(len(matrix1[w])):
            matrix2[-1].append(0)

    i, j = start_point
    matrix2[i][j] = 1

    counter = 0
    while matrix2[end_point[0]][end_point[1]] == 0:
        counter += 1
        step(counter, matrix1, matrix2)

    end_path = []
    end_path = path_maker(end_point, matrix2, end_path)

    for point in end_path:
        path_visual[point[0]][point[1]] = '*'

    print()

    for i in range(row):
        for j in range(column):
            print(path_visual[i][j], end=' ')
        print()