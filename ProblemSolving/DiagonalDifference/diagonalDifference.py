from sys import stdin


def main():
    x = int(stdin.readline())
    temp = []
    sum1 = 0
    sum2 = 0
    for i in range(x):
        y = [int(x) for x in stdin.readline().split()]
        temp.append(y)
    for i in range(len(temp)):
        sum1 += temp[i][i]
        sum2 += temp[i][(len(temp)-1)-i]
    total = sum1-sum2
    if total < 0:
        total *= -1
    print(total)


main()
