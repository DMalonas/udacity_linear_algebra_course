class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def scalar_multiply(self, scalar):
        return Vector([scalar * a for a in self.components])

    def __repr__(self):
        return f"Vector({self.components})"

# Example usage:
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)
print("v1 * 3 =", v1.scalar_multiply(3))
