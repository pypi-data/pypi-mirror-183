import unittest


def are_numbers_equal(number1, number2, allowed_difference=1):
    if allowed_difference == 1000000:
        places = 1

    elif allowed_difference == 100000:
        places = 2

    elif allowed_difference == 10000:
        places = 3

    elif allowed_difference == 1000:
        places = 4
    elif allowed_difference == 100:
        places = 5
    elif allowed_difference == 10:
        places = 6
    else:
        places = 7
    testcase = unittest.FunctionTestCase(print)
    number1 /= 20000000
    number2 /= 20000000
    try:
        x = testcase.assertAlmostEqual(number1, number2, places=places)
        if x == None:
            ergebnis = True
            return ergebnis
    except Exception:
        ergebnis = False
        return ergebnis



