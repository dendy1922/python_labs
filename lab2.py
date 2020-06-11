import numpy as np

#creating array from 0 to 8 with 3 col and 3 row
my_array = np.arange(9).reshape(3, 3)

#first way,function to sum negative elements
def sum_negative_first(my_array):
    a = my_array.ravel()
    result = sum([item for item in a if item < 0])
    return result

#second way,function to sum negative elements
def sum_negative_second(my_array):
    a = my_array.ravel()
    z=a<0
    return a.sum(where = z)


#function to count zero elements
def count_zero_el(my_array):
    a = my_array.ravel()
    result = len([item for item in a if item == 0])
    return result

#function to swap columns
def swap_cols(my_array, frm, to):
    arr = np.copy(my_array)
    arr[:, [frm, to]] = arr[:, [to, frm]]
    return arr

#function to sum of two first rows
def sum_two_rows(my_array):
    b = my_array[:2, :]
    return np.array([b.sum()], int)


if __name__ == "__main__":
    #creating array from 0 to 8 with 3 col and 3 row
    my_array = np.arange(9).reshape(3, 3)
    #find negative sum
    print(sum_negative_first(my_array))
    print()
    #executing second way
    print(sum_negative_second(my_array))
    print()
    #counting zero elements
    print(count_zero_el(my_array))
    print()
    #swap in array first and second column
    print(swap_cols(my_array, 0, 1))
    print()
    #sum two first rows and displaying in array
    print(sum_two_rows(my_array))
    print()
