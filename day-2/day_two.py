rows = []

with open("day-2/puzzle_input.txt", 'r') as file:
    for line in file:
        numbers = [int(e) for e in line.split()]
        rows.append(numbers)

def check_safety(line):
    check = -1
    
    asc = False
    des = False
    
    for i in range(len(line) - 1):
        a = line[i]
        b = line[i + 1]
        
        if a < b:
            asc = True
        elif a > b:
            des = True
        else:
            asc = True
            des = True
        
        if asc and des:
            check = i
            break
        
        if abs(a - b) > 3:
            check = i
            break
        
    return check

def part_one():
    count = 0
    
    for line in rows:
        if check_safety(line) == -1:
            count += 1
    
    return count

def part_two():
    count = 0
    
    for line in rows:
        
        index = check_safety(line)
        
        if index == -1:
            count += 1
        else:
            
            testOne = line.copy()
            testTwo = line.copy()
            
            testOne.pop(index)
            testTwo.pop(index + 1)
            
            if check_safety(testOne) == -1 or check_safety(testTwo) == -1:
                count += 1
            elif index > 0:
                testThree = line.copy()
                testThree.pop(index - 1)
                
                if check_safety(testThree) == -1:
                    count += 1
                
    return count


print(part_one())
print(part_two())