#!/usr/bin/env python3

def print_fibonacci(length):
    # Check if the requested length is less than or equal to 0
    if length <= 0:
        print([])
        return
    
    #Initailize a list of the specified length with all the elements set to o
    fibonacci_sequence = [0] * length
    # if the length is greater than 1 , set the second element to 1
    if length > 1 :
        fibonacci_sequence[1] = 1

        #Calculate each fibonacci number from the third element onwards 
        for i in range(2, length):
            #Each element is the sum of the two preceding elements 
            fibonacci_sequence[i] = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
#return the list containing the sequence 
    print(fibonacci_sequence) 

print(print_fibonacci(9))