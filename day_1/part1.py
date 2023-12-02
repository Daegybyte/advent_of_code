import os
if __name__ == "__main__":    
    
    script_directory = os.path.dirname(os.path.realpath(__file__))

    file_path = os.path.join(script_directory, "input.txt")
    
    with open(file_path) as f:
        lines = [line.strip() for line in f]
    nums = []
    for line in lines:
        n = ''.join(filter(str.isdigit, line))
        if n:
            nums.append(int(n))
    print(nums)
        
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