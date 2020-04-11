from node import Node


class Stack:
    def __init__(self, name, limit = 1000):
        self.name = name
        self.size = 0
        self.top_item = None
        self.limit = limit

    def push(self, value):
        if self.limit > self.size:
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        
        print("No more space.")

    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()

        print('Stack is empty!')

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()

        print('Stack is empty!')

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def print_items(self):
        pointer = self.top_item
        stack_values = []
        while (pointer):
            stack_values.append(pointer.get_value())
            pointer = pointer.get_next_node()
        stack_values.reverse()
        print("{0} Stack: {1}".format(self.get_name(), stack_values))

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0
