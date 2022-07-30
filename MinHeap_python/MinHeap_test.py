import MinHeap as MH
import numpy as np

def test_create_new_heap():
    test = MH.MinHeap()
    # Backing array should be equivalent to an empty array of size HEAP_SIZE
    assert all(map(lambda x: x[0] == x[1], list(zip(test.as_array(), np.zeros((test.get_max_size()))))[:test.get_heap_size()]))

def test_insert_one_element_into_empty_heap():
    test = MH.MinHeap()
    test.insert(1)

    test_against_array = np.zeros((test.get_max_size()))
    test_against_array[0] = 1

    assert all(map(lambda x: x[0] == x[1], list(zip(test.as_array(), test_against_array))[:test.get_heap_size()]))

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

    test_against_array = np.zeros((test.get_max_size()))
    test_against_array[0] = 1
    test_against_array[1] = 5
    test_against_array[2] = 7
    test_against_array[3] = 10

    assert all(map(lambda x: x[0] == x[1], list(zip(test.as_array(), test_against_array))[:test.get_heap_size()]))

def test_extract_min():
    # Same as test_insert_multiple_elements_into_empty_heap() to set up the tree for now/until we implement heap building function
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

    temp = test.extract_min()

    test_against_array = np.zeros((test.get_max_size()))
    test_against_array[0] = 5
    test_against_array[1] = 10
    test_against_array[2] = 7

    assert (temp, all(map(lambda x: x[0] == x[1], list(zip(test.as_array(), test_against_array))[:test.get_heap_size()]))) == (1, True)

def test_build_heap():
    test = np.array([10,9,8,7,6,5,4,3,2,1,0,3,2,1,0])
    test_heap = MH.build_heap(test)

    test_against_array = np.array([0,1,0,2,6,2,1,3,7,9,10,3,5,8,4])

    assert all(map(lambda x: x[0] == x[1], list(zip(test_heap.as_array(), test_against_array))[:test_heap.get_heap_size()]))

if __name__ == "__main__":
    test_create_new_heap()
    print ("test_create_new_heap passed!")

    test_insert_one_element_into_empty_heap()
    print ("test_insert_one_element_into_empty_heap passed!")

    test_insert_multiple_elements_into_empty_heap()
    print ("test_insert_multiple_elements_into_empty_heap passed!")

    test_extract_min()
    print ("test_extract_min passed!")

    test_build_heap()
    print ("test_build_heap passed!")