class Stack:
    def __init__(self, items=None, limit=None):
        self.items = items if items is not None else []
        self.limit = limit

    def push(self, value):
        if self.limit is not None and len(self.items) >= self.limit:
            return
        self.items.append(value)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        if self.limit is None:
            return False
        return len(self.items) >= self.limit

    def search(self, value):
        try:
            return len(self.items) - 1 - self.items.index(value)
        except ValueError:
            return -1
