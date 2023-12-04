"""
method used:
locate stars, then look before and after it
then search char directly above and under
if char above/under is digit, then no need to check char left up/down and char right up/down
if above/under is not digit, then check top/bottom left and right
gather all the valid numbers for the *, multiply them if there's exactly 2
"""

with open('day3.txt', 'r') as file:
   lines = file.readlines()

sum = 0
allRows = []

for line in lines:
    allRows.append(line.strip())

for i in range(len(allRows)-1):
    line = allRows[i]
    for j in range(len(line)):
        if line[j] == "*":
            ratio = 0

            num1 = "0"
            # num before a star
            if (line[j-1].isdigit()):
                countBef = 1
                while j-countBef>=0 and line[j-countBef].isdigit():
                    num1=num1[:1]+line[j-countBef]+num1[1:]
                    countBef+=1

            # num after a star
            charCount2 = 1
            num2="0"
            while j+charCount2<len(line) and line[j+charCount2].isdigit():
                num2+=line[j+charCount2]
                charCount2+=1

            # check line before
            prevLine = allRows[i-1]
            num3="0"
            if (prevLine[j].isdigit()):
                count1 = 1
                while j-count1>=0 and prevLine[j-count1].isdigit():
                    num3=num3[:1]+prevLine[j-count1]+num3[1:]
                    count1+=1
                count2 = 0
                while j+count2<len(prevLine) and prevLine[j+count2].isdigit():
                    num3+=prevLine[j+count2]
                    count2+=1
            elif (prevLine[j-1].isdigit()):
                count1a = 1
                while j-count1a>=0 and prevLine[j-count1a].isdigit():
                    num3=num3[:1]+prevLine[j-count1a]+num3[1:]
                    count1a+=1
            num3a="0"
            if (not prevLine[j].isdigit() and prevLine[j+1].isdigit()):
                count2a = 1
                while j+count2a<len(prevLine) and prevLine[j+count2a].isdigit():
                    num3a+=prevLine[j+count2a]
                    count2a+=1

            # check line after
            nextLine = allRows[i+1]
            num4="0"
            if (nextLine[j].isdigit()):
                count4 = 1
                while j-count4>=0 and nextLine[j-count4].isdigit():
                    num4=num4[:1]+nextLine[j-count4]+num4[1:]
                    count4+=1
                count5 = 0
                while j+count5<len(nextLine) and nextLine[j+count5].isdigit():
                    num4+=nextLine[j+count5]
                    count5+=1
            elif (nextLine[j-1].isdigit()):
                count4a = 1
                while j-count4a>=0 and nextLine[j-count4a].isdigit():
                    num4=num4[:1]+nextLine[j-count4a]+num4[1:]
                    count4a+=1
            num4a="0"
            if (not nextLine[j].isdigit() and (nextLine[j+1].isdigit())):
                count5a=1
                while j+count5a<len(nextLine) and nextLine[j+count5a].isdigit():
                    num4a+=nextLine[j+count5a]
                    count5a+=1

            multi = []
            if int(num1)>0:
                multi.append(int(num1))
            if int(num2)>0:
                multi.append(int(num2))
            if int(num3)>0:
                multi.append(int(num3))
            if int(num3a)>0:
                multi.append(int(num3a))
            if int(num4)>0:
                multi.append(int(num4))
            if int(num4a)>0:
                multi.append(int(num4a))

            if (len(multi)==2):
                ratio = multi[0]*multi[1]
            sum+=ratio
            
print(sum)