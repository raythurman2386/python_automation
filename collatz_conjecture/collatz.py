from typing import List

def collatz(n: int) -> List[int]:
    # Ensure the number is a positive whole number
    if type(n) is not int:
        raise TypeError(f'Please input a valid positive whole number! Your input was: {n}')
    
    if n <= 0:
        raise ValueError(f'Please input a value greater than 0! Your input was: {n}.')
    
    
    # Keep a list of the numbers calculated
    sequence = [n]
    
    # Till the number reaches 1
    while n != 1:
        # If the number even, divide by two
        if n % 2 == 0:
            n = n // 2
        else:
        # If the number is odd, multiply by 3 and add 1
            n = 3 * n + 1
            
        # Add the number to the list
        sequence.append(n)
        
    # return the final list
    return sequence

# print(collatz(391))
print(collatz(3919377))