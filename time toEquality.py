def time_equality(array):
    maximum = float('-inf')
    result = 0
    for i in range(len(array)):
        if array[i] > maximum:
            maximum = array[i]
    for i in range(len(array)):
        result += maximum - array[i]
    return result

size = int(input())
array = list(map(int, input().split()))
print(time_equality(array))
