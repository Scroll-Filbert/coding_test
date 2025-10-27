def main():
    n = 10  # Example input
    print(f"Fibonacci of {n} is {fibonacci(n)}")

def fibonacci(n):
    '''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    '''
    
    ans = [0,1]

    for i in range(2,n+1):
        ans.append(ans[i-1]+ans[i-2])
    return ans[n]
    
if __name__ == "__main__":
    main()