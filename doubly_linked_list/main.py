from doubly_linked_list import DoublyLinkedList

def main():
    # add_to_front
    # empty list ATF(3) <=3=>
    d_list = DoublyLinkedList()
    d_list.add_to_front(3)
    # <=3=> ATF(4) <=3==4=>
    d_list.add_to_front(4)
    pass

if __name__ == "__main__":
    main()