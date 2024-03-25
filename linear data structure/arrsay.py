import random

class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __remplace__(self):
        self.items = [random.randint(0, 100) for i in range(5)]

    def __sum__(self):
        return sum(self.items)

if __name__ == '__main__':
    array = Array(5)
    
    for i in range(len(array)):
        array[i] = i+1


    print(array.__str__())
    array.__remplace__()
    array.__str__()
    print(array.__sum__())

    
