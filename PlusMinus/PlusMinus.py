from sys import stdin

def main():
    x = int(stdin.readline())
    arr = [int(y) for y in stdin.readline().split()]
    pos, neg, zer = 0,0,0
    for i in range(x):
        if arr[i] < 0:
            neg += 1
        elif arr[i] > 0:
            pos += 1
        else:
            zer += 1
    print('{:.6f}'.format(pos/x))
    print('{:.6f}'.format(neg/x))
    print('{:.6f}'.format(zer/x))
main()
