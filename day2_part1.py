def parse_file(file_path):
    safe_count = 0
    unsafe_data = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        # Parse each line into a list of integers
        numbers = list(map(int, line.split()))
        
        if is_safe(numbers):
            safe_count += 1
        else:
            unsafe_data.append(numbers)
    
    print(f"Number of safe arrays: {safe_count}")
    return unsafe_data,safe_count

def is_safe(numbers):
    # Check if the list is sorted (ascending or descending)
    sorted_asc = numbers == sorted(numbers)
    sorted_desc = numbers == sorted(numbers, reverse=True)
    
    if sorted_asc or sorted_desc:
        # Check differences between consecutive numbers
        for i in range(len(numbers) - 1):
            diff = abs(numbers[i] - numbers[i + 1])
            if diff <= 0 or diff > 3:
                return False
        return True
    return False

# File path
file_path = '/content/day2_data.txt'
parse_file(file_path)
