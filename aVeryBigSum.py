from sys import stdin

def main():
    x = int(stdin.readline())
    arr = [int(y) for y in stdin.readline().split()]
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    print(sum)
main()
