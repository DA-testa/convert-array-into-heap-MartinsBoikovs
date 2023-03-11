# python3
import math

def build_heap(data):
    swaps = []

    for i in reversed(data):
        n = data.index(i)

        while n != 0:
            if data[n] < data[int(math.floor((n-1)/2))]:
                data[n],data[int(math.floor((n-1)/2))]=data[int(math.floor((n-1)/2))],data[n]
                swaps.append((int(math.floor((n-1)/2)), n))

            n = int(math.floor((n-1)/2)) 

    return swaps


def main():
    text = input()
    if 'F' in text in text:
        file_name = input()
        file = "./test/" + file_name
        with open(file) as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    if 'I' in text:
        n = int(input())
        data = list(map(int, input().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
