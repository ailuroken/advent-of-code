from puzzle_input import left_list, right_list

def part_one():
    answer = 0

    left_list.sort()
    right_list.sort()
    
    for i in range(len(left_list)):
        answer += abs(left_list[i] - right_list[i])

    return answer

def part_two():
    answer = 0
    right_dict = dict()

    for elem in right_list:
        if elem in right_dict:
            right_dict[elem] += 1
        else:
            right_dict[elem] = 1

    for elem in left_list:
        if elem in right_dict:
            answer += elem * right_dict[elem]

    return answer

print(part_one())
print(part_two())