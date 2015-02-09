class DoublyLinkedLIstNode(object):
    def __init(self, value):
        self.value = value
        self.previous_node = None
        self.next_node = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_previous_node(self):
        return self.previous_node

    def set_previous_node(self, node):
        self.previous_node = node

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, node):
        self.next_node = node