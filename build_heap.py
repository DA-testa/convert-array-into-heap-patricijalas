# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n// 2 -1, -1, -1):
   
      while True:
        tn=i
        l=2*i+1
        r=2*i+2
 
        if l< n and data[l]< data[tn]:
          tn= l
        if r< n and data[r]< data[tn]:
          tn= r
        if i!= tn:
          swaps.append((i, tn))
          data[i], data[tn]= data[tn], data[i]
          i=tn

        else:
          break
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
