from collections import Counter

n = input()
numbers = []

line = input()
numbers = list(map(lambda x: int(x), line.split(" ")))
numbers.sort()

total = sum(numbers)
count = len(numbers)

mean = total / count
median = 0
mode = Counter(numbers).most_common()[0][0]

middle = count // 2

if count % 2 == 0:
    median = (numbers[middle - 1] + numbers[middle]) / 2
else:
    median = numbers[middle]

print(mean)
print(median)
print(mode)


