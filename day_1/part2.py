import re
import os
def extract_digits(line):
    # Extract digits (both actual digits and spelled-out digits) from the line
    digits = re.findall(r'\d+|[a-z]+', line.lower())
    
    # Convert spelled-out digits to actual digits
    digit_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    digits = [digit_mapping.get(d, d) for d in digits]
    print(digits)
    
    # Extract the first and last digits
    first_digit = str(digits[0])
    last_digit = str(digits[-1])
    
    return first_digit, last_digit

def calculate_calibration_sum(calibration_document):
    # Split the document into lines and concatenate the first and last digits
    concatenated_digits = ""
    
    for line in calibration_document:
        if line:
            first_digit, last_digit = extract_digits(line)
            concatenated_digits += first_digit + last_digit
    
    return concatenated_digits

if __name__ == "__main__":    
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Combine the script directory with the file name
    file_path = os.path.join(script_directory, "input.txt")
    
    with open(file_path) as f:
        lines = [line.strip() for line in f]
    # print(lines)    
    nums = []
    for line in lines:
        n = ''.join(filter(str.isdigit, line))
        if n:
            nums.append(int(n))
    print(nums)
    
    # print(sum(nums))
    
    nums_modded = []
    for num in nums:
        if 0 < num < 10:
            num = num * 11
            nums_modded.append(num)
            continue
        elif 10 <= num < 100:
            nums_modded.append(num)
            continue
        else:
            num_str = str(num)
            new_num = int(num_str[0] + num_str[-1])
            nums_modded.append(new_num)

    print(nums_modded)
    print(sum(nums_modded))