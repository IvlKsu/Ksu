"""
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


#>>> list(fizzbuzz(5))
['1', '2', 'fizz', '4', 'buzz']

* https://en.wikipedia.org/wiki/Fizz_buzz
"""
from typing import Generator


def fizzbuzz(n: int) -> Generator[str]:
    for i in range(1, n + 1):
        if i % 15 == 0:
            yield str("fizz-buzz")
        elif i % 3 == 0:
            yield str("fizz")
        elif i % 5 == 0:
           yield str("buzz")
        else:
            yield str(i)



