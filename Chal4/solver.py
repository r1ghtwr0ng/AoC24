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
    return None


def main():
    with open("input", "r") as file:
        text = file.read()

    print(f"Solution (1): {solve_first(text)}")
    print(f"Solution (2): {solve_second(text)}")


if __name__ == "__main__":
    main()
