import copy


def get_first_matrix():
    first_matrix = []
    first_row, first_column = input('Enter matrix size:').split()
    print('Enter matrix:')
    for i in range(int(first_row)):
        row = [int(i) if i.isalnum() else float(i) for i in input().split()]
        first_matrix.append(row)
    return first_matrix, first_row, first_column


def get_second_matrix():
    second_matrix = []
    second_row, second_column = input('Enter matrix size:').split()
    print('Enter matrix:')
    for i in range(int(second_row)):
        row = [int(i) if i.isalnum() else float(i) for i in input().split()]
        second_matrix.append(row)
    return second_matrix, second_row, second_column


def check_matrix_for_sum(first_matrix, first_row, first_column, second_matrix, secodn_row, second_column):
    sum_matrix = []
    if not (first_row == secodn_row and first_column == second_column):
        print('ERROR')
        return False
    else:
        for row in range(len(first_matrix)):
            row_sum = [(str(first_matrix[row][column] + (second_matrix[row][column]))) for column in
                       range(len(first_matrix[row]))]

            sum_matrix.append(row_sum)
    for i in sum_matrix:
        print(' '.join(i))


def get_scalar():
    scalar = int(input())
    return scalar


def matrix_multiply(matrix, scalar):
    multiply_matrix = []
    for row in matrix:
        multiple = [str(i * scalar) for i in row]
        multiply_matrix.append(multiple)
    for i in multiply_matrix:
        print(' '.join(i))
    return multiply_matrix


def two_matrix_multiply(first_matrix, first_row, first_column, second_matrix, second_row, second_column):
    result_matrix = []
    if not first_column == second_row:
        print('ERROR')
    else:
        for row in range(len(first_matrix)):
            result_mul_row = [str(sum([first_matrix[row][column] * (second_matrix[column][j]) for column in
                                       range(len(first_matrix[row]))])) for j in range(int(second_column))]

            print(' '.join(result_mul_row))


def main_diagnal(first_matrix, first_row, first_column):
    transpose_matrix = []
    for i in range(int(first_column)):
        transpose_matrix.append([j for j in range(int(first_row))])
    for i in range(int(first_row)):
        for j in range(int(first_column)):
            transpose_matrix[j][i] = first_matrix[i][j]
    return transpose_matrix


def side_diagnal(first_matrix, first_row, first_column):
    transpose_matrix = []
    for i in range(int(first_column)):
        transpose_matrix.append([j for j in range(int(first_row))])
    for i in range(int(first_row)):
        for j in range(int(first_column)):
            transpose_matrix[int(first_column) - 1 - j][int(first_row) - 1 - i] = (first_matrix[i][j])
    return transpose_matrix


def vertical_line(first_matrix, first_row, first_column):
    transpose_matrix = []
    for i in range(int(first_row)):
        transpose_matrix.append([j for j in range(int(first_column))])
    for i in range(int(first_row)):
        for j in range(int(first_column)):
            transpose_matrix[i][int(first_column) - 1 - j] = str(first_matrix[i][j])
    [print(' '.join(i)) for i in transpose_matrix]


def horizontal_line(first_matrix, first_row, first_column):
    transpose_matrix = []
    for i in range(int(first_row)):
        transpose_matrix.append([j for j in range(int(first_column))])
    for i in range(int(first_row)):
        for j in range(int(first_column)):
            transpose_matrix[int(first_row) - 1 - i][j] = str(first_matrix[i][j])
    [print(' '.join(i)) for i in transpose_matrix]


def get_det_matrix(first_matrix):
    det = first_matrix[0][0] * first_matrix[1][1] - first_matrix[0][1] * first_matrix[1][0]
    return det


def get_high_order_determinant(first_matrix, c=1):
    result_list = []
    if not len(first_matrix[0]) >= 3:
        return first_matrix
    for i in range(len(first_matrix[0])):
        det_list = copy.deepcopy(first_matrix)
        det_list_row = first_matrix[0]
        det_list.remove(det_list[0])
        c = det_list_row[i]
        sign = 1 if i % 2 == 0 else -1
        c *= sign
        for j in det_list:
            del (j[i])
        if len(det_list[0]) == 2:
            det_result = c * get_det_matrix(det_list)
            result_list.append(det_result)
        else:
            result = c * get_high_order_determinant(det_list)
            result_list.append(result)
    return sum(result_list)


def determinant(first_matrix, first_row, first_column):
    if first_row != first_column:
        print('ERROR')
    elif first_row == '1':
        det = first_matrix[0][0]
        return det

    elif first_row == '2':
        det = get_det_matrix(first_matrix)
        return det
    else:
        first_matrix = get_high_order_determinant(first_matrix)
        return first_matrix


def get_cofactore(first_matrix):
    result_matrix = copy.deepcopy(first_matrix)
    for i in range(len(first_matrix)):
        for j in range(len(first_matrix[i])):
            det_list = copy.deepcopy(first_matrix)
            del (det_list[i])
            sign = 1 if (j + i) % 2 == 0 else -1
            for k in det_list:
                del (k[j])
            if len(det_list[0]) == 1:
                result_matrix[i][j] = det_list[0][0] * sign
            else:
                element_det = determinant(det_list, str(len(det_list)), str(len(det_list[0])))
                result_matrix[i][j] = element_det * sign
    return result_matrix


def get_reverse_matrix(first_matrix, first_row, first_column):
    if first_column != first_row:
        print('ERROR')
        return False
    det = determinant(first_matrix, first_row, first_column)
    if det == 0:
        print('ERROR')
        return False
    else:
        result_matrix = get_cofactore(first_matrix)
        rev_det = 1 / det
    c_matrix = main_diagnal(result_matrix, first_row, first_column)
    return matrix_multiply(c_matrix, rev_det)


quit_ = {'exit': True}
action_menue = {'1': 'Add matrices', '2': 'Multiply matrix by a constant',
                '3': 'Multiply matrices', '4': 'Transpose matrix',
                '5': 'Calculate a determinant', '6': 'Inverse matrix', '0': 'Exit'}
transpose_matrix = {'1': 'Main diagonal', '2': 'Side diagonal', '3': 'Vertical line',
                    '4': 'Horizontal line'}

if __name__ == '__main__':
    while quit_['exit']:
        [print(i + '.', j) for i, j in action_menue.items()]
        what_to_do = input()
        if what_to_do == '0':
            quit_['exit'] = False
        elif what_to_do == '1':
            check_matrix_for_sum(*get_first_matrix(), *get_second_matrix())
        elif what_to_do == '2':
            matrix, row, column = get_first_matrix()
            matrix_multiply(matrix, get_scalar())

        elif what_to_do == '3':
            two_matrix_multiply(*get_first_matrix(), *get_second_matrix())
        elif what_to_do == '4':
            [print(i + '.', j) for i, j in transpose_matrix.items()]
            what_transpose = input()
            if what_transpose == '1':
                transpose_matrix = main_diagnal(*get_first_matrix())
                other_transpose_matrix = copy.deepcopy(transpose_matrix)
                for i in range(len(transpose_matrix)):
                    for j in range(len(transpose_matrix[i])):
                        other_transpose_matrix[i][j] = str(transpose_matrix[i][j])
                [print(' '.join(i)) for i in other_transpose_matrix]

            elif what_transpose == '2':
                transpose_matrix = side_diagnal(*get_first_matrix())
                other_transpose_matrix = copy.deepcopy(transpose_matrix)
                for i in range(len(transpose_matrix)):
                    for j in range(len(transpose_matrix[i])):
                        other_transpose_matrix[i][j] = str(transpose_matrix[i][j])
                [print(' '.join(i)) for i in other_transpose_matrix]

            elif what_transpose == '3':
                vertical_line(*get_first_matrix())
            elif what_transpose == '4':
                horizontal_line(*get_first_matrix())
        elif what_to_do == '5':
            det = determinant(*get_first_matrix())
            print(det)
        elif what_to_do == '6':
            get_reverse_matrix(*get_first_matrix())
