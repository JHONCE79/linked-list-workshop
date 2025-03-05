from datastruct.classes.lists import LinkedList


def sort_list_by_insertion(linked_list: LinkedList[int]) -> LinkedList[int]:
    if linked_list.is_empty() or linked_list.head.next is None:
        return linked_list
    
    sorted_list = LinkedList[int]()
    current = linked_list.head
    while current:
        next_node = current.next      
        current_data = current.data
        
        if sorted_list.is_empty():
            sorted_list.insert(current_data)
        else:
            insert_position = sorted_list.head
            prev = None
        break