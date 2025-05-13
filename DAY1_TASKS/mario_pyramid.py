def print_mario_pyramid():
    max_stars = 4
    for stars in range(1, max_stars + 1):
        spaces = " " * (max_stars - stars)  
        print(f"  {spaces}{'*' * stars}")  

def main():  
    print_mario_pyramid()

main()  # Program starts here
 