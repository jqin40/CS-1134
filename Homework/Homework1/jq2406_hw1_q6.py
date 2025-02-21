class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0] * d
        elif isinstance(d, list):
            self.coords = d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]
    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __sub__(self,other):
        if len(self) != len(other):
            raise ValueError("dimension mismatch")
        result = Vector(len(self))
        for i in range(len(result)):
            result[i] = self[i] - other[i]
        return result
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * -1
        return result
    def __mul__(self, factor):
        if isinstance(factor, int):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * factor
        elif isinstance(factor, Vector):
            if len(self) != len(factor):
                raise ValueError("dimension mismatch")
            result = 0
            for i in range(len(self)):
                result += self[i] * factor[i]
        return result
    def __rmul__(self, factor):
        return self * factor

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'
    def __repr__(self):
        return str(self)

def main():
    # a = Vector([1,2,3])
    # b = Vector(3)
    # c = Vector([2,2,2])
    # print(a)
    # print(b)
    # print(a-c)
    # d = -c
    # print(d)
    # print(a * 3) #3, 6, 9
    # print(2 * a) #2, 4, 6
    # print(a * b) #0
    # print(a * c) #12

    v1 = Vector(5)
    v1[1] = 10
    v1[-1] = 10
    print(v1)
    v2 = Vector([2, 4, 6, 8, 10])
    print(v2)
    u1 = v1+v2
    print(u1)
    u2 = -v2
    print(u2)
    u3 = 3 * v2
    print(u3)
    u4 = v2 * 3
    print(u4)
    u5 = v1 * v2
    print(u5)