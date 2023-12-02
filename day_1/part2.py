import re
import os


def extract_digits(line):
    # Extract digits (both actual digits and spelled-out digits) from the line
    digits = re.findall(r'\d+|[a-z]+', line.lower())
    
    # Convert spelled-out digits to actual digits
    digit_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    for i in range(len(digits)):
        if digits[i] in digit_mapping:
            digits[i] = digit_mapping[digits[i]]
    
    print(digits)
    
    # Extract the first and last digits
    first_digit = str(digits[0])
    last_digit = str(digits[-1])
    
    return first_digit, last_digit

# Rest of your code...



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
    
    result = calculate_calibration_sum(lines)
    print(result)
    