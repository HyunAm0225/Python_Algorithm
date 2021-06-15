from collections import deque
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]


def solution(skill, skill_trees):
    answer = 0
    skill_dict = {}
    for index, item in enumerate(skill):
        skill_dict[item] = index
    print(skill_dict)
    skill_tree_length = len(skill_trees)
    skill_trees = deque(skill_trees)
    fail = []
    while skill_trees:
        skill_count = 0
        skill_data = skill_trees.popleft()
        for data in list(skill_data):
            if data in skill_dict:
                if skill_count != skill_dict[data]:
                    fail.append(skill_data)
                    break
                else:
                    skill_count += 1
        print(fail)
    return skill_tree_length-len(fail)


print(solution(skill, skill_trees))
