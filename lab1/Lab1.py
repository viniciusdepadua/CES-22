import turtle
import math
import sys
import time


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def draw_this():
    """Makes a turtle draw 5 squares inside of each other"""

    bob = turtle.Turtle()
    for i in range(4):
        bob.up()
        bob.ht()
        bob.goto(-i * 10, -i * 10)
        bob.st()
        bob.down()
        for j in range(4):
            bob.forward(20 * (i + 1))
            bob.left(90)
    time.sleep(5)
    turtle.Screen().clear()


def draw_poly(t, n, sz):
    """makes a turtle 't' draw a regular
polygon with size sz and n sides."""

    s_intern_angles = (n - 2) * 180
    for i in range(n):
        t.forward(sz)
        t.left(180 - s_intern_angles / n)
    time.sleep(5)


def sum_to(n):
    """returns the sum of all integer numbers up
to and including n."""

    sum_value = 0
    for i in range(1, n + 1):
        sum_value = sum_value + i
    return sum_value


def test_sum_to():
    """Some tests cases to sse if the function is doing alright"""

    test(sum_to(100) == 5050)
    test(sum_to(10000) == 50005000)


def sum_list(list_data):
    """Sums all the elements in a list up to
but not including the first even number."""

    sum_value = 0
    for number in list_data:
        if number % 2 == 1:
            sum_value += number
        else:
            break
    return sum_value


def test_sum_list():
    """Some test cases to sse if the function is doing alright """

    test(sum_list([1, 5, 7, 3, 4, 5, 7, 9, 12]) == 16)
    test(sum_list([3, 3, 3, 3, 3, 3, 3]) == 21)
    test(sum_list([2, 2, 2, 2]) == 0)


def how_many_words(list_data):
    """Counts how many words occur in a list up to and including
    the first occurrence of the word “sam”."""

    words_number = 0
    for words in list_data:
        words_number += 1
        if words == "sam":
            break
    return words_number


def test_how_many_words():
    """Some test cases to see if the function is doing alright."""

    test(how_many_words(["hi ", "my ", "name ", "is ", "sam", "im", "okay"]) == 5)
    test(how_many_words(["hi ", "my ", "name ", "is ", "vinicius", "im", "okay"]) == 7)
    test(how_many_words([]) == 0)


def is_prime(number):
    """Check if a number is a prime number"""

    prime = True
    for i in range(2, math.floor(math.sqrt(number) + 1)):
        if number % i == 0:
            prime = False
            break
    return prime


def test_prime():
    """Test if function is doing ok with some test case"""

    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))


def sum_of_squares(xs):
    """Computes the sum of the squares of the
numbers in the list xs."""

    sum_squares = 0
    for number in xs:
        sum_squares += number * number
    return sum_squares


def test_sum_of_squares():
    """Some test cases to see if the function is doing alright"""

    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)


def draw_table(size):
    """Prints a neat looking multiplication table
 with size size x size """

    tab = len(str(size * size))
    header = " " * tab + " " * (2 * tab) + "1"
    dash_counter = 2 * tab
    for i in range(2, size + 1):
        header += " " * (tab + 1 - len(str(i))) + str(i)
        dash_counter += tab + 1
    header += "\n"
    dash = " " * tab + ":" + "-" * dash_counter + "\n"
    body = ""
    for i in range(1, size + 1):
        body = body + " " * (tab - len(str(i))) + str(i) + ":"
        body = body + " " * (2 * tab - len(str(i * 1))) + str(i * 1)
        for j in range(2, size + 1):
            body = body + " " * (tab + 1 - len(str(j * i))) + str(j * i)
        body = body + "\n"
    print(header + dash + body)


def is_palindrome(string):
    """A function that recognizes palindromes"""

    palindrome = False
    if string == string[len(string)::-1]:
        palindrome = True
    return palindrome


def test_is_palindrome():
    """Some test cases to see if the function is doing alright"""

    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))


def complex_sum(z, w):
    """ Representing a complex number as a tuple of
    two numeric values, and creating a function
    that calculates the addition of two of them """

    sum_complex = (z[0] + w[0], z[1] + w[1])
    return sum_complex


"""Tests to all function in this file
uncomment if you want to use"""
# draw_this()
# turtle.clear()
# jack = turtle.Turtle()
# draw_poly(jack, 6, 50)
# test_sum_to()
# test_sum_list()
# test_how_many_words()
# test_prime()
# test_sum_of_squares()
# draw_table(12)
# test_is_palindrome()
# print(complex_sum((1,2),(2,3)))
