# import sys
import re
# orig_stdout = sys.stdout
# f = open('out.txt', 'w')
# sys.stdout = f

numDict = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
}

# creds to bdoan for the idea of findall instead of replace, which fixed my issue with joined words such as twone
pattern = r"(\d|one|two|three|four|five|six|seven|eight|nine)"

with open('day1.txt', 'r') as file:
   lines = file.readlines()

sum = 0

for line in lines:
   s = line
   allnums = re.findall(pattern, line)
   first = allnums[0]
   second = allnums[-1]
   for word, number in numDict.items():
      first = first.replace(word, number)
      second = second.replace(word, number)
   sum+=(int(first)*10) + int(second)

print(sum)

# sys.stdout = orig_stdout
# f.close()
