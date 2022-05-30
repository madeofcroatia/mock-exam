"""
Enter your full name here:

Gulyamov Sardor

Enter your ID here:

21SE000
"""


def rotate_right_by_1(array):
    """
    Return how the given 'array' would look like if all of
    its values were rotated right by 1!

    Input:
        array (list) - a list of integers

    Return:
        new_array, which is just array cyclically rotated right by 1 element

    Example: if array = [1, 2, 3, 4, 5], then you should return [5, 1, 2, 3, 4]

    YOU SHOULD NOT CHANGE ANYTHING IN 'array', BUT INSTEAD
    DO ALL THE WORK ON 'new_array' AND RETURN IT
    """
    new_array = array[:]
    temp = new_array[0]
    for i in range(1, len(new_array)):
        temp, new_array[i] = new_array[i], temp

    new_array[0] = temp
    return new_array


def rotate_right_by_k(array, k):
    """
    Return how the given 'array' would look like if it was
    cyclically rotated by k elements to the right.

    You MUST use rotate_right_by_1

    Input:
        array (list) - a list of integers
        k (integer) - a non-negative integer

    Return:
        new_array, which should be array cyclically rotated right by k elements

    Note that if k is 1, then your porgram should return the same thing as
    rotate_right_by_1.

    Examples:
        Inputs: array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 1
        Return: new_array = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        Inputs: array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 4
        Return: new_array = [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]
    """
    new_array = array[:]
    for _ in range(k):
        new_array = rotate_right_by_1(new_array)
    return new_array


def rotate_by_k(array, k):
    """
    Same as the previous function, but here if k < 0 you need
    to cyclically rotate array left by |k|

    For example, if k = -3, you need to return what the array
    would look like if you rotated it left by 3

    For example: array = [5, 1, 12, 3, 144, 4], k = -1
                 returns new_array = [1, 12, 3, 144, 4, 5]

                 array = [12, 333, 12, 44, 9], k = -3
                 returns new_array = [44, 9, 12, 333, 12]
    """
    new_array = array[:]
    if k > 0:
        return rotate_right_by_k(new_array, k)
    else:
        return list(reversed(rotate_right_by_k(list(reversed(new_array)), -k)))

