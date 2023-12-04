"""
method used:
replace all "."s with xs so special characters can be searched using not isalnum
find each number, then find the start and end index of the line
look left, right, line above, line under
manually added the last line to save time
"""

with open('day3.txt', 'r') as file:
   lines = file.readlines()

sum = 0
allRows = []

for line in lines:
    allRows.append(line.strip().replace(".", "x"))

for i in range(len(allRows)-1):
# for i in range(2):
    line = allRows[i]
    maxIndex = -1
    for j in range(len(line)-2):
        if j > maxIndex:
            if line[j].isdigit() & line[j+1].isdigit() & line[j+2].isdigit():
                num = line[j:j+3]
                maxIndex = j+2
            elif line[j].isdigit() & line[j+1].isdigit():
                num = line[j:j+2]
                maxIndex = j+1
            elif line[j].isdigit():
                num = line[j]
                maxIndex = j
            # check if there is symbol around it
            if maxIndex >= j:
                nextLine = allRows[i+1]
                if (j-1>0 and (not line[j-1].isalnum())) | (maxIndex+1<len(line) and (not line[maxIndex+1].isalnum())):
                    sum += int(num)
                    # print("if", num)
                else:
                    if i == 0:
                        index = j-1
                        while index < maxIndex+2:
                            if (not nextLine[index].isalnum()):
                                sum += int(num)
                                # print("index:", index, "else", num)
                                break
                            index+=1
                    else:
                        prevLine = allRows[i-1]
                        if j-1 <= 0:
                            index = 0
                        else:
                            index = j-1
                        if maxIndex+1 > len(line)-1:
                            maxIndex = maxIndex-1
                        while index < maxIndex+2:
                            if (not nextLine[index].isalnum()) | (not prevLine[index].isalnum()):
                                sum += int(num)
                                # print("index:", index, "else", num)
                                break
                            index+=1

# manually added the last line to the sum
print(sum)
