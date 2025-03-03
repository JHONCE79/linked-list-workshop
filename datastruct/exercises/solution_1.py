from datastruct.classes.lists import LinkedList


def add_two_numbers(l1: LinkedList[int], l2: LinkedList[int]) -> LinkedList[int]:

    list1 = l1.head
    list2 = l2.head

    sum_result = LinkedList[int]

    while list1 is not None and list2 is not None:
        if list1.value + list2.value >9:
            pass
        