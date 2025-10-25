'''
Example:

Input: 19
Output: True
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
End result 1 = True, else False
'''

def main():
    seen = []
    cur = str(50)
    result = 0

    while cur not in seen:
        seen.append(cur)
        result = 0
        for digit in cur:
            digit = int(digit)
            result += digit **2

        if result == 1 : 
            print("True")
            return True
        cur = str(result)
    print("False")
    return False

if __name__ == "__main__":
    main()