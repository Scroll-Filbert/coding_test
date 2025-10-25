def main():
    data = [0, 1, 3, 5, 0, 8, 9, 0, 5, 3]
    result = []

    for i in data :
        if data[i] != 0:
            result.append(data[i])
    
    print(result)

if __name__ == "__main__":
    main()