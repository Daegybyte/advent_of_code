LETTERS_TO_DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_calibration_sum(lines: list[str]) -> int:
    calibration_sum = 0

    for line in lines:
        first_number, last_number = None, None

        for i, char in enumerate(line):
            if char.isdigit():
                if first_number is None:
                    first_number = int(char)
                last_number = int(char)
            else:
                for length in range(5, 2, -1):
                    if i < len(line) - length + 1 and line[i:i + length] in LETTERS_TO_DIGITS:
                        if first_number is None:
                            first_number = LETTERS_TO_DIGITS[line[i:i + length]]
                        last_number = LETTERS_TO_DIGITS[line[i:i + length]]
                        break

        calibration_sum += int(f"{first_number}{last_number}") if first_number is not None and last_number is not None else 0

    return calibration_sum


def main() -> None:
    import os
    script_directory = os.path.dirname(os.path.realpath(__file__))

    file_path = os.path.join(script_directory, "input.txt")
    
    with open(file_path, "r") as f:
        result = get_calibration_sum(f.readlines())
        print(result)


if __name__ == "__main__":
    main()
