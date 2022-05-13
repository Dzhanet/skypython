class Box():
    def __init__(self, size, weight, contains):
        self.size = size
        self.weight = weight
        self.contains = contains

    def observe(self):
        return (f"Это похоже на ящик размером {self.size} и весом {self.weight}кг")


class Container(Box):
    pass


box_1 = Box("30x30", 1, "15 золотых монет")
print(box_1.observe())