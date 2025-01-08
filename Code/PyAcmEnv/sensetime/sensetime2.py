def func(monsters):
    n = len(monsters)

    diff = [0] * n

    def rule(monster):
        if monster[1] > monster[0]:
            return [True, -monster[0]]
        else:
            return [False, monster[1]]

    monsters.sort(
        key=rule
    )

    now = 0
    result = 0
    for monster in monsters:
        if now >= monster[0]:
            now = now - monster[0] + monster[1]
        else:
            result += monster[0] - now
            now = monster[1]
    
    return result

if __name__ == "__main__":
    monsters = [[1, 2], [3, 4]]    
    func(monsters)