def mario_pyramid():
    height = int(input("Enter pyramid height: "))
    
    pyramid = [] 
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        blocks = '#' * i
        row = spaces + blocks
        pyramid.append(row)
    
    for row in pyramid:
        print(row)

mario_pyramid()
