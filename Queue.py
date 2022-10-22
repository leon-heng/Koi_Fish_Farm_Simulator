import time


class Queue(object):
    
    def __int__(self):
        self.item = []

    def __repr__(self) -> str:
        return "{}".format(self.item)

    def str(self) -> str:
        return "{}".format(self.item)

    def enque(self, item):
        self.item.insert(0, item)
        return True

    def size(self):
        return len(self.item)

    def isempty(self):
        if self.size() == 0:
            return True
        else:
            return False
    
    def deque(self):
        if self.isempty():
            return None
        else:
            return self.item.pop()