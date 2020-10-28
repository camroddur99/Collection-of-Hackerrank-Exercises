from sys import stdin

def main():
    n = int(stdin.readline())
    sum = 1
    sumto = 0
    iter = 0 
    arr = [int(y) for y in stdin.readline().split()]
    arr2 = []
    arr.sort()
    while len(arr) > 0:
        if len(arr) > 1:
            if arr[iter] == arr[iter+1]:
                sum += 1
                arr.pop(iter+1)
            else:
                arr.pop(iter)
                arr2.append(sum)
                sum = 1
        else:
            arr.pop(iter)
            arr2.append(sum)
            sum = 1
    for i in range(len(arr2)):
        sumto += arr2[i] // 2
    print(sumto)
main()
