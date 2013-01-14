from calculator import Calculator, CalculationError


class CalculatorLibrary(object):
    """Test library for testing calculator business logic.

    Interaction with the calculator is done directly using its `push` method.
    """

    def __init__(self):
        self._calc = Calculator()
        self._result = ''

    def push_button(self, button):
        """Pushes the specified `button`.

        The given value is passed to the calculator directly. Valid buttons
        are everything that the calculator accepts.

        Examples:
        | `Push Button` | 1 |
        | `Push Button` | C |

        Use `Push Buttons` if you need to input longer expressions.
        """
        self._result = self._calc.push(button)

    def push_buttons(self, buttons):
        """Pushes the specified `buttons`.

        Uses `Push Button` to push all the buttons that must be given as
        a single string. Possible spaces are ignored.

        Example:
        | `Push Buttons` | 1 + 2 = |
        """
        for button in buttons.replace(' ',''):
            self.push_button(button)

    def result_should_be(self, expected):
        """Verifies that the current result is `expected`.

        Example:
        | `Push Buttons`     | 1 + 2 = |
        | `Result Should Be` | 3       |
        """
        if self._result != expected:
            raise AssertionError('%s != %s' % (self._result, expected))

    def should_fail(self, expression):
        """Verifies that calculating the given `expression` fails.

        The error message is returned.

        Examples:
        | `Should Fail`     | invalid       |                   |
        | ${error} =        | `Should Fail` | 1 / 0             |
        | `Should Be Equal` | ${error}      | Division by zero. |
        """
        try:
            self.push_buttons(expression)
        except CalculationError, err:
            return str(err)
        else:
            raise AssertionError("'%s' should have failed" % expression)
