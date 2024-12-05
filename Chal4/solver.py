import re
import numpy as np


def count_regexes(regex, lines):
    count = 0
    for line in lines:
        count += len(regex.findall(line))
        count += len(regex.findall(line[::-1]))
    return count


def solve_first(data):
    xmas = re.compile(r"XMAS")
    horizontal = data.strip().split()
    arr = np.array([list(line) for line in horizontal])
    vertical = ["".join(line) for line in np.transpose(arr)]

    # Get diagonals
    lr_diagonal = get_lr_diagonals(arr)
    flipped = np.fliplr(arr)
    rl_diagonal = get_lr_diagonals(flipped)

    # Count the horizontal words
    count = 0
    count += count_regexes(xmas, horizontal)
    count += count_regexes(xmas, vertical)
    count += count_regexes(xmas, lr_diagonal)
    count += count_regexes(xmas, rl_diagonal)

    return count


def get_lr_diagonals(matrix):
    diagonals = []
    rows, cols = matrix.shape

    # Loop through all possible diagonals (negative to positive offsets)
    for offset in range(-rows + 1, cols):  # Covers all diagonals
        diagonal = "".join(matrix.diagonal(offset=offset))
        diagonals.append(diagonal)

    return diagonals


def solve_second(data):
    horizontal = data.strip().split()
    arr = np.array([list(line) for line in horizontal])
    patterns = [
        np.array([["M", 0, "M"], [0, "A", 0], ["S", 0, "S"]]),
        np.array([["M", 0, "S"], [0, "A", 0], ["M", 0, "S"]]),
        np.array([["S", 0, "M"], [0, "A", 0], ["S", 0, "M"]]),
        np.array([["S", 0, "S"], [0, "A", 0], ["M", 0, "M"]]),
    ]

    sum = 0
    rows, cols = arr.shape
    for i in range(rows - 2):
        for j in range(cols - 2):
            for reference in patterns:
                matrix = arr[i : i + 3, j : j + 3].copy()
                if check_matrix(matrix, reference):
                    sum += 1
                    continue

    return sum


def check_matrix(matrix, reference):
    indices = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]
    for i, j in indices:
        if not matrix[i, j] == reference[i, j]:
            return False
    return True


def main():
    with open("input", "r") as file:
        text = file.read()

    print(f"Solution (1): {solve_first(text)}")
    print(f"Solution (2): {solve_second(text)}")


if __name__ == "__main__":
    main()
