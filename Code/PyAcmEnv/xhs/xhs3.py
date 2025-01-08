def calc_tot_dist(n, m, a, j):
    tot_dist = 0
    for a_i in a:
        tot_dist += min(abs(j - a_i), abs(a_i + n - j))
    return tot_dist


def func(n, m, a):
    a.sort()

    min_tot_dist = float('inf')
    optimal_position = 0

    for j in range(1, n + 1):
        tot_dist = calc_tot_dist(n, m, a, j)
        if tot_dist < min_tot_dist:
            min_tot_dist = tot_dist
            optimal_position = j
    
    return optimal_position

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(func(n, m, a))
    