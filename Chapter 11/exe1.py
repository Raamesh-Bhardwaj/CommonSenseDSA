from typing import List


def count_characters(array: List[str]):
    """_summary_
    Exercise Question 1
    Use Recursion to write a function that accepts an Array of string
    and returns the total number of characters across all strings.
    Example 1:  ['ab', 'c', 'def', 'ghij'] return 10
    """
    # base case - TODO
    if len(array) == 0:
        return 0
    # check 1 - use set 
    count = len(array[0]) + count_characters(array[1:])
    return count
    
    
def main():
    test_input = ['ab', 'cd', 'def', 'ghij']
    count = count_characters(test_input)
    print(f'Total Count is {count}')


if __name__ == '__main__':
    main()
