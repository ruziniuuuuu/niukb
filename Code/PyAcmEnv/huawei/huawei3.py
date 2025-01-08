# Brute Force
def func():
    num_hunters, num_animals = map(int, input().split())
    hunter_skills = input().split()
    animal_weaks = input().split()

    for i, weaks in enumerate(animal_weaks):
        weaks = set(weaks)
        animal_weaks[i] = weaks


    # condition 2
    set_condition2 = set('ABCDEF')
    condition2 = [False] * num_hunters
    for i, skills in enumerate(hunter_skills):
        for skill in skills:
            if skill in set_condition2:
                condition2[i] = True
                break


    results = []
    for i, skills in enumerate(hunter_skills):
        result = 0
        # check condition 2
        if condition2[i] == True:
            final_skill = skills[-1]
            condition3 = False
            skills_set = set(skills)
            for weaks in animal_weaks:
                # check condition 3
                if final_skill in weaks:
                    # check condition 1
                    flag = 1
                    for weak in weaks:
                        if weak not in skills_set:
                            flag = 0
                            break
                    # satisfy all 3 conditions
                    if flag == 1:
                        result += 1

        results.append(result)

    print(' '.join(str(result) for result in results))



if __name__ == "__main__":
    func()
