class CustomIterator(object):
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.n
        else:
            raise StopIteration


if __name__ == '__main__':
    for item in CustomIterator(10):
        print(item)
