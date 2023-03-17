# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n// 2 -1, -1, -1):
      k=i
      while True:
        b=k
        left=2*k+1
        right=2*k+2
 
    if left < n and data[left] > data[b]:
        b= left
    if right < n and data[right] > data[b]:
        b= right
    if b!= k:
        swaps.append(k, b)
        data[k], data[b]= data[b], data[k]
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    return swaps    
def main():
    inp_type=input()
    # TODO : add input and corresponding checks
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file
    if 'I' in inp_type:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
        
    elif 'F' in inp_type:
        fn= input()
        with open(f"tests/{fn}") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    
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
