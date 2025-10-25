#Swap number between variables

def main():
    x = 5
    y = 10

    print(f"Variables before swapping : {x} and {y} ")

    x, y = y, x

    print(f"Variables after swapping : {x} and {y} ")

if __name__ == "__main__":
    main()