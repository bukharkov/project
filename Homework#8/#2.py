
class ErrorDiv(Exception):

    def __init__(self):
        self.text = 'Division by zero'


def division(numerator, denominator):

    try:
        if denominator == 0:
            raise ErrorDiv
        print(numerator / denominator)
    except ErrorDiv as err:
        print(err.text)

division(7, 0)

