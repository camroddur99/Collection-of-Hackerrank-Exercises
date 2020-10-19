from sys import stdin

def main():
    x = int(stdin.readline())
    arr = [int(y) for y in stdin.readline().split()]
    sum = 0
    for i in range(x):
        sum += arr[i]
    print(sum)
main()
