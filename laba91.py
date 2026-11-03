def find_missing_numbers(arr):
    if len(arr)<2:
        return[]
    missing = []
    for i in range(len(arr)-1):
        start = int(arr[i])+1
        end = int(arr[i+1])
        for num in range(start, end):
            missing.append(num)
            
    return missing
arr = [-3, -2, 1, 5]
print(find_missing_numbers(arr))