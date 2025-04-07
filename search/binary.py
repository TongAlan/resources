# Python implementation of binary search
import math

def binary_search_iterative(haystack: list, needle: int) -> bool:
    lo = 0
    hi = len(haystack)
    count = 0

    while lo < hi:
        count += 1
        m = math.floor(math.floor(lo + (hi - lo) / 2))
        v = haystack[m]
        if v == needle:
            return True
        elif v > needle:
            hi = m
        else:
            lo = m + 1
    return False

def binary_search_recursive(haystack: list, lo: int, hi: int, needle: int) -> bool:
    if hi >= lo:
        m = math.floor(lo + (hi - lo) / 2)
        v = haystack[m]
        if needle == v:
            return True
        elif needle > v:
            return binary_search_recursive(haystack, m+1, hi, needle)
        else:
            return binary_search_recursive(haystack, lo, m-1, needle)
    else: 
        return False


def main():
    some_haystack = [i for i in range(100)] # search space
    some_needle = 50 # search value

    # output = binary_search_iterative(some_haystack, some_needle) # bool return to output
    # output = binary_search_recursive(some_haystack, 0, len(some_haystack), some_needle)

main()
    
    


    
        
    