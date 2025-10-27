from collections import Counter

def main():
    arr = [1,2,2,1,1,3]
    counter = Counter(arr)
    print(f"Counter: {counter}")
    s = set()
    for i in counter.values():
        if i in s:
            print(False)
            return
        else:
            s.add(i)
    print(True)

if __name__ == "__main__":
    main()
