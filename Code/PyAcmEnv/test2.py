# x^5+x+1=0

def func():
    left = -1
    right = 0

    d = 1e-5

    f = 1
    mid = 0
    while abs(f) >= d:
        mid = (left + right) / 2
        f = mid**5 + mid + 1
        if f < 0:
            left = mid
        else:
            right = mid

    return f, mid

if __name__ == "__main__":
    print(func())
