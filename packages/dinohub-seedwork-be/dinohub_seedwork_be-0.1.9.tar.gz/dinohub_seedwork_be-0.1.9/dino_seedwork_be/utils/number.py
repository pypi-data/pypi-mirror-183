from typing import TypeVar

NumberType = TypeVar("NumberType", bound=int)

__all__ = ["increase"]
# Not pure
def increase(a_number: NumberType, amount: NumberType = 1):
    a_number = a_number + amount
    return a_number
