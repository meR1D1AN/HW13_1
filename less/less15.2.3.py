import timeit


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_set_delet(self):
        self.x += 1
        self.y = 100
        del self.y


class PointSltots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_set_delet(self):
        self.x += 1
        self.y = 100
        del self.y


point_slots = PointSltots(1, 2)

print(point_slots)

point = Point(1, 2)

time_slotls = timeit.timeit(point_slots.get_set_delet)
time = timeit.timeit(point.get_set_delet)

print(time_slotls)
print(time)
