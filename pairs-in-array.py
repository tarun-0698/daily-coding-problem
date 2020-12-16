# Given a list of numbers and a number k, 
# return whether any two numbers from the 
# list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, 
# return true since 10 + 7 is 17.


def sumOfTwoNum(arr, arr_len, sum):

    #Empty set
    s= set()

    for i in range(0,arr_len):          # Time complexity is O(n) as it need to search every element in the array
        
        # Temp contains the elements after sub from the arr.
        temp = sum - arr[i]
        #print(temp)
        
        if (temp in s):
            print ("True since "+ str(arr[i]) +" + "+ str(temp) + " is " + str(sum))
        s.add(arr[i])
        
                    
arr = []
num = int(input("Enter number of elements in array: "))

for i in range(0,num):
    element = int(input("Enter a value: "))
    
    #Adds the element to the list.
    arr.append(element)  
print(arr)

numberToFind = int(input("Enter a number: "))
sumOfTwoNum(arr, len(arr), numberToFind)

