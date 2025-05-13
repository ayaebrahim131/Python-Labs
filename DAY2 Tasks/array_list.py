def sort_array():
    numbers = [int(input(f"Pick a Number: ")) for i in range(5)]
    
    print(f"\nOriginal list: {numbers}")
    print(f"Ascending order: {sorted(numbers)}")
    print(f"Descending order: {sorted(numbers, reverse=True)}")

sort_array()