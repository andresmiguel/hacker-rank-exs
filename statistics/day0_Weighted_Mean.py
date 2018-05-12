n = input()
numbers = []
weights = []

line = input()
numbers = list(map(lambda x: int(x), line.split(" ")))

line = input()
weights = list(map(lambda x: int(x), line.split(" ")))

weightAndNumberSum = 0
weightSum = sum(weights)

for idx, number in enumerate(numbers):
    weightAndNumberSum += number * weights[idx]

print(weightAndNumberSum / weightSum)
