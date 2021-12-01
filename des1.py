#part 1
with open('c:/Users/kellertsen/Downloads/AdventOfCode2021/puzzle1.txt') as measurements:
    lines = measurements.readlines()
    
    current = int(lines[0])
    increases = 0
    for line in lines:
        if(int(line) > current):
            increases += 1
        current = int(line)
        
    print(increases)

#part 2


def slidingWindow(list, n, windowSize):
    sums = []
    for i in range(n - windowSize + 1):
        currentWindow = list[i:i+windowSize]
        sum = 0
        for x in currentWindow:
            sum += int(x)
        sums.append(sum)
    return sums

with open('c:/Users/kellertsen/Downloads/AdventOfCode2021/puzzle1.txt') as measurements:
    lines = measurements.readlines()
    sums = slidingWindow(lines, len(lines), 3)
    increases = 0
    for i in range(0, len(sums)-1, 1):
        if(sums[i] < sums[i+1]):
            increases += 1
    print(increases)