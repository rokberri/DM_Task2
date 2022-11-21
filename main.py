def read_file(filename_name):
    matrix = []
    with open(filename_name, "r") as file:
        for line in file:
            for el in line.split(' '):
                matrix.append(int(el))
    return matrix


def write_to_file(am_of_comp):
    with open("output.txt", 'w') as file:
        file.write(str(am_of_comp))


def pos_search(matrix, target):
    pos = -1
    am_of_comp = 0

    for num in matrix:
        am_of_comp += 1
        pos += 1
        if num == target:
            return am_of_comp


def binary_search(matrix, target):
    mid = len(matrix) // 2
    low = 0
    high = len(matrix) - 1
    am_of_comp = 0

    while matrix[mid] != target and low <= high:
        if target > matrix.__getitem__(mid):
            low = mid + 1
        else:
            high = mid - 1
        am_of_comp += 1
        mid = (low + high) // 2
    if low > high:
        am_of_comp += 1
        return am_of_comp
    else:
        am_of_comp += 1
        return am_of_comp


def interpolation_search(matrix, target):
    low = 0
    am_of_comp = 0
    high = (len(matrix) - 1)
    while low <= high and target >= matrix[low] and target <= matrix[high]:
        index = low + int(((float(high - low) / (matrix[high] - matrix[low])) * (target - matrix[low])))
        if matrix[index] == target:
            am_of_comp += 1
            return am_of_comp
        if matrix[index] < target:
            low = index + 1
        else:
            high = index - 1
        am_of_comp += 1
    return -1

def main():
    mas = read_file("input.txt")
    # print(read_file("input.txt").__getitem__(0))
    print("1. Последовательный поиск\n2. Бинарный поиск\n3. Интерполяционный поиск")
    variant = int(input("Выберите поиск "))
    sr_znach = 0
    if variant == 1:
        for num in mas:
            sr_znach += pos_search(mas, num)
    elif variant == 2:
        for num in mas:
            sr_znach += binary_search(mas, num)
    elif variant == 3:
        for num in mas:
            interpolation_search(mas, num)
    write_to_file(sr_znach / len(mas))


if __name__ == '__main__':
    main()


