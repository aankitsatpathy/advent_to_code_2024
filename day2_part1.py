def parse_file(file_path):
    s=0
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    data = []
    for line in lines:
        # Split each line into integers and store as an array
        numbers = list(map(int, line.split()))
        print(numbers, end="")  # Print the array of numbers
        
        # Check if the list is sorted in ascending or descending order
        sorted_asc = numbers == sorted(numbers)
        sorted_desc = numbers == sorted(numbers, reverse=True)
        
        if sorted_asc or sorted_desc :
            print(" - Sorted ",end="")            
            f=0
            for i in range(len(numbers)-1):
              diff=abs(numbers[i]-numbers[i+1])
              if(diff>0 and diff<=3):
                f=0
              else:
                f=1
                break
            if(f==0):
              print("Safe")
              s+=1
            else:
              print("Unsafe")
        else:
            print("Unsafe")
    print(s)
    return data
file_path = 'input_advent_d1p1.txt'
parse_file(file_path)
