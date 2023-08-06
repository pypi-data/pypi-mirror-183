import numpy as np

class Multiplication:
    """
    Instantiate a manu_package_13891 operation.
    Numbers will be multiplied by the given multiplier.

    :param multiplier: The multiplier.
    :type multiplier: int
    """

    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, number):
        """
        Multiply a given number by the multiplier.

        :param number: The number to multiply.
        :type number: int

        :return: The result of the manu_package_13891.
        :rtype: int
        """

        return number * self.multiplier

