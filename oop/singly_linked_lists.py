class SList:

    def __init__(self):
        self.head = None

    def add_to_front(self, val):	
        new_node = SLNode(val)	# create a new instance of our Node class using the given value
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self,val):
        new_node = SLNode(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        current_head = self.head
        self.head = current_head.next
        return self

    def remove_from_back(self):
        runner = self.head
        while runner.next != None:
            previous_runner = runner
            runner = runner.next
        previous_runner.next = None
        return self

    def remove_val(self,val):
        runner = self.head
        while runner != None:
            if runner.value == val:
                runner = runner.next
                continue
            runner = runner.next
        
        return self

    def insert_at(self,val,n):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next



class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


my_list = SList()
my_list.add_to_front("are").add_to_front("Linked Lists").add_to_back("fun!")
my_list.add_to_front("test number 1")
my_list.add_to_back('testing')
# my_list.remove_from_front().print_values()
my_list.remove_from_back().print_values()
my_list.remove_val("are").print_values()