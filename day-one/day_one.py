from puzzle_input import left_list, right_list

def part_one():
    answer = 0

    left_list.sort()
    right_list.sort()
    
    for i in range(len(left_list)):
        answer += abs(left_list[i] - right_list[i])

    return answer

print(part_one())