# Given an array of integers, return a new array such that 
# each element at index i of the new array is the product 
# of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output
# would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
# the expected output would be [2, 3, 6].


def productOfNum(arr, arr_len):
    
    if arr_len == 0:
        return 0
    
    i = 1
    temp = 1
    
    product = [1 for i in range(arr_len)]
    
    # Product from the left side of the array.    
    for i in range(arr_len):
        product[i] = temp
        temp = temp * arr[i] 
    
    temp = 1 # As the above temp values already contains values.
    
    # Product from the right side of the array        
    for i in range(arr_len-1, -1, -1):
        product[i] = product[i]*temp  #Multiplying with the above array values.
        temp = temp * arr[i] 
        
    for i in range(arr_len):
        print(product[i], end=" ")
        
arr = []
num = int(input("Enter number of elements in array: "))

for i in range(0,num):
    element = int(input("Enter a value: "))
    
    #Adds the element to the array.
    arr.append(element)  
print(arr)

print("The product: ")
productOfNum(arr, len(arr))
