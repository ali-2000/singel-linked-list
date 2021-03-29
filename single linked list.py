class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data} ==> {self.next}"


class linked_list:
    def __init__(self, ite=None):
        self.head = None
        self.tail = None
        self.current = None
        if ite:
            self.extend(ite)

    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            self.tail = new
            self .current = self.head
        else:
            self.tail.next = new
            self.tail = new

    def extend(self, ite):
        for i in ite:
            self.append(i)

    def __len__(self):
        item = self.head
        c = 0
        while item:
            c += 1
            item = item.next
        return c

    def __getitem__(self, index):
        item = self.head
        c = 0
        while item:
            if c == index:
                return item.data
            c += 1
            item = item.next
        else:
            raise IndexError("index out of range")

    def __setitem__(self, key, value):
        item = self.head
        c = 0
        while item:
            if c == key:
                item.data = value
                return
            c += 1
            item = item.next
        else:
            raise IndexError("index out of range")

    def __str__(self):
        item = self.head
        l = len(self)
        s = ""
        c = 0
        while item:
            s += str(item.data)
            if c != l - 1:
                s += " ==> "
            item = item.next
            c += 1
        return s

    def __iter__(self):
        self .current = self.head
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data

    def insert(self, index, item):
        next = self.head
        previous = None
        c = 0
        while next:
            if c == index:
                new = Node(item)
                if previous:
                    previous.next = new
                else:
                    self.head = new
                new.next = next
                return
            c += 1
            previous = next
            next = next.next

    def __add__(self, other):
        new = linked_list()
        item = self.head
        while item:
            new.append(item.data)
            item = item.next
        item = other.head
        while item:
            new.append(item.data)
            item = item.next
        return new
        # self.tail.next = other.head
        # self.tail = other.tail
        # return self

    def revers(self):
        current = self.head
        previous = None
        next = self.head
        while current:
            next = next.next
            current.next = previous
            previous = current
            current = next
        self.head, self.tail = self.tail, self.head
        # n = len(self)
        # for i in range(n // 2):
        #     self[i], self[(n - 1) - i] = self[(n - 1) - i], self[i]


    def removeAt(self, index):
        next = self.head
        previous = None
        c = 0
        while next:
            if c == index:
                item = next.data
                if not previous:
                    self.head = self.head.next
                else:
                    previous.next = next.next
                return item
            c += 1
            previous = next
            next = next.next
        else:
            raise IndexError("index out of range")

    def remove(self, item):
        next = self.head
        previous = None
        while next:
            if next.data == item:
                if not previous:
                    self.head = self.head.next
                else:
                    previous.next = next.next
                return
            previous = next
            next = next.next


class Stack:
    def __init__(self,ite):
        self.items = linked_list()
        self.top = -1
        if ite:
            for i in ite:
                self.push(i)

    def is_empty(self):
        return len(self.items) == 0

    def push(self,item):
        self.items.append(item)
        self.top += 1

    def pop(self):
        if not self.is_empty():
            self.items.removeAt(self.top)
            self.top -= 1
