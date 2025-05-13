while True:
    num = int(input("Enter a number for multiplication table (or 0 to exit): "))
    
    if num == 0:
        print("Okay, Have a nice day :)")
        break

    print(f"\nMultiplication table for {num}:")

    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(f"\n{i} × {j} = {i*j}", end="  ")

        print()