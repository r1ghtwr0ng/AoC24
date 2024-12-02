import numpy as np


def solve_first(data):
    acc = 0
    reports = data.strip().split("\n")
    for idx, report in enumerate(reports):
        data = np.array([int(x) for x in report.split()])
        diff = np.zeros(data.size - 1, dtype="int")
        for i in range(1, len(data)):
            diff[i - 1] = data[i - 1] - data[i]

        # Check if all decrease or increase in given range
        valid_hi = np.all((diff > 0) & (diff <= 3))
        valid_lo = np.all((diff < 0) & (diff >= -3))
        if valid_hi ^ valid_lo:
            acc += 1
    return acc


def dampen(orig_data):
    for i in range(orig_data.size):
        data = np.delete(orig_data, i)
        diff = np.zeros(data.size - 1, dtype="int")
        for i in range(1, len(data)):
            diff[i - 1] = data[i - 1] - data[i]

        # Check if all decrease or increase in given range
        valid_hi = np.all((diff > 0) & (diff <= 3))
        valid_lo = np.all((diff < 0) & (diff >= -3))
        if valid_hi ^ valid_lo:
            return True
    return False


def solve_second(data):
    acc = 0
    reports = data.strip().split("\n")
    for idx, report in enumerate(reports):
        data = np.array([int(x) for x in report.split()])
        diff = np.zeros(data.size - 1, dtype="int")
        for i in range(1, len(data)):
            diff[i - 1] = data[i - 1] - data[i]
        # Check if all decrease or increase in given range
        valid_hi = np.all((diff > 0) & (diff <= 3))
        valid_lo = np.all((diff < 0) & (diff >= -3))
        if valid_hi ^ valid_lo:
            acc += 1
        elif dampen(data):
            acc += 1

    return acc


def main():
    with open("input", "r") as file:
        text = file.read()

    print(f"Solution (1): {solve_first(text)}")
    print(f"Solution (2): {solve_second(text)}")


if __name__ == "__main__":
    main()
