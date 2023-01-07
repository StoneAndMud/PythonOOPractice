"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Creates a base number and start"""
        self.base = start
        self.start = start

    def __repr__(self):
        """Returns the class and its attributes"""
        return F"<Serial Generator start={(self.base)} next={(self.base + 1)}>"

    def generate(self):
        """Generates a number that increments positevly by 1"""
        self.start += 1
        return self.start - 1

    def reset(self):
        """Resets to the base number given"""
        self.start = self.base


serial = SerialGenerator(start=100)

print(serial.__repr__())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())
print(serial.generate())
