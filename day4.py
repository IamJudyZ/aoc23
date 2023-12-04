with open('day4.txt', 'r') as file:
   lines = file.readlines()

sum = 0
index = 0
copies = [1]*219

for line in lines:
    round = line.split(":")[1].split("|")
    winners = round[0].replace("  ", " ").strip().split(" ")
    mine = round[1].replace("  ", " ").strip().split(" ")
    hit = 1
    for num in mine:
        if num in winners:
            copies[index+hit]+=copies[index]
            hit+=1
    index+=1

for i in copies:
    sum+=i
print(copies)
print(sum)