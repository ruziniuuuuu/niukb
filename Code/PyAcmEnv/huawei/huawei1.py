"""
无线基站名字相似度
"""

def func():
    # input a, b
    a = input()
    b = input()
    
    # define set 1 and set 2
    set1 = set('wirel@com')
    set2 = set('hfv#gbts')
    
    # define dp
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # init dp
    for i in range(m + 1):
        dp[i][0] = i * 3 # del
    for j in range(n + 1):
        dp[0][j] = j * 3 # add
    

    # fill in dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                if a[i - 1] in set1 and b[j - 1] in set1:
                    cost = 1
                elif a[i - 1] in set2 and b[j - 1] in set2:
                    cost = 1
                elif a[i - 1] in set1 and b[j - 1] in set2:
                    cost = 2
                elif a[i - 1] in set2 and b[j - 1] in set1:
                    cost = 2
                else:
                    cost = 3

                dp[i][j] = min(dp[i - 1][j - 1] + cost,
                               dp[i - 1][j] + 3,
                               dp[i][j - 1] + 3)

    print(dp[m][n])

if __name__ == "__main__":
    func()
