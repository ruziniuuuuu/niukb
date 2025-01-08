def func(n, a):
    tot = sum(a)
    half = tot // 2
    dp = [False] * (half + 1)
    dp[0] = True
    
    for ele in a:
        for i in range(half, ele - 1, -1):
            dp[i] |= dp[i - ele]
            
    for i in range(half, -1, -1):
        if dp[i]:
            return abs(tot - 2*i)
    

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    
    print(func(n, a))