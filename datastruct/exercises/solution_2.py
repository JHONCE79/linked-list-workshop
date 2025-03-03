import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from datastruct.classes.lists import LinkedList

def swap_nodes_in_pairs(linked_list: LinkedList[int]) -> LinkedList[int]:
    if linked_list.head is None or linked_list.head.next is None:
        return linked_list
    
    new_head = linked_list.head.next
    prev = None
    current = linked_list.head
    
    while current and current.next:
        next_pair = current.next.next  
        second = current.next          
        
        second.next = current
        
        if prev:
            prev.next = second
        
        current.next = next_pair
    
    linked_list.head = new_head
    
    return linked_list

