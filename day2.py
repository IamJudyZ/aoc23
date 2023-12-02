with open('day2.txt', 'r') as file:
   lines = file.readlines()

sum = 0

for line in lines:
    maxBlue = 0
    maxRed = 0
    maxGreen = 0
    round = line.split(":")[1].split(";")
    for i in round:
        balls = i.split(",")
        for b in balls:
            b = b.strip().split(" ")
            if (b[1] == "blue") & (int(b[0]) > maxBlue):
                maxBlue = int(b[0])
            elif (b[1] == "red") & (int(b[0]) > maxRed):
                maxRed = int(b[0])
            elif (b[1] == "green") & (int(b[0]) > maxGreen):
                maxGreen = int(b[0])
    total = maxBlue*maxRed*maxGreen
    sum+=total
print(sum)

# pt1
# sum = 0
# counter = 0

# for line in lines:
#     addLine = True
#     counter+=1
#     round = line.split(":")[1].split(";")
#     for i in round:
#         for b in i.split(","):
#             b = b.strip().split(" ")
#             if ((b[1] == "blue") & (int(b[0]) > 14)) | ((b[1] == "red") & (int(b[0]) > 12)) | ((b[1] == "green") & (int(b[0]) > 13)):
#                 addLine = False
#     if addLine:
#         sum += counter
# print(sum)

# correct answers:
# judyzhan-mn1:aoc23 judyzhan$ /opt/homebrew/bin/python3.11 /Users/judyzhan/Desktop/aoc23/day2.py
# 2149
# judyzhan-mn1:aoc23 judyzhan$ /opt/homebrew/bin/python3.11 /Users/judyzhan/Desktop/aoc23/day2.py
# 71274