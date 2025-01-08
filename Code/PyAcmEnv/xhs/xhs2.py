def func(n, x, collections):
    best_pair = None
    
    for i in range(n):
        s_i = collections[i][1:]
        for j in range(i + 1, n):
            s_j = collections[j][1:]
            s_ij = s_i + s_j
            mcn_ij = len(set(s_ij))
            if mcn_ij == x:
                if best_pair is None or (i < best_pair[0] or (i == best_pair[1] and j < best_pair[1])):
                    best_pair = (i, j)
    if best_pair:
        print("YES")
        print(best_pair[0] + 1, best_pair[1] + 1)
    else:
        print("NO")

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, x = map(int, input().split())
        collections = []
        for _ in range(n):
            user_info = list(map(str, input().split()))
            collections.append(user_info)
        func(n, x, collections)