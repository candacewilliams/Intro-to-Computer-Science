class Queue:
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.append(value)
        
    def remove(self):
      self.queue.pop(0)

    def print_values(self):
      print(self.queue)

my_queue = Queue()
my_queue.add(5)
my_queue.add('pizza')
my_queue.add(False)
my_queue.add('sunshine')
my_queue.print_values()
my_queue.remove()
my_queue.print_values()
my_queue.add(42)
my_queue.remove()
my_queue.print_values()
