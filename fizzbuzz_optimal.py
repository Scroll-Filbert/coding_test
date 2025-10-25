def main():
    for i in range(1, 101):       # 1..100 inclusive
        text = ""

        if i % 3 == 0:
            text += "Fizz"
        if i % 5 == 0:
            text += "Buzz"
        if i % 7 == 0:
            text += "Bazz"

        print(text or i)

if __name__ == "__main__":
    main()