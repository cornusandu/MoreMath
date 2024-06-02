from __future__ import annotations
from Functions import IsPrime
from typing import Any

class Number(float):
    def __init__(self, value: int | float = 0):
        self.value = value
        self._val = value
        self.IsPrime = IsPrime

    def __repr__(self):
        return self.value

    def __int__(self):
        return round(self.value)

    def __str__(self):
        return str(self.value)

    def __float__(self):
        return float(self.value)