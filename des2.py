#part 1
with open('c:/Users/kellertsen/Downloads/AdventOfCode2021/puzzle2.txt') as movements:
    lines = movements.readlines()

    course = {
        "forward": 0,
        "up": 0,
        "down": 0
    }
    
    for line in lines:
        course[line.split(" ")[0]] += int(line.split(" ")[1])
    total = (course["down"]-course["up"])*course["forward"]
    print("Depth part1: ", total)

#part 2
with open('c:/Users/kellertsen/Downloads/AdventOfCode2021/puzzle2.txt') as movements:
    lines = movements.readlines()

    course = {
        "forward": 0,
        "depth": 0,
        "aim": 0
    }

    for line in lines:
        course["forward"] += int(line.split(" ")[1]) if line.split(" ")[0] == "forward" else 0
        course["aim"] += int(line.split(" ")[1]) if line.split(" ")[0] == "down" else -abs(int(line.split(" ")[1])) if line.split(" ")[0] == "up" else 0
        course["depth"] += int(line.split(" ")[1])*course["aim"] if line.split(" ")[0] == "forward" else 0
    total = course["depth"]*course["forward"]
    print("Depth part2: ", total)
   
