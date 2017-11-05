def decide_alive(alive:bool, neighbours:int):
    if alive:
        return neighbours in (2, 3)
    else:
        return neighbours==3


def neighbour_iter(center_x, center_y):
    for x in range(center_x-1, center_x+2):
        for y in range(center_y-1, center_y+2):
            if x != center_x or y != center_y:
                yield (x, y)

class FieldBasics:
    def count_neighbours(self, center_x, center_y):
        result = 0
        for x, y in neighbour_iter(center_x, center_y):
            result += self.get(x, y)
        return result

    def __str__(self):
        fields = set(self.get_fields())
        min_x = min([x for x, y in fields])
        max_x = max([x for x, y in fields])
        min_y = min([y for x, y in fields])
        max_y = max([y for x, y in fields])

        result = []
        for y in range(min_y, max_y+1):
            row = [self.get(x, y) for x in range(min_x, max_x+1)]
            row = ['X' if field else '.' for field in row]
            result.append(''.join(row))
        return '\n'.join(result)


class InfiniteField(set, FieldBasics):
    """Infinited field based on set storage"""
    def get(self, x, y):
        return (x, y) in self

    def set(self, x, y, alive):
        if alive:
            self.add((x, y))
        else:
            self.discard((x, y))

    def get_fields(self):
        todo = set()
        for alive_field in self:
            todo.update(neighbour_iter(*alive_field))
        for field in todo:
            yield field

    def new(self):
        return InfiniteField()


class FixedField(list, FieldBasics):
    """Field of a fixed size, everything outside is dead.

    Implementation based on 2d list."""
    def __init__(self, size_x, size_y):
        for _ in range(size_x):
            self.append([False] * size_y)
        self.size_x = size_x
        self.size_y = size_y

    def get(self, x, y):
        if 0 <= x < self.size_x and 0 <= y < self.size_y:
            return self[x][y]
        return False

    def set(self, x, y, alive):
        if 0 <= x < self.size_x and 0 <= y < self.size_y:
            self[x][y] = alive

    def count_neighbours(self, center_x, center_y):
        result = 0
        for x, y in neighbour_iter(center_x, center_y):
            result += self.get(x, y)
        return result

    def get_fields(self):
        for x in range(self.size_x):
            for y in range(self.size_y):
                yield x, y

    def new(self):
        return FixedField(self.size_x, self.size_y)


class Game:
    def __init__(self, field):
        self.field = field

    def tick(self):
        next_field = self.field.new()
        for x, y in self.field.get_fields():
            alive = self.field.get(x, y)
            count = self.field.count_neighbours(x, y)
            next_state = decide_alive(alive, count)
            next_field.set(x, y, next_state)

        self.field = next_field


def main():
    # field = FixedField(3, 3)
    field = InfiniteField()
    
    g = Game(field)
    g.field.set(0, 0, True)
    g.field.set(0, 1, True)
    g.field.set(0, 2, True)

    print(g.field)
    print()

    g.tick()
    print(g.field)
    print()

    g.tick()
    print(g.field)


if __name__ == '__main__':
    main()
