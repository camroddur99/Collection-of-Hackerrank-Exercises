from sys import stdin

def main():
    x1 = [int(x) for x in stdin.readline().split()]
    y1 = [int(x) for x in stdin.readline().split()]
    cont1 = 0
    cont2 = 0
    for i in range(len(x1)):
        if x1[i] > y1[i]:
            cont1 += 1
        elif x1[i] < y1[i]:
            cont2 += 1
    print(cont1,cont2)
main()
