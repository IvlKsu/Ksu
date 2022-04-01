"""
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(5))
['1', '2', 'fizz', '4', 'buzz']

* https://en.wikipedia.org/wiki/Fizz_buzz
"""
from typing import Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    for num in range(1, n + 1):
        yield "fizz" * (not num % 3) + "buzz" * (not num % 5) or str(num)
