
#part 1
with open('c:/Users/kellertsen/Downloads/AdventOfCode2021/puzzle3.txt') as diagnostics:
    lines = diagnostics.readlines()
    gammaList = [0] * 12
    for bin in lines:
        for i in range(len(bin)-1):
            gammaList[i] += int(bin[i])
    half = len(lines)/2
    gamma, epsilon = "", ""
    for i in range(len(gammaList)):
        if(gammaList[i] > half):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(int(gamma, 2)*int(epsilon, 2))
    
#part 2
def oxygenRating(binList, currentBit, type):
    if(len(binList) == 1):    
        return binList[0]   

    ones, zeroes = [], []
    for bin in binList:
        if(bin[currentBit] == "1"):
            ones.append(bin)
        else:
            zeroes.append(bin)

    if(type == "oxygen"): 
        return oxygenRating(ones, currentBit+1, type) if len(ones) >= len(zeroes) else oxygenRating(zeroes, currentBit+1, type)
    else:
        return oxygenRating(zeroes, currentBit+1, type) if len(zeroes) <= len(ones) else oxygenRating(ones, currentBit+1, type)

with open('c:/Users/kellertsen/Downloads/AdventOfCode2021/puzzle3.txt') as diagnostics:
    lines = diagnostics.readlines()
    oxyRating = oxygenRating(lines, 0, "oxygen")
    co2Rating = oxygenRating(lines, 0, "co2")
    print(int(oxyRating, 2)*int(co2Rating, 2))