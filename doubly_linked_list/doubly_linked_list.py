from doubly_linked_list_node import DoublyLinkedLIstNode


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_front(self, value):
        temp_head = self.head
        self.head = DoublyLinkedLIstNode(value)
        self.head.set_next_node(temp_head)
        if self.length == 0:
            self.tail = self.head
        else:
            temp_head.set_previous_node(self.head)

        self.length += 1

    def enumerate(self, forward):
        if forward:
            current_node = self.head
        else:
            current_node = self.tail

        while current_node != None:
            if forward:
                current_node = self.head
            else:
                current_node = self.tail


