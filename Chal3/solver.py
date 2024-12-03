import numpy as np
import re


def mul(instr):
    (op_1, op_2) = (int(y) for y in instr[4:-1].split(","))
    return op_1 * op_2


def solve_first(data):
    mul_regex = re.compile(r"mul\(\-?\d{1,10},\d{1,10}\)")
    sum = 0
    for instr in mul_regex.findall(data):
        sum += mul(instr)
    return sum


def solve_second(data):
    pass


def main():
    with open("input", "r") as file:
        text = file.read()

    print(f"Solution (1): {solve_first(text)}")
    print(f"Solution (2): {solve_second(text)}")


if __name__ == "__main__":
    main()
