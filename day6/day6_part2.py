class LanternFish:
    def __init__(self, days, count):
        self.days = days
        self.count = count

inputFile = open("day6/input.txt", "r")

lanternFish = [LanternFish(0, 0), LanternFish(1, 0), LanternFish(2, 0), LanternFish(3, 0), LanternFish(4, 0), LanternFish(5, 0), LanternFish(6, 0)]
sum = 0

for line in inputFile:
    allLanternfish = [int(fish) for fish in line.strip().split(",")]
    sum = len(allLanternfish)

    for fish in allLanternfish:
        for fishGroup in lanternFish:
            if fishGroup.days == fish:
                fishGroup.count += 1

# print(lanternFish)

babyFish = []

for x in range(256):
    for matured in babyFish:
        matured.days -= 1
        if matured.days <= 6:
            for adultGroup in lanternFish:
                if adultGroup.days == matured.days:
                    adultGroup.count += matured.count
            babyFish.remove(matured)
    for i in range(len(lanternFish)):
        lanternFish[i].days -= 1
        if lanternFish[i].days < 0:
            babyFish.append(LanternFish(8, lanternFish[i].count))
            lanternFish[i].days = 6
            sum += lanternFish[i].count

print(sum)
