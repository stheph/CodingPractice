import MinHeap as MH
import numpy as np

def test_create_new_heap():
    test = MH.MinHeap()
    # Backing array should be equivalent to an empty array of size HEAP_SIZE
    assert all(map(lambda x: x[0] == x[1], (zip(test.as_array, np.zeros((MH.HEAP_SIZE))))))

def test_insert_one_element_into_empty_heap():
    test = MH.MinHeap()
    test.insert(1)

    test_against_array = np.zeros((MH.HEAP_SIZE))
    test_against_array[0] = 1

    assert all(map(lambda x: x[0] == x[1], (zip(test.as_array, test_against_array))))

def test_insert_multiple_elements_into_empty_heap():
    test = MH.MinHeap()
    test.insert(10)
    # 10 is root
    test.insert(5)
    # Add 5 to left child, 5 and 10 swap
    test.insert(7)
    # Add 7 as right child
    test.insert(1)
    # Add 1 as left-left child, swaps with 10, then 5.

    # Final Tree:
    #       1
    #      / \
    #     5   7
    #    /
    #  10
    # [1,5,7,10]

    test_against_array = np.zeros((MH.HEAP_SIZE))
    test_against_array[0] = 1
    test_against_array[1] = 5
    test_against_array[2] = 7
    test_against_array[3] = 10

    assert all(map(lambda x: x[0] == x[1], (zip(test.as_array, test_against_array))))

if __name__ == "__main__":
    test_create_new_heap()
    print ("test_create_new_heap passed!")

    test_insert_one_element_into_empty_heap()
    print ("test_insert_one_element_into_empty_heap passed!")

    test_insert_multiple_elements_into_empty_heap()
    print ("test_insert_multiple_elements_into_empty_heap passed!")