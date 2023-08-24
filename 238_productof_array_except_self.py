def productExceptSelf_(nums):
    """
    Calculate the product of all numbers except the current one for each position in the input list.

    Args:
    - nums (List[int]): A list of integers.

    Returns:
    - List[int]: A list where each element at index 'i' is the product of all numbers in 'nums' except nums[i].

    Example:
    >>> productExceptSelf_([1, 2, 3, 4])
    [24, 12, 8, 6]
    """
    
    # Initialize the length of the input list and the result list with 1s.
    n = len(nums)
    result = [1]*n
    
    # Compute the prefix product for each position.
    prefix = 1
    for i, num in enumerate(nums):
        # Multiply the current position in the result by the prefix product.
        result[i] *= prefix
        # Update the prefix product.
        prefix *= num

    # Compute the postfix (or suffix) product for each position.
    postfix = 1
    for j in range(n-1, -1, -1):
        # Multiply the current position in the result by the postfix product.
        result[j] *= postfix 
        # Update the postfix product.
        postfix *= nums[j]

    # Return the result list.
    return result
