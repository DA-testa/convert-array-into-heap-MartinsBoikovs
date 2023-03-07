# python3
import math

def build_heap(data):
    swaps = []
    n = len(data)

    while n != 0:
        (data[int(math.floor((n-1)/2))], data[n-1]) = (data[n-1], data[int(math.floor((n-1)/2))])

        swaps.append((int(math.floor((n-1)/2)), n))

        n1 = n

        while 2*n1 + 1 < len(data): #WHICH N1 SHOULD BE???????
            if data[n1] > data[2*n1]:
                (data[2*n1], data[n1]) = (data[n1], data[2*n1]) 
                


                
                swaps.append((n1, 2*n1))
                
                n1 = 2*n1
        
        n = int(math.floor((n-1)/2)) 
 



    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    text = input()
    if 'F' in text in text:
        file_name = input()
        file = "./test/" + file_name
        with open(file) as f:
            т = int(f.readline())
            data = list(map(int, f.readline().split()))
    if 'I' in text:
        n = int(input())
        data = list(map(int, input().split()))


    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
