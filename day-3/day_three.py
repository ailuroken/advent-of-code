import re

rows = []

with open("day-3/puzzle_input.txt", 'r') as file:
    for line in file:
        rows.append(line)

def part_one():
    answer = 0
    
    for line in rows:
        x = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
        for mul in x:
            nums = re.findall("[0-9]+", mul)
            nums = [int(y) for y in nums]
            answer += (nums[0] * nums[1])
    
    return answer

def part_two():
    answer = 0
    enabled = True
    
    for line in rows:
        x = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", line)
        for elem in x:
            if elem == "do()":
                enabled = True
            elif elem == "don't()":
                enabled = False
            elif enabled:
                nums = re.findall("[0-9]+", elem)
                nums = [int(y) for y in nums]
                answer += (nums[0] * nums[1])
    
    return answer

print(part_one())
print(part_two())