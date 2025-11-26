filename = input(" Enter the file name: ")
filehand = open(filename)
count = 0 
total = 0
for line in filehand:
    line = line.strip()
    if not line.startswith("X-DSPAM-Confidence"):
        continue
    colon_pos = line.find(':')
    num_str = line[colon_pos + 1:]
    num = float(num_str)
    total += num
    count += 1
average = total / count
print("Average spam confidence:", average)