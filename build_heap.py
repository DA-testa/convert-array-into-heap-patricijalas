# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n// 2 -1, -1, -1):
        heap(data, i, n)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps

def heap_sort(data):
    build_heap(data)
    for i in range(len(data) -1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heap_size = i
        heap(data, 0, heap_size)
    data.reverse()

def heap(data, i, heap_size):
    b=i
    left=2*i+1
    right=2*i+2
 
    if left < heap_size and data[left] > data[b]:
        b = left
    if right < heap_size and data[right] > data[b]:
        b = right
    if b != i:
        data[i], data[b] = data[b], data[i]
        heap(data, b, heap_size)
def main():
    input_type = input()
    # TODO : add input and corresponding checks
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file

    if 'I' in input_type:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
        
        
    elif 'F' in input_type:
        filename = input()
        with open("test/" + filename, 'r') as f:
            n = int(f.readline())
            data = list(map(int, input().split()))
    else:
        exit()
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
