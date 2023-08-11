n = int(input())
numbers = list(map(int, input().split()))
sumOfNumber = 0
for number in numbers:
    if number%2==0:
        sumOfNumber += 1
print(sumOfNumber)

