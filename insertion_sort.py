'''
This Program performs insertion sort in very simple way by shifting and comparing the values of array/list

'''
input_string = input("Enter numbers separated by commas: ")
input_list = input_string.split(',')
arr = [int(num) for num in input_list]
print("Original array:", arr)
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print("Sorted array:", arr)
print("The Time Complexity of insertion sort is O(n2)")
